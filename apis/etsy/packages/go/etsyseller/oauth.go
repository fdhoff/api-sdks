package etsyseller

import (
	"context"
	"crypto/rand"
	"crypto/sha256"
	"encoding/base64"
	"errors"
	"fmt"
	"log/slog"
	"net/http"
	"net/url"
	"regexp"
	"slices"
	"strconv"
	"strings"
	"sync"

	"github.com/fdhoff/api-sdks/apis/etsy/packages/go/internal/runtime"
)

// AuthorizationEndpoint is where a user grants your app access.
const AuthorizationEndpoint = "https://www.etsy.com/oauth/connect"

// remembered is how many earlier tokens and codes stay redacted besides the current tokens.
const remembered = 16

var verifierPattern = regexp.MustCompile(`^[A-Za-z0-9\-._~]{43,128}$`)

// The token endpoint takes no credentials beyond the form, so a 401 from it never triggers a refresh.
var tokenOperation = &runtime.Operation{
	ID:          "oauthToken",
	Method:      http.MethodPost,
	Path:        "/v3/public/oauth/token",
	Resource:    "OAuth",
	Name:        "Token",
	ReturnsJSON: true,
}

type tokenForm struct {
	GrantType    string `urlencoded:"grant_type"`
	ClientID     string `urlencoded:"client_id"`
	RedirectURI  string `urlencoded:"redirect_uri"`
	Code         string `urlencoded:"code"`
	CodeVerifier string `urlencoded:"code_verifier"`
	RefreshToken string `urlencoded:"refresh_token"`
}

// Token is an access token and the refresh token that replaces it. Etsy prefixes both with the
// user's ID. Printing or logging a Token shows neither.
type Token struct {
	AccessToken  string
	RefreshToken string
	// ExpiresIn is the access token's lifetime in seconds, or 0 when the response did not say.
	ExpiresIn int64
	TokenType string
}

// UserID is the numeric prefix of the access token, and false when it has none.
func (t Token) UserID() (int64, bool) {
	prefix, _, found := strings.Cut(t.AccessToken, ".")
	id, err := strconv.ParseInt(prefix, 10, 64)
	return id, found && err == nil
}

// String hides both tokens.
func (t Token) String() string { return "Token{***}" }

// GoString hides both tokens.
func (t Token) GoString() string { return t.String() }

// LogValue hides both tokens.
func (t Token) LogValue() slog.Value { return slog.StringValue(t.String()) }

// AuthorizationParams configures an authorization request. State and CodeVerifier are generated
// when empty.
type AuthorizationParams struct {
	RedirectURI  string
	Scopes       []string
	State        string
	CodeVerifier string
}

// AuthorizationRequest is where to send the user. Keep State and CodeVerifier until Etsy redirects
// back, check that the redirect's state matches, then pass its code and this CodeVerifier to
// [OAuth.ExchangeCode].
type AuthorizationRequest struct {
	URL          string
	State        string
	CodeVerifier string
}

// String hides the code verifier.
func (r AuthorizationRequest) String() string {
	return fmt.Sprintf("AuthorizationRequest{URL: %s, State: %s}", r.URL, r.State)
}

// GoString hides the code verifier.
func (r AuthorizationRequest) GoString() string { return r.String() }

// LogValue hides the code verifier.
func (r AuthorizationRequest) LogValue() slog.Value { return slog.StringValue(r.String()) }

// CodeChallenge is the S256 challenge for a PKCE code verifier.
func CodeChallenge(codeVerifier string) string {
	digest := sha256.Sum256([]byte(codeVerifier))
	return base64.RawURLEncoding.EncodeToString(digest[:])
}

func randomText(size int) (string, error) {
	data := make([]byte, size)
	if _, err := rand.Read(data); err != nil {
		return "", err
	}
	return base64.RawURLEncoding.EncodeToString(data), nil
}

