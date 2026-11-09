package ebaysell

import (
	"context"
	"crypto/rand"
	"encoding/base64"
	"errors"
	"fmt"
	"log/slog"
	"maps"
	"net/http"
	"net/url"
	"slices"
	"strings"
	"sync"
	"time"

	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/internal/runtime"
)

// APIScope is the scope of an application token, which the public operations accept.
const APIScope = "https://api.ebay.com/oauth/api_scope"

// The scopes eBay's client credentials grant gives. An operation that accepts any of them takes an
// application token, and every other operation a user token.
var appScopes = map[string]bool{APIScope: true, APIScope + "/metadata.insights": true}

var authorizationURLs = map[string]string{
	Production: "https://auth.ebay.com/oauth2/authorize",
	Sandbox:    "https://auth.sandbox.ebay.com/oauth2/authorize",
}

// An application token this close to expiry is replaced before use.
const expiryMargin = 60 * time.Second

// remembered is how many earlier tokens and codes stay redacted besides the current ones.
const remembered = 16

// The token endpoint authenticates with the keyset alone, so a 401 from it never triggers a refresh.
var tokenOperation = &runtime.Operation{
	ID:          "oauthToken",
	Method:      http.MethodPost,
	Path:        "/identity/v1/oauth2/token",
	Resource:    "OAuth",
	Name:        "Token",
	ReturnsJSON: true,
	Host:        "api",
}

type tokenForm struct {
	GrantType    string `urlencoded:"grant_type"`
	Code         string `urlencoded:"code"`
	RedirectURI  string `urlencoded:"redirect_uri"`
	RefreshToken string `urlencoded:"refresh_token"`
	Scope        string `urlencoded:"scope"`
}

func unknownEnvironment(environment string) error {
	names := slices.Sorted(maps.Keys(authorizationURLs))
	return fmt.Errorf("unknown environment %q; expected one of: %s", environment, strings.Join(names, ", "))
}

// Token is an access token and, for a user token, the refresh token that replaces it. eBay's refresh
// returns a new access token only, so the refresh token carries over. Printing or logging a Token
// shows neither token.
type Token struct {
	AccessToken string
	// ExpiresIn is the access token's lifetime in seconds, or 0 when the response did not say.
	ExpiresIn    int64
	RefreshToken string
	// RefreshTokenExpiresIn is the refresh token's lifetime in seconds, or 0 when the response did
	// not say.
	RefreshTokenExpiresIn int64
	TokenType             string
}

// String hides both tokens.
func (t Token) String() string { return "Token{***}" }

// GoString hides both tokens.
func (t Token) GoString() string { return t.String() }

// LogValue hides both tokens.
func (t Token) LogValue() slog.Value { return slog.StringValue(t.String()) }

// AuthorizationParams configures an authorization request. State is generated when empty. Set Prompt
// to "login" to make the user sign in even if they already are.
type AuthorizationParams struct {
	Scopes []string
	State  string
	Prompt string
}

// AuthorizationRequest is where to send the user. Keep State until eBay redirects to your RuName's
// accept URL, check that the redirect's state matches, then pass its code to [OAuth.ExchangeCode].
type AuthorizationRequest struct {
	URL   string
	State string
}

func randomText(size int) (string, error) {
	data := make([]byte, size)
	if _, err := rand.Read(data); err != nil {
		return "", err
	}
	return base64.RawURLEncoding.EncodeToString(data), nil
}

// NewAuthorizationRequest builds the URL that asks a user to grant the app with this client ID the
// given scopes. ruName is your app's redirect URL name, which eBay takes as redirect_uri, and
// environment is [Production] or [Sandbox].
func NewAuthorizationRequest(clientID, ruName, environment string, params AuthorizationParams) (*AuthorizationRequest, error) {
	if len(params.Scopes) == 0 {
		return nil, errors.New("request at least one scope")
	}
	endpoint, found := authorizationURLs[environment]
	if !found {
		return nil, unknownEnvironment(environment)
	}
	state := params.State
	if state == "" {
		var err error
		if state, err = randomText(32); err != nil {
			return nil, err
		}
	}
	query := url.Values{
		"client_id":     {clientID},
		"redirect_uri":  {ruName},
		"response_type": {"code"},
		"scope":         {strings.Join(params.Scopes, " ")},
		"state":         {state},
	}
	if params.Prompt != "" {
		query.Set("prompt", params.Prompt)
	}
	return &AuthorizationRequest{URL: endpoint + "?" + query.Encode(), State: state}, nil
}

