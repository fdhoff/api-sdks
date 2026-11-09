package miraklseller

import (
	"context"
	"errors"
	"iter"
	"log/slog"
	"net/http"
	"net/url"
	"slices"
	"strconv"
	"strings"
	"time"

	"github.com/fdhoff/api-sdks/apis/mirakl/packages/go/internal/runtime"
)

type (
	// File is a file to upload.
	File = runtime.File
	// Time is a date and time in the API.
	Time = time.Time
	// Seq iterates items and stops after yielding an error.
	Seq[T any] = iter.Seq2[T, error]
	// Download is a binary response. The caller must close its Body.
	Download = runtime.Download
	// WaitOptions sets how often a wait polls and for how long. Mirakl allows about one status call a
	// minute, so a shorter interval may be rate limited.
	WaitOptions = runtime.WaitOptions
	// Credentials supplies each request's credentials. [APIKey] covers the usual shop API key; pass
	// your own to [NewClient] for anything else.
	Credentials = runtime.Credentials
	// AuthRequest is one attempt's request, as [Credentials] sees it before it is sent.
	AuthRequest = runtime.AuthRequest
)

// shopAPIKey is the spec's one security scheme, which [Client.DownloadURL] names for credentials.
var shopAPIKey = runtime.Requirement{{Name: "Shop-API-Key"}}

// Ptr returns a pointer to value, for setting optional fields.
func Ptr[T any](value T) *T { return &value }

// APIKey returns credentials that send key as the whole Authorization header, with no scheme, as
// Mirakl expects. The client keeps it only in memory and never logs it.
func APIKey(key string) Credentials {
	return runtime.StaticCredentials{Header: http.Header{"Authorization": {key}}, Values: []string{key}}
}

type options struct {
	shopID        *int64
	userAgent     string
	logger        *slog.Logger
	httpTransport http.RoundTripper
	timeout       time.Duration
	maxRetries    int
	retryBase     time.Duration
	rateLimitWait time.Duration
	maxRetryWait  time.Duration
}

// Option configures a [Client].
type Option func(*options)

// WithShopID sets the shop every call acts for when the key covers several. A call's own ShopID
// wins. Without either, the operator uses the key's default shop.
func WithShopID(shopID int64) Option { return func(o *options) { o.shopID = &shopID } }

// WithUserAgent sets the User-Agent header.
func WithUserAgent(userAgent string) Option { return func(o *options) { o.userAgent = userAgent } }

// WithTimeout sets the deadline for each attempt, from sending the request to reading the last
// byte of the response. The default is 30 seconds.
func WithTimeout(timeout time.Duration) Option { return func(o *options) { o.timeout = timeout } }

// WithMaxRetries sets the retries after the first attempt. The default is 3.
func WithMaxRetries(retries int) Option { return func(o *options) { o.maxRetries = retries } }

// WithRetryBaseDelay sets the base of the exponential backoff. The default is 500 milliseconds.
func WithRetryBaseDelay(delay time.Duration) Option { return func(o *options) { o.retryBase = delay } }

// WithRateLimitWait sets the wait after a 429 with no usable Retry-After. The default is 10 seconds.
func WithRateLimitWait(wait time.Duration) Option { return func(o *options) { o.rateLimitWait = wait } }

// WithMaxRetryWait sets the longest Retry-After to wait for. The default is 60 seconds. A longer one
// returns a rate-limited error at once, with the header's value in RetryAfter.
func WithMaxRetryWait(wait time.Duration) Option { return func(o *options) { o.maxRetryWait = wait } }

// WithHTTPTransport sets the [http.RoundTripper] to use instead of [http.DefaultTransport].
func WithHTTPTransport(transport http.RoundTripper) Option {
	return func(o *options) { o.httpTransport = transport }
}

// WithLogger sets where the client logs methods, URLs and statuses, never your key or response
// bodies. By default it logs nothing.
func WithLogger(logger *slog.Logger) Option { return func(o *options) { o.logger = logger } }

// Client calls the API. It is safe for concurrent use, and its resources are its fields.
type Client struct {
	Resources
	transport *runtime.Transport
}

func cleanBaseURL(baseURL string) (string, error) {
	parsed, err := url.Parse(baseURL)
	if err != nil || (parsed.Scheme != "https" && parsed.Scheme != "http") || parsed.Host == "" {
		return "", errors.New("the base URL must be an absolute http or https URL, such as your operator's https://<instance>.mirakl.net")
	}
	if parsed.RawQuery != "" || parsed.Fragment != "" {
		return "", errors.New("the base URL must not have a query or fragment")
	}
	return strings.TrimRight(baseURL, "/"), nil
}

// NewClient builds a client for one operator's Mirakl instance. baseURL is the instance's root,
// before /api, which the operator gives you: there is no shared host and no public sandbox. Your
// credentials are sent only to it. Pass [APIKey] with your shop API key.
func NewClient(baseURL string, credentials Credentials, opts ...Option) (*Client, error) {
	root, err := cleanBaseURL(baseURL)
	if err != nil {
		return nil, err
	}
	if credentials == nil {
		return nil, errors.New("credentials are required; pass APIKey with your shop API key")
	}
	if static, isStatic := credentials.(runtime.StaticCredentials); isStatic && slices.Contains(static.Values, "") {
		return nil, errors.New("the API key is required")
	}
	config := options{
		timeout:       30 * time.Second,
		maxRetries:    3,
		retryBase:     500 * time.Millisecond,
		rateLimitWait: 10 * time.Second,
		maxRetryWait:  60 * time.Second,
	}
	for _, option := range opts {
		option(&config)
	}
	headers := http.Header{"Accept": {"application/json"}}
	if config.userAgent != "" {
		headers.Set("User-Agent", config.userAgent)
	}
	var queryDefaults map[string]string
	if config.shopID != nil {
		queryDefaults = map[string]string{"shop_id": strconv.FormatInt(*config.shopID, 10)}
	}
	transport, err := runtime.NewTransport(runtime.Settings{
		BaseURL:        root,
		QueryDefaults:  queryDefaults,
		Credentials:    credentials,
		Headers:        headers,
		ToError:        toError,
		Logger:         config.logger,
		HTTPTransport:  config.httpTransport,
		Timeout:        config.timeout,
		MaxRetries:     config.maxRetries,
		RetryBaseDelay: config.retryBase,
		RateLimitWait:  config.rateLimitWait,
		MaxRetryWait:   config.maxRetryWait,
	})
	if err != nil {
		return nil, err
	}
	return &Client{Resources: newResources(transport), transport: transport}, nil
}

// DownloadURL fetches an absolute URL that a response returned, such as a file of a finished
// export, following up to five redirects. Your credentials go only to the base URL's scheme, host
// and port, and never again once a redirect leaves them. The URL is logged without its query,
// which may hold a signature. The caller must close the download's Body.
func (c *Client) DownloadURL(ctx context.Context, address string) (*Download, error) {
	return runtime.DownloadURL(ctx, c.transport, address, shopAPIKey)
}
