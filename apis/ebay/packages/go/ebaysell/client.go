package ebaysell

import (
	"errors"
	"log/slog"
	"maps"
	"net/http"
	"slices"
	"strings"
	"time"

	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/account"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/accountv2"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/analytics"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/developeranalytics"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/feed"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/feedback"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/finances"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/fulfillment"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/identity"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/inventory"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/keymanagement"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/marketing"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/media"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/message"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/metadata"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/negotiation"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/notification"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/postorder"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/recommendation"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/stores"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/taxonomy"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/internal/runtime"
)

// The environments [WithEnvironment] takes.
const (
	Production = "production"
	Sandbox    = "sandbox"
)

var environments = map[string]map[string]string{
	Production: {"api": "https://api.ebay.com", "apiz": "https://apiz.ebay.com", "apim": "https://apim.ebay.com"},
	Sandbox:    {"api": "https://api.sandbox.ebay.com", "apiz": "https://apiz.sandbox.ebay.com", "apim": "https://apim.sandbox.ebay.com"},
}

// Environments returns the base URL of each host the APIs use, by environment. The result is a copy.
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
)

// Ptr returns a pointer to value, for setting optional fields.
func Ptr[T any](value T) *T { return &value }

type options struct {
	clientID        string
	clientSecret    string
	ruName          string
	appToken        string
	userToken       string
	refreshToken    string
	onToken         func(Token)
	appScopes       []string
	userScopes      []string
	environment     string
	hosts           map[string]string
	marketplaceID   string
	contentLanguage string
	signingKey      *SigningKey
	userAgent       string
	logger          *slog.Logger
	httpTransport   http.RoundTripper
	timeout         time.Duration
	maxRetries      int
	retryBase       time.Duration
	rateLimitWait   time.Duration
	maxRetryWait    time.Duration
	now             func() time.Time
}

// Option configures a [Client].
type Option func(*options)

// WithClientCredentials sets your keyset's App ID and Cert ID. With them the client mints application
// tokens itself and can exchange and refresh user tokens. They are sent only to the token endpoint.
func WithClientCredentials(clientID, clientSecret string) Option {
	return func(o *options) { o.clientID, o.clientSecret = clientID, clientSecret }
}

// WithRuName sets your app's redirect URL name, for the authorization code grant.
func WithRuName(ruName string) Option { return func(o *options) { o.ruName = ruName } }

// WithAppToken sets an application token to use instead of minting one.
func WithAppToken(token string) Option { return func(o *options) { o.appToken = token } }

// WithUserToken sets a user access token, sent on operations that act for a seller.
func WithUserToken(token string) Option { return func(o *options) { o.userToken = token } }

// WithRefreshToken lets the client replace an expired user token by itself, once per call.
func WithRefreshToken(token string) Option { return func(o *options) { o.refreshToken = token } }

// WithOnToken sets a function called with every new user token, from [OAuth.ExchangeCode] and every
// refresh, so you can store it. It runs before the call that obtained the token continues, while the
// client holds its token locks, so it must not call the client: calling [OAuth.Refresh] from it
// deadlocks.
func WithOnToken(onToken func(Token)) Option { return func(o *options) { o.onToken = onToken } }

// WithAppScopes sets the scopes of minted application tokens. The default is [APIScope]. [NewClient]
// fails without at least one.
func WithAppScopes(scopes ...string) Option {
	return func(o *options) { o.appScopes = append([]string(nil), scopes...) }
}

// WithUserScopes sets the scopes to ask for when refreshing a user token. eBay keeps the original
// grant's when none are set.
func WithUserScopes(scopes ...string) Option {
	return func(o *options) { o.userScopes = append([]string(nil), scopes...) }
}

// WithEnvironment picks the API hosts and the authorization URL: [Production], the default, or
// [Sandbox].
func WithEnvironment(environment string) Option {
	return func(o *options) { o.environment = environment }
}

// WithHosts sets your own base URL for each of the api, apiz and apim hosts, such as a mock's,
// instead of the environment's. Your credentials are sent to them.
func WithHosts(hosts map[string]string) Option {
	return func(o *options) { o.hosts = maps.Clone(hosts) }
}

// WithMarketplaceID is sent as X-EBAY-C-MARKETPLACE-ID on operations that take it, unless a call
// passes its own.
func WithMarketplaceID(marketplaceID string) Option {
	return func(o *options) { o.marketplaceID = marketplaceID }
}

// WithContentLanguage is sent as Content-Language on operations that take it, unless a call passes
// its own.
func WithContentLanguage(language string) Option {
	return func(o *options) { o.contentLanguage = language }
}