// takesAppToken reports whether an operation accepts an application token. eBay lists the scopes an
// operation accepts, any one of which is enough.
func takesAppToken(operation *runtime.Operation) bool {
	for _, requirement := range operation.Security {
		for _, scheme := range requirement {
			if slices.ContainsFunc(scheme.Scopes, func(scope string) bool { return appScopes[scope] }) {
				return true
			}
		}
	}
	return false
}

// credentials sends an application token on operations that accept one and a user token on the
// rest, then signs the request when there is a signing key. It mints an application token when there
// is none or it is about to expire. After a 401 it mints a new application token, or refreshes the
// user token once when there is a refresh token.
type credentials struct {
	clientID     string
	clientSecret string
	basic        string
	onToken      func(Token)
	signer       *runtime.MessageSigner
	signatureKey string
	now          func() time.Time
	oauth        *OAuth

	lock         sync.Mutex
	appToken     string
	appExpiresAt time.Time // Zero when the expiry is not known.
	userToken    string
	refreshToken string
	seen         []string
}

func newCredentials(config options) (*credentials, error) {
	c := &credentials{
		clientID:     config.clientID,
		clientSecret: config.clientSecret,
		onToken:      config.onToken,
		now:          config.now,
		appToken:     config.appToken,
		userToken:    config.userToken,
		refreshToken: config.refreshToken,
	}
	if config.clientID != "" {
		c.basic = base64.StdEncoding.EncodeToString([]byte(config.clientID + ":" + config.clientSecret))
	}
	if config.signingKey != nil {
		signer, err := config.signingKey.signer()
		if err != nil {
			return nil, err
		}
		c.signer, c.signatureKey = signer, config.signingKey.JWE
	}
	return c, nil
}

func (c *credentials) canMint() bool { return c.basic != "" }

// freshAppToken is the application token, unless it is about to expire. A token passed in has no
// known expiry.
func (c *credentials) freshAppToken() string {
	c.lock.Lock()
	defer c.lock.Unlock()
	if c.appToken != "" && (c.appExpiresAt.IsZero() || c.now().Before(c.appExpiresAt.Add(-expiryMargin))) {
		return c.appToken
	}
	return ""
}

func (c *credentials) current() (app, user, refresh string) {
	c.lock.Lock()
	defer c.lock.Unlock()
	return c.appToken, c.userToken, c.refreshToken
}

func (c *credentials) token(ctx context.Context, operation *runtime.Operation) (string, error) {
	_, user, _ := c.current()
	if !takesAppToken(operation) {
		if user == "" {
			return "", fmt.Errorf("%s needs a user token: pass WithUserToken, or call OAuth.ExchangeCode first", operation.Key())
		}
		return user, nil
	}
	token := c.freshAppToken()
	if token == "" && c.canMint() {
		minted, err := c.oauth.AppToken(ctx)
		if err != nil {
			return "", err
		}
		token = minted.AccessToken
	}
	if token == "" {
		token = user
	}
	if token == "" {
		return "", fmt.Errorf("%s needs an application token: pass WithClientCredentials, or WithAppToken", operation.Key())
	}
	return token, nil
}

func (c *credentials) Apply(ctx context.Context, request *runtime.AuthRequest) error {
	if request.Operation == tokenOperation {
		if !c.canMint() {
			return errors.New("a token request needs WithClientCredentials")
		}
		request.Header.Set("Authorization", "Basic "+c.basic)
		return nil
	}
	token, err := c.token(ctx, request.Operation)
	if err != nil {
		return err
	}
	request.Header.Set("Authorization", "Bearer "+token)
	if c.signer == nil {
		return nil
	}
	request.Header.Set("x-ebay-signature-key", c.signatureKey)
	return c.signer.Sign(request)
}