// NewAuthorizationRequest builds the URL that asks a user to grant the app with this keystring the
// given scopes, with PKCE S256.
func NewAuthorizationRequest(apiKey string, params AuthorizationParams) (*AuthorizationRequest, error) {
	if len(params.Scopes) == 0 {
		return nil, errors.New("request at least one scope")
	}
	verifier, state := params.CodeVerifier, params.State
	var err error
	if verifier == "" {
		if verifier, err = randomText(64); err != nil {
			return nil, err
		}
	}
	if !verifierPattern.MatchString(verifier) {
		return nil, errors.New("the code verifier must be 43 to 128 unreserved characters")
	}
	if state == "" {
		if state, err = randomText(32); err != nil {
			return nil, err
		}
	}
	query := url.Values{
		"response_type":         {"code"},
		"client_id":             {apiKey},
		"redirect_uri":          {params.RedirectURI},
		"scope":                 {strings.Join(params.Scopes, " ")},
		"state":                 {state},
		"code_challenge":        {CodeChallenge(verifier)},
		"code_challenge_method": {"S256"},
	}
	return &AuthorizationRequest{URL: AuthorizationEndpoint + "?" + query.Encode(), State: state, CodeVerifier: verifier}, nil
}

func needs(operation *runtime.Operation, scheme string) bool {
	return operation != nil && slices.ContainsFunc(operation.Security, func(requirement runtime.Requirement) bool {
		return slices.ContainsFunc(requirement, func(part runtime.Scheme) bool { return part.Name == scheme })
	})
}

// credentials sends x-api-key on every operation that names it and the access token on those that
// need OAuth. After a 401 on one of those, it refreshes the access token once, when it has a
// refresh token and the call sent the current access token.
type credentials struct {
	apiKey       string
	sharedSecret string
	onToken      func(Token)
	oauth        *OAuth

	lock         sync.Mutex
	accessToken  string
	refreshToken string
	token        *Token
	seen         []string
}

func newCredentials(apiKey, sharedSecret, accessToken, refreshToken string, onToken func(Token)) *credentials {
	c := &credentials{apiKey: apiKey, sharedSecret: sharedSecret, onToken: onToken, accessToken: accessToken, refreshToken: refreshToken}
	c.remember(accessToken, refreshToken)
	return c
}

func (c *credentials) Apply(_ context.Context, request *runtime.AuthRequest) error {
	if needs(request.Operation, "api_key") {
		request.Header.Set("x-api-key", c.apiKey+":"+c.sharedSecret)
	}
	c.lock.Lock()
	access := c.accessToken
	c.lock.Unlock()
	if access != "" && needs(request.Operation, "oauth2") {
		request.Header.Set("Authorization", "Bearer "+access)
	}
	return nil
}

func (c *credentials) Secrets() []string {
	c.lock.Lock()
	defer c.lock.Unlock()
	secrets := []string{c.apiKey, c.sharedSecret}
	for _, current := range []string{c.accessToken, c.refreshToken} {
		if current != "" {
			secrets = append(secrets, current)
		}
	}
	return append(secrets, c.seen...)
}

// remember keeps values out of logs and errors from now on, such as a code about to be exchanged.
// Only the most recent values are kept, so a long-lived client does not grow.
func (c *credentials) remember(values ...string) {
	c.lock.Lock()
	defer c.lock.Unlock()
	for _, value := range values {
		if value != "" {
			c.seen = append(c.seen, value)
		}
	}
	if extra := len(c.seen) - remembered; extra > 0 {
		c.seen = slices.Delete(c.seen, 0, extra)
	}
}

func (c *credentials) store(token Token) Token {
	c.remember(token.AccessToken, token.RefreshToken)
	c.lock.Lock()
	c.accessToken, c.refreshToken, c.token = token.AccessToken, token.RefreshToken, &token
	c.lock.Unlock()
	if c.onToken != nil {
		c.onToken(token)
	}
	return token
}

func (c *credentials) currentRefreshToken() string {
	c.lock.Lock()
	defer c.lock.Unlock()
	return c.refreshToken
}

