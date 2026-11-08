package backmarketseller

import (
	"errors"
	"fmt"
	"iter"
	"log/slog"
	"net/http"
	"net/url"
	"strings"
	"time"

	"github.com/fdhoff/api-sdks/apis/backmarket/packages/go/internal/runtime"
)

// Region selects a marketplace region.
type Region string

// The marketplace regions.
const (
	RegionAP Region = "ap"
	RegionEU Region = "eu"
	RegionNA Region = "na"
)

// Environment selects production or preprod.
type Environment string

// The environments.
const (
	EnvironmentProduction Environment = "production"
	EnvironmentPreprod    Environment = "preprod"
)

type server struct {
	region      Region
	environment Environment
}

var servers = map[server]string{
	{RegionAP, EnvironmentProduction}: "https://www.backmarket.co.jp",
	{RegionAP, EnvironmentPreprod}:    "https://preprod.backmarket.co.jp",
	{RegionEU, EnvironmentProduction}: "https://www.backmarket.fr",
	{RegionEU, EnvironmentPreprod}:    "https://preprod.backmarket.fr",
	{RegionNA, EnvironmentProduction}: "https://www.backmarket.com",
	{RegionNA, EnvironmentPreprod}:    "https://preprod.backmarket.com",
}

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
	region        Region
	environment   Environment
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

// WithRegion selects the marketplace region. Pass this or [WithBaseURL].
func WithRegion(region Region) Option { return func(o *options) { o.region = region } }

// WithEnvironment selects production, the default, or preprod.
func WithEnvironment(environment Environment) Option {
	return func(o *options) { o.environment = environment }
}

// WithBaseURL sets a server root, for tests against a mock. Your token is sent to it.
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

// WithLogger sets where the client logs methods, URLs and statuses, never your token or response
// bodies. By default it logs nothing.
func WithLogger(logger *slog.Logger) Option { return func(o *options) { o.logger = logger } }

// Client calls the API. It is safe for concurrent use, and its resources are its fields.
type Client struct {
	Resources
}

func baseURL(config options) (string, error) {
	if (config.region == "") == (config.baseURL == "") {
		return "", errors.New("pass exactly one of WithRegion and WithBaseURL")
	}
	if config.baseURL == "" {
		root, found := servers[server{config.region, config.environment}]
		if !found {
			return "", fmt.Errorf("unknown region %q or environment %q", config.region, config.environment)
		}
		return root, nil
	}
	parsed, err := url.Parse(config.baseURL)
	if err != nil || parsed.Scheme == "" || parsed.Host == "" {
		return "", errors.New("the base URL must be absolute")
	}
	return strings.TrimRight(config.baseURL, "/"), nil
}

// NewClient builds a client. Your token is sent verbatim, and the client stores it only in memory.
// userAgent is required, in the form BM-{Company}-{Integration};contact@example.com. locale is sent
// as Accept-Language on every call, for example fr-fr.
func NewClient(token, userAgent, locale string, opts ...Option) (*Client, error) {
	if token == "" {
		return nil, errors.New("token is required")
	}
	if userAgent == "" {
		return nil, errors.New("userAgent is required; the API may refuse a request without it")
	}
	config := options{
		environment:   EnvironmentProduction,
		timeout:       30 * time.Second,
		maxRetries:    3,
		retryBase:     500 * time.Millisecond,
		rateLimitWait: 10 * time.Second,
		maxRetryWait:  60 * time.Second,
	}
	for _, option := range opts {
		option(&config)
	}
	root, err := baseURL(config)
	if err != nil {
		return nil, err
	}
	transport := runtime.NewTransport(runtime.Settings{
		BaseURL: root,
		Credentials: runtime.StaticCredentials{
			Header: http.Header{"Authorization": {"Basic " + token}},
			Values: []string{token},
		},
		Headers: http.Header{
			"User-Agent":      {userAgent},
			"Accept":          {"application/json"},
			"Accept-Language": {locale},
		},
		ToError:        toError,
		Logger:         config.logger,
		HTTPTransport:  config.httpTransport,
		Timeout:        config.timeout,
		MaxRetries:     config.maxRetries,
		RetryBaseDelay: config.retryBase,
		RateLimitWait:  config.rateLimitWait,
		MaxRetryWait:   config.maxRetryWait,
	})
	return &Client{newResources(transport)}, nil
}