func (c *credentials) Secrets() []string {
	c.lock.Lock()
	defer c.lock.Unlock()
	var secrets []string
	for _, value := range []string{c.clientSecret, c.basic, c.appToken, c.userToken, c.refreshToken} {
		if value != "" {
			secrets = append(secrets, value)
		}
	}
	if c.signer != nil {
		secrets = append(secrets, c.signer.Secrets()...)
	}
	return append(secrets, c.seen...)
}

// remember keeps values out of logs and errors from now on, such as a code about to be exchanged.
// Only the most recent values are kept, so a long-lived client does not grow.
func (c *credentials) remember(values ...string) {
	c.lock.Lock()
	defer c.lock.Unlock()
	c.rememberLocked(values...)
}

func (c *credentials) rememberLocked(values ...string) {
	for _, value := range values {
		if value != "" {
			c.seen = append(c.seen, value)
		}
	}
	if extra := len(c.seen) - remembered; extra > 0 {
		c.seen = slices.Delete(c.seen, 0, extra)
	}
}

func (c *credentials) storeApp(token Token) Token {
	c.lock.Lock()
	defer c.lock.Unlock()
	c.rememberLocked(c.appToken)
	c.appToken = token.AccessToken
	c.appExpiresAt = time.Time{}
	if token.ExpiresIn > 0 {
		c.appExpiresAt = c.now().Add(time.Duration(token.ExpiresIn) * time.Second)
	}
	return token
}

// storeUser keeps the refresh token when the response has none, as eBay's refresh does not return one.
func (c *credentials) storeUser(token Token) Token {
	c.lock.Lock()
	if token.RefreshToken == "" {
		token.RefreshToken = c.refreshToken
	}
	c.rememberLocked(c.userToken, c.refreshToken)
	c.userToken, c.refreshToken = token.AccessToken, token.RefreshToken
	c.lock.Unlock()
	if c.onToken != nil {
		c.onToken(token)
	}
	return token
}

// expireApp makes the next call mint a new application token, unless another one replaced token.
func (c *credentials) expireApp(token string) {
	c.lock.Lock()
	defer c.lock.Unlock()
	if c.appToken == token {
		c.appExpiresAt = time.Unix(0, 0)
	}
}

func (c *credentials) Refresh(ctx context.Context, request *runtime.AuthRequest) (bool, error) {
	app, user, refresh := c.current()
	sent := strings.TrimPrefix(request.Header.Get("Authorization"), "Bearer ")
	if takesAppToken(request.Operation) && (c.canMint() || app != "") {
		if !c.canMint() {
			return false, nil
		}
		c.expireApp(sent)
		if _, err := c.oauth.AppToken(ctx); err != nil {
			return false, err
		}
		return true, nil
	}
	if refresh == "" {
		return false, nil
	}
	if user != sent {
		return true, nil
	}
	if _, err := c.oauth.Refresh(ctx); err != nil {
		return false, err
	}
	return true, nil
}

// OAuth runs OAuth 2 as eBay implements it: application tokens from the client credentials grant,
// and user tokens from the authorization code grant, both from one token endpoint with HTTP Basic
// client authentication. A user token it obtains is used for the client's later calls, and passed to
// the function set by [WithOnToken].
type OAuth struct {
	credentials *credentials
	transport   *runtime.Transport
	ruName      string
	appScopes   []string
	userScopes  []string
	environment string
	minting     chan struct{}
	refreshing  chan struct{}
}

func newOAuth(credentials *credentials, transport *runtime.Transport, config options) *OAuth {
	return &OAuth{
		credentials: credentials,
		transport:   transport,
		ruName:      config.ruName,
		appScopes:   config.appScopes,
		userScopes:  config.userScopes,
		environment: config.environment,
		minting:     make(chan struct{}, 1),
		refreshing:  make(chan struct{}, 1),
	}
}

func (o *OAuth) userGrant() error {
	if !o.credentials.canMint() {
		return errors.New("pass WithClientCredentials to use the authorization code grant")
	}
	if o.ruName == "" {
		return errors.New("pass WithRuName to use the authorization code grant")
	}
	return nil
}