// WithSigningKey signs every request, as eBay requires of EU and UK sellers on some calls.
func WithSigningKey(key SigningKey) Option { return func(o *options) { o.signingKey = &key } }

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

// Client calls the APIs. It is safe for concurrent use. Each API is a field, holding that API's
// resources.
type Client struct {
	Account            account.Resources
	AccountV2          accountv2.Resources
	Analytics          analytics.Resources
	Feed               feed.Resources
	Finances           finances.Resources
	Fulfillment        fulfillment.Resources
	Inventory          inventory.Resources
	Marketing          marketing.Resources
	Metadata           metadata.Resources
	Negotiation        negotiation.Resources
	Recommendation     recommendation.Resources
	Stores             stores.Resources
	PostOrder          postorder.Resources
	Feedback           feedback.Resources
	Identity           identity.Resources
	Media              media.Resources
	Message            message.Resources
	Notification       notification.Resources
	Taxonomy           taxonomy.Resources
	DeveloperAnalytics developeranalytics.Resources
	KeyManagement      keymanagement.Resources
	// OAuth obtains and refreshes the tokens this client sends.
	OAuth *OAuth
}

func headerDefaults(config options) map[string]string {
	defaults := map[string]string{}
	if config.marketplaceID != "" {
		defaults["X-EBAY-C-MARKETPLACE-ID"] = config.marketplaceID
	}
	if config.contentLanguage != "" {
		defaults["Content-Language"] = config.contentLanguage
	}
	return defaults
}

// NewClient builds a client. Pass [WithClientCredentials], a token, or both. The client keeps every
// credential only in memory.
func NewClient(opts ...Option) (*Client, error) {
	config := options{
		appScopes:     []string{APIScope},
		environment:   Production,
		timeout:       30 * time.Second,
		maxRetries:    3,
		retryBase:     500 * time.Millisecond,
		rateLimitWait: 10 * time.Second,
		maxRetryWait:  60 * time.Second,
		now:           time.Now,
	}
	for _, option := range opts {
		option(&config)
	}
	if _, found := authorizationURLs[config.environment]; !found {
		return nil, unknownEnvironment(config.environment)
	}
	if (config.clientID == "") != (config.clientSecret == "") {
		return nil, errors.New("pass the client ID and client secret together")
	}
	if config.clientID == "" && config.appToken == "" && config.userToken == "" && config.refreshToken == "" {
		return nil, errors.New("pass WithClientCredentials, or a token")
	}
	if !slices.ContainsFunc(config.appScopes, func(scope string) bool { return strings.TrimSpace(scope) != "" }) {
		return nil, errors.New("pass at least one scope to WithAppScopes")
	}
	hosts, err := runtime.SelectHosts(environments, config.environment, config.hosts)
	if err != nil {
		return nil, err
	}
	credentials, err := newCredentials(config)
	if err != nil {
		return nil, err
	}
	headers := http.Header{"Accept": {"application/json"}}
	if config.userAgent != "" {
		headers.Set("User-Agent", config.userAgent)
	}
	transport, err := runtime.NewTransport(runtime.Settings{
		BaseURL:        hosts["api"],
		Hosts:          hosts,
		HeaderDefaults: headerDefaults(config),
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
	oauth := newOAuth(credentials, transport, config)
	credentials.oauth = oauth
	return &Client{
		Account:            account.NewResources(transport),
		AccountV2:          accountv2.NewResources(transport),
		Analytics:          analytics.NewResources(transport),
		Feed:               feed.NewResources(transport),
		Finances:           finances.NewResources(transport),
		Fulfillment:        fulfillment.NewResources(transport),
		Inventory:          inventory.NewResources(transport),
		Marketing:          marketing.NewResources(transport),
		Metadata:           metadata.NewResources(transport),
		Negotiation:        negotiation.NewResources(transport),
		Recommendation:     recommendation.NewResources(transport),
		Stores:             stores.NewResources(transport),
		PostOrder:          postorder.NewResources(transport),
		Feedback:           feedback.NewResources(transport),
		Identity:           identity.NewResources(transport),
		Media:              media.NewResources(transport),
		Message:            message.NewResources(transport),
		Notification:       notification.NewResources(transport),
		Taxonomy:           taxonomy.NewResources(transport),
		DeveloperAnalytics: developeranalytics.NewResources(transport),
		KeyManagement:      keymanagement.NewResources(transport),
		OAuth:              oauth,
	}, nil
}
