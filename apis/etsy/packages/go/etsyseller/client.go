package etsyseller

import (
	"errors"
	"iter"
	"log/slog"
	"net/http"
	"net/url"
	"strings"
	"time"

	"github.com/fdhoff/api-sdks/apis/etsy/packages/go/internal/runtime"
)

// BaseURL is the API's server root.
const BaseURL = "https://openapi.etsy.com"

type (
	// File is a file to upload.
	File = runtime.File
	// Time is a date and time in the API.
	Time = time.Time
	// Seq iterates items and stops after yielding an error.
	Seq[T any] = iter.Seq2[T, error]
)

// Ptr returns a pointer to value, for setting optional fields.
func Ptr[T any](value T) *T { return &value }

type options struct {
	accessToken   string
	refreshToken  string
	onToken       func(Token)
	userAgent     string
	baseURL       string
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

// WithAccessToken sets an OAuth access token, sent verbatim as a bearer token on the operations
// that need one.
func WithAccessToken(token string) Option { return func(o *options) { o.accessToken = token } }

// WithRefreshToken lets the client replace an expired access token by itself, once per call.
func WithRefreshToken(token string) Option { return func(o *options) { o.refreshToken = token } }

// WithOnToken sets a function called with every new token pair, from [OAuth.ExchangeCode] and every
// refresh, so you can store it. The old refresh token stops working. It runs before the call that
// obtained the token continues, and must not call the client.
func WithOnToken(onToken func(Token)) Option { return func(o *options) { o.onToken = onToken } }

// WithUserAgent sets the User-Agent header.
func WithUserAgent(userAgent string) Option { return func(o *options) { o.userAgent = userAgent } }

// WithBaseURL sets the server root, for tests against a mock. Your credentials are sent to it.
func WithBaseURL(baseURL string) Option { return func(o *options) { o.baseURL = baseURL } }

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

// WithLogger sets where the client logs methods, URLs and statuses, never your credentials or
// response bodies. By default it logs nothing.
func WithLogger(logger *slog.Logger) Option { return func(o *options) { o.logger = logger } }

// Client calls the API. It is safe for concurrent use, and its resources are its fields.
type Client struct {
	Resources
	// OAuth obtains and refreshes the access token this client sends.
	OAuth *OAuth
}

func baseURL(root string) (string, error) {
	parsed, err := url.Parse(root)
	if err != nil || parsed.Scheme == "" || parsed.Host == "" {
		return "", errors.New("the base URL must be absolute")
	}
	return strings.TrimRight(root, "/"), nil
}

// NewClient builds a client for your app. apiKey is its keystring and sharedSecret its shared
// secret; both are sent as x-api-key on every API call, though not on token requests. The client
// keeps every credential only in memory.
func NewClient(apiKey, sharedSecret string, opts ...Option) (*Client, error) {
	if apiKey == "" || sharedSecret == "" {
		return nil, errors.New("apiKey and sharedSecret are required")
	}
	config := options{
		baseURL:       BaseURL,
		timeout:       30 * time.Second,
		maxRetries:    3,
		retryBase:     500 * time.Millisecond,
		rateLimitWait: 10 * time.Second,
		maxRetryWait:  60 * time.Second,
	}
	for _, option := range opts {
		option(&config)
	}
	root, err := baseURL(config.baseURL)
	if err != nil {
		return nil, err
	}
	credentials := newCredentials(apiKey, sharedSecret, config.accessToken, config.refreshToken, config.onToken)
	headers := http.Header{"Accept": {"application/json"}}
	if config.userAgent != "" {
		headers.Set("User-Agent", config.userAgent)
	}
	transport := runtime.NewTransport(runtime.Settings{
		BaseURL:        root,
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
	oauth := &OAuth{credentials: credentials, transport: transport, busy: make(chan struct{}, 1)}
	credentials.oauth = oauth
	return &Client{Resources: newResources(transport), OAuth: oauth}, nil
}