// AuthorizationRequest builds the URL that asks a user to grant your app the given scopes, in the
// client's environment.
func (o *OAuth) AuthorizationRequest(params AuthorizationParams) (*AuthorizationRequest, error) {
	if err := o.userGrant(); err != nil {
		return nil, err
	}
	return NewAuthorizationRequest(o.credentials.clientID, o.ruName, o.environment, params)
}

// ExchangeCode trades the code from eBay's redirect for a user token and its refresh token.
func (o *OAuth) ExchangeCode(ctx context.Context, code string) (Token, error) {
	o.credentials.remember(code)
	if err := o.userGrant(); err != nil {
		return Token{}, err
	}
	token, err := o.request(ctx, tokenForm{GrantType: "authorization_code", Code: code, RedirectURI: o.ruName})
	if err != nil {
		return Token{}, err
	}
	return o.credentials.storeUser(token), nil
}

// Refresh replaces the user token now. The client also does this itself after a 401. scopes must be
// the original grant's or fewer, and default to those set by [WithUserScopes]. A refresh asked for
// while another is under way waits for it and returns its token.
func (o *OAuth) Refresh(ctx context.Context, scopes ...string) (Token, error) {
	_, before, refresh := o.credentials.current()
	if refresh == "" {
		return Token{}, errors.New("there is no refresh token: pass WithRefreshToken, or exchange a code first")
	}
	if err := acquire(ctx, o.refreshing); err != nil {
		return Token{}, err
	}
	defer func() { <-o.refreshing }()
	if _, user, refresh := o.credentials.current(); user != "" && user != before {
		return Token{AccessToken: user, RefreshToken: refresh, TokenType: "Bearer"}, nil
	}
	if len(scopes) == 0 {
		scopes = o.userScopes
	}
	token, err := o.request(ctx, tokenForm{GrantType: "refresh_token", RefreshToken: refresh, Scope: strings.Join(scopes, " ")})
	if err != nil {
		return Token{}, err
	}
	return o.credentials.storeUser(token), nil
}

// AppToken returns an application token with the scopes set by [WithAppScopes], minting one unless
// the current one is still fresh.
func (o *OAuth) AppToken(ctx context.Context) (Token, error) {
	if err := acquire(ctx, o.minting); err != nil {
		return Token{}, err
	}
	defer func() { <-o.minting }()
	if current := o.credentials.freshAppToken(); current != "" {
		return Token{AccessToken: current, TokenType: "Bearer"}, nil
	}
	token, err := o.request(ctx, tokenForm{GrantType: "client_credentials", Scope: strings.Join(o.appScopes, " ")})
	if err != nil {
		return Token{}, err
	}
	return o.credentials.storeApp(token), nil
}

// acquire lets one token request of a kind run at a time. A caller can stop waiting for its turn.
func acquire(ctx context.Context, busy chan struct{}) error {
	select {
	case busy <- struct{}{}:
		return nil
	case <-ctx.Done():
		return ctx.Err()
	}
}

func seconds(value any) int64 {
	if number, ok := value.(float64); ok && number > 0 && number == float64(int64(number)) {
		return int64(number)
	}
	return 0
}

// request is not cancelled with ctx once sent, so a token eBay has already issued is still stored.
// The timeout bounds it.
func (o *OAuth) request(ctx context.Context, form tokenForm) (Token, error) {
	reply, err := runtime.Call[map[string]any](context.WithoutCancel(ctx), o.transport, tokenOperation, runtime.Input{Params: &form})
	if err != nil {
		return Token{}, err
	}
	access, _ := reply["access_token"].(string)
	if access == "" {
		return Token{}, &APIError{Kind: KindDecode, Message: "the token response has no access token"}
	}
	token := Token{AccessToken: access, TokenType: "Bearer", ExpiresIn: seconds(reply["expires_in"]), RefreshTokenExpiresIn: seconds(reply["refresh_token_expires_in"])}
	token.RefreshToken, _ = reply["refresh_token"].(string)
	if kind, ok := reply["token_type"].(string); ok && kind != "" {
		token.TokenType = kind
	}
	return token, nil
}
