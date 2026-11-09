package mercurybanking

import (
	"errors"
	"iter"
	"log/slog"
	"maps"
	"net/http"
	"time"

	"github.com/fdhoff/api-sdks/apis/mercury/packages/go/internal/runtime"
)

// The environments [WithEnvironment] takes.
const (
	Production = "production"
	Sandbox    = "sandbox"
)

// Mercury documents no sandbox host for card details, so those calls go to the sandbox's own API host.
var environments = map[string]map[string]string{
	Production: {"api": "https://api.mercury.com/api/v1", "vault": "https://vault-api.mercury.com/api/v1"},
	Sandbox:    {"api": "https://api-sandbox.mercury.com/api/v1", "vault": "https://api-sandbox.mercury.com/api/v1"},
}

// Environments returns the base URL of each host the API uses, by environment. vault serves only
// [CardsResource.Reveal]. The result is a copy.
func Environments() map[string]map[string]string {
	copied := make(map[string]map[string]string, len(environments))
	for name, hosts := range environments {
		copied[name] = maps.Clone(hosts)
	}
	return copied
}

type (
	// File is a file to upload.
	File = runtime.File
	// Time is a date and time in the API.
	Time = time.Time
	// Seq iterates items and stops after yielding an error.
	Seq[T any] = iter.Seq2[T, error]
	// Download is a binary response. The caller must close its Body.
	Download = runtime.Download
)

// Ptr returns a pointer to value, for setting optional fields.
func Ptr[T any](value T) *T { return &value }

type options struct {
	environment   string
	hosts         map[string]string
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

// WithEnvironment picks the hosts: [Production], the default, or [Sandbox]. A sandbox token works
// only in the sandbox.
func WithEnvironment(environment string) Option {
	return func(o *options) { o.environment = environment }
}

// WithHosts sets your own base URL for each of the api and vault hosts, such as a mock's, instead of
// the environment's. Your token is sent to them.
func WithHosts(hosts map[string]string) Option {
	return func(o *options) { o.hosts = maps.Clone(hosts) }
}

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

// WithLogger sets where the client logs methods, URLs and statuses, never your token or response
// bodies. By default it logs nothing.
func WithLogger(logger *slog.Logger) Option { return func(o *options) { o.logger = logger } }

// Client calls the API. It is safe for concurrent use, and its resources are its fields.
type Client struct {
	Resources
}

// NewClient builds a client. token is your API token, sent verbatim as a bearer token; the
// secret-token: prefix is part of it. The client keeps it only in memory and never logs it.
func NewClient(token string, opts ...Option) (*Client, error) {
	if token == "" {
		return nil, errors.New("token is required")
	}
	config := options{
		environment:   Production,
		timeout:       30 * time.Second,
		maxRetries:    3,
		retryBase:     500 * time.Millisecond,
		rateLimitWait: 10 * time.Second,
		maxRetryWait:  60 * time.Second,
	}
	for _, option := range opts {
		option(&config)
	}
	hosts, err := runtime.SelectHosts(environments, config.environment, config.hosts)
	if err != nil {
		return nil, err
	}
	headers := http.Header{"Accept": {"application/json"}}
	if config.userAgent != "" {
		headers.Set("User-Agent", config.userAgent)
	}
	transport, err := runtime.NewTransport(runtime.Settings{
		BaseURL: hosts["api"],
		Hosts:   hosts,
		Credentials: runtime.StaticCredentials{
			Header: http.Header{"Authorization": {"Bearer " + token}},
			Values: []string{token},
		},
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
	return &Client{newResources(transport)}, nil
}
