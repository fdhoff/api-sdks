package gitearest

import (
	"encoding/base64"
	"errors"
	"iter"
	"log/slog"
	"net/http"
	"net/url"
	"strings"
	"time"

	"github.com/fdhoff/api-sdks/apis/gitea/packages/go/internal/runtime"
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
	// Credentials supplies each request's credentials. [Token], [Basic] and [BasicWithOTP] cover
	// Gitea's own schemes; pass your own to [NewClient] for anything else.
	Credentials = runtime.Credentials
	// AuthRequest is one attempt's request, as [Credentials] sees it before it is sent.
	AuthRequest = runtime.AuthRequest
)

// APIPath is what [NewClient] adds to the instance URL.
const APIPath = "/api/v1"

// Ptr returns a pointer to value, for setting optional fields.
func Ptr[T any](value T) *T { return &value }

// staticCredentials are the credentials this package builds, with the reason they cannot be used,
// if any, for [NewClient] to return.
type staticCredentials struct {
	runtime.StaticCredentials
	problem string
}

// Token returns credentials that send an access token as `Authorization: token <token>`. The
// client keeps it only in memory and never logs it.
func Token(token string) Credentials {
	credentials := staticCredentials{StaticCredentials: runtime.StaticCredentials{
		Header: http.Header{"Authorization": {"token " + token}},
		Values: []string{token},
	}}
	if token == "" {
		credentials.problem = "the token must not be empty"
	}
	return credentials
}

// Basic returns credentials that send a username and password with Basic authentication. The
// password and the encoded header are never logged.
func Basic(username, password string) Credentials {
	return basic(username, password, nil)
}

// BasicWithOTP returns [Basic] credentials that also send a current one-time password as
// X-GITEA-OTP, for an account with two-factor authentication on. The one-time password is never
// logged.
func BasicWithOTP(username, password, otp string) Credentials {
	return basic(username, password, &otp)
}

func basic(username, password string, otp *string) Credentials {
	encoded := base64.StdEncoding.EncodeToString([]byte(username + ":" + password))
	credentials := staticCredentials{StaticCredentials: runtime.StaticCredentials{
		Header: http.Header{"Authorization": {"Basic " + encoded}},
		Values: []string{password, encoded},
	}}
	if otp != nil {
		credentials.Header.Set("X-GITEA-OTP", *otp)
		credentials.Values = append(credentials.Values, *otp)
	}
	switch {
	case username == "":
		credentials.problem = "the username must not be empty"
	case password == "":
		credentials.problem = "the password must not be empty"
	case otp != nil && *otp == "":
		credentials.problem = "the one-time password must not be empty"
	}
	return credentials
}

type options struct {
	sudo          *string
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

// WithSudo makes every call act as another user, sent as the Sudo header. It needs an admin's
// credentials.
func WithSudo(username string) Option { return func(o *options) { o.sudo = &username } }

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

// WithLogger sets where the client logs methods, URLs and statuses, never your credentials or
// response bodies. By default it logs nothing.
func WithLogger(logger *slog.Logger) Option { return func(o *options) { o.logger = logger } }

// Client calls the API. It is safe for concurrent use, and its resources are its fields.
type Client struct {
	Resources
}

func apiURL(baseURL string) (string, error) {
	parsed, err := url.Parse(baseURL)
	if err != nil || (parsed.Scheme != "https" && parsed.Scheme != "http") || parsed.Host == "" {
		return "", errors.New("the base URL must be your Gitea instance's URL, such as https://gitea.example.com")
	}
	if parsed.RawQuery != "" || parsed.Fragment != "" || parsed.User != nil {
		return "", errors.New("the base URL must not have a query, fragment or user")
	}
	root := strings.TrimRight(baseURL, "/")
	if strings.HasSuffix(root, APIPath) {
		return "", errors.New("the base URL is the instance's URL; leave out " + APIPath + ", which the client adds")
	}
	return root + APIPath, nil
}

// NewClient builds a client for one Gitea instance. baseURL is the instance's own URL, such as
// https://gitea.example.com, or https://example.com/git for an instance under a sub-path; the
// client adds /api/v1. There is no default. Your credentials are sent only to it. Pass [Token],
// [Basic] or [BasicWithOTP].
func NewClient(baseURL string, credentials Credentials, opts ...Option) (*Client, error) {
	root, err := apiURL(baseURL)
	if err != nil {
		return nil, err
	}
	if credentials == nil {
		return nil, errors.New("credentials are required; pass Token, Basic or BasicWithOTP")
	}
	if static, isStatic := credentials.(staticCredentials); isStatic && static.problem != "" {
		return nil, errors.New(static.problem)
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
	if config.sudo != nil {
		if *config.sudo == "" {
			return nil, errors.New("the sudo username must not be empty")
		}
		headers.Set("Sudo", *config.sudo)
	}
	transport, err := runtime.NewTransport(runtime.Settings{
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
	if err != nil {
		return nil, err
	}
	return &Client{Resources: newResources(transport)}, nil
}