// replaced is the token another refresh stored since refreshToken was read, since each refresh
// token works only once.
func (c *credentials) replaced(refreshToken string) (Token, bool) {
	c.lock.Lock()
	defer c.lock.Unlock()
	if c.token == nil || c.refreshToken == refreshToken {
		return Token{}, false
	}
	return *c.token, true
}

func (c *credentials) Refresh(ctx context.Context, request *runtime.AuthRequest) (bool, error) {
	c.lock.Lock()
	access, refreshToken := c.accessToken, c.refreshToken
	c.lock.Unlock()
	if refreshToken == "" || !needs(request.Operation, "oauth2") {
		return false, nil
	}
	sent := ""
	if access != "" {
		sent = "Bearer " + access
	}
	if request.Header.Get("Authorization") != sent {
		return true, nil
	}
	if _, err := c.oauth.Refresh(ctx); err != nil {
		return false, err
	}
	return true, nil
}

// OAuth runs the OAuth 2 authorization code flow with PKCE, as Etsy implements it. A token it
// obtains is used for the client's later calls, and passed to the function set by [WithOnToken].
type OAuth struct {
	credentials *credentials
	transport   *runtime.Transport
	busy        chan struct{}
}

// AuthorizationRequest builds the URL that asks a user to grant your app the given scopes.
func (o *OAuth) AuthorizationRequest(params AuthorizationParams) (*AuthorizationRequest, error) {
	return NewAuthorizationRequest(o.credentials.apiKey, params)
}

// ExchangeCode trades the code from Etsy's redirect for a token. redirectURI must match the
// authorization request's.
func (o *OAuth) ExchangeCode(ctx context.Context, code, codeVerifier, redirectURI string) (Token, error) {
	o.credentials.remember(code, codeVerifier)
	if err := o.acquire(ctx); err != nil {
		return Token{}, err
	}
	defer o.release()
	return o.request(ctx, tokenForm{
		GrantType:    "authorization_code",
		ClientID:     o.credentials.apiKey,
		RedirectURI:  redirectURI,
		Code:         code,
		CodeVerifier: codeVerifier,
	})
}

// Refresh replaces the access token now. The client also does this itself after a 401. A refresh
// asked for while another is under way waits for it and returns its token.
func (o *OAuth) Refresh(ctx context.Context) (Token, error) {
	refreshToken := o.credentials.currentRefreshToken()
	if refreshToken == "" {
		return Token{}, errors.New("there is no refresh token: pass WithRefreshToken, or exchange a code first")
	}
	if err := o.acquire(ctx); err != nil {
		return Token{}, err
	}
	defer o.release()
	if token, ok := o.credentials.replaced(refreshToken); ok {
		return token, nil
	}
	return o.request(ctx, tokenForm{GrantType: "refresh_token", ClientID: o.credentials.apiKey, RefreshToken: refreshToken})
}

// acquire lets one token request run at a time. A caller can stop waiting for its turn.
func (o *OAuth) acquire(ctx context.Context) error {
	select {
	case o.busy <- struct{}{}:
		return nil
	case <-ctx.Done():
		return ctx.Err()
	}
}

func (o *OAuth) release() { <-o.busy }

// request is not cancelled with ctx once sent, so a token pair Etsy has already rotated is still
// stored. The timeout bounds it.
func (o *OAuth) request(ctx context.Context, form tokenForm) (Token, error) {
	reply, err := runtime.Call[map[string]any](context.WithoutCancel(ctx), o.transport, tokenOperation, runtime.Input{Params: &form})
	if err != nil {
		return Token{}, err
	}
	access, _ := reply["access_token"].(string)
	refresh, _ := reply["refresh_token"].(string)
	if access == "" || refresh == "" {
		return Token{}, &APIError{Kind: KindDecode, Message: "the token response has no access and refresh token"}
	}
	token := Token{AccessToken: access, RefreshToken: refresh, TokenType: "Bearer"}
	if expires, ok := reply["expires_in"].(float64); ok && expires == float64(int64(expires)) {
		token.ExpiresIn = int64(expires)
	}
	if kind, ok := reply["token_type"].(string); ok {
		token.TokenType = kind
	}
	return o.credentials.store(token), nil
}
