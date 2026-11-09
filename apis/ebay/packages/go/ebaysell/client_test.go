package ebaysell_test

import (
	"bytes"
	"context"
	"crypto/ed25519"
	"crypto/rand"
	"crypto/sha256"
	"crypto/x509"
	"encoding/base64"
	"encoding/pem"
	"errors"
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"net/http/httptest"
	"net/url"
	"os"
	"path/filepath"
	"reflect"
	"regexp"
	"slices"
	"strings"
	"sync"
	"sync/atomic"
	"testing"
	"time"

	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/developeranalytics"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/fulfillment"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/inventory"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/postorder"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/ebaysell/taxonomy"
	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/internal/runtime"
)

const (
	clientID     = "synthetic-app-id"
	clientSecret = "synthetic-cert-id"
	appToken     = "synthetic-app-token"
	userToken    = "synthetic-user-token"
	refreshToken = "synthetic-refresh-token"
	newAppToken  = "synthetic-app-token-2"
	newUserToken = "synthetic-user-token-2"
	tokenPath    = "/identity/v1/oauth2/token"
	treePath     = "/commerce/taxonomy/v1/get_default_category_tree_id"
	orderPath    = "/sell/fulfillment/v1/order/01-00000-00001"
)

var basic = "Basic " + base64.StdEncoding.EncodeToString([]byte(clientID+":"+clientSecret))

type sent struct {
	host      string
	authority string
	method    string
	path      string
	query     url.Values
	header    http.Header
	body      string
}

// recorder keeps every request with the host key it was sent to.
type recorder struct {
	lock     sync.Mutex
	requests []sent
}

func (r *recorder) all() []sent {
	r.lock.Lock()
	defer r.lock.Unlock()
	return slices.Clone(r.requests)
}

func (r *recorder) paths() []string {
	paths := []string{}
	for _, request := range r.all() {
		paths = append(paths, request.path)
	}
	return paths
}

func (r *recorder) to(path string) []sent {
	var matching []sent
	for _, request := range r.all() {
		if request.path == path {
			matching = append(matching, request)
		}
	}
	return matching
}

// server serves each host key under its own prefix of one mock, and builds a client for it.
func server(t *testing.T, handle http.HandlerFunc, options ...ebaysell.Option) (*ebaysell.Client, *recorder) {
	t.Helper()
	seen := &recorder{}
	mock := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		host, path, _ := strings.Cut(strings.TrimPrefix(r.URL.Path, "/"), "/")
		r.URL.Path = "/" + path
		body, _ := io.ReadAll(r.Body)
		r.Body = io.NopCloser(bytes.NewReader(body))
		seen.lock.Lock()
		seen.requests = append(seen.requests, sent{host, r.Host, r.Method, r.URL.Path, r.URL.Query(), r.Header.Clone(), string(body)})
		seen.lock.Unlock()
		handle(w, r)
	}))
	t.Cleanup(mock.Close)
	hosts := map[string]string{"api": mock.URL + "/api", "apiz": mock.URL + "/apiz", "apim": mock.URL + "/apim"}
	defaults := []ebaysell.Option{ebaysell.WithHosts(hosts), ebaysell.WithRetryBaseDelay(time.Millisecond), ebaysell.WithRateLimitWait(time.Millisecond)}
	client, err := ebaysell.NewClient(append(defaults, options...)...)
	if err != nil {
		t.Fatal(err)
	}
	return client, seen
}

func replyJSON(w http.ResponseWriter, status int, body string) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	fmt.Fprint(w, body)
}

func token(w http.ResponseWriter, access string, expiresIn int) {
	replyJSON(w, http.StatusOK, fmt.Sprintf(`{"access_token":%q,"expires_in":%d,"token_type":"User Access Token"}`, access, expiresIn))
}

// accepting answers every API call with a small JSON object, and token requests with new tokens.
func accepting(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != tokenPath {
		replyJSON(w, http.StatusOK, `{"categoryTreeId":"0","orderId":"01-00000-00001"}`)
		return
	}
	_ = r.ParseForm()
	if r.PostForm.Get("grant_type") == "client_credentials" {
		token(w, newAppToken, 7200)
		return
	}
	token(w, newUserToken, 7200)
}

func defaultTree(client *ebaysell.Client) error {
	_, err := client.Taxonomy.CategoryTrees.GetDefaultID(context.Background(), &taxonomy.CategoryTreesGetDefaultIDParams{MarketplaceID: ebaysell.Ptr("EBAY_US")})
	return err
}

func order(client *ebaysell.Client) error {
	_, err := client.Fulfillment.Orders.Get(context.Background(), "01-00000-00001", nil)
	return err
}

var operationLine = regexp.MustCompile(`(?m)^(\w+): \{ resource: (\w+), method: (\w+)(?:, iterator: (\w+))?`)

// The client field of each contract, as the conformance driver also names them.
var contractFields = map[string]string{
	"sell_account_v1": "Account", "sell_account_v2": "AccountV2", "sell_analytics": "Analytics", "sell_feed": "Feed",
	"sell_finances": "Finances", "sell_fulfillment": "Fulfillment", "sell_inventory": "Inventory", "sell_marketing": "Marketing",
	"sell_metadata": "Metadata", "sell_negotiation": "Negotiation", "sell_recommendation": "Recommendation", "sell_stores": "Stores",
	"sell_post_order": "PostOrder", "commerce_feedback": "Feedback", "commerce_identity": "Identity", "commerce_media": "Media",
	"commerce_message": "Message", "commerce_notification": "Notification", "commerce_taxonomy": "Taxonomy",
	"developer_analytics": "DeveloperAnalytics", "developer_key_management": "KeyManagement",
}

func TestEveryOperationHasAPublicMethod(t *testing.T) {
	files, err := filepath.Glob("../operations/*.yaml")
	if err != nil || len(files) != len(contractFields) {
		t.Fatalf("found %d operations files: %v", len(files), err)
	}
	client, _ := server(t, accepting, ebaysell.WithUserToken(userToken))
	operations, iterators := 0, 0
	for _, file := range files {
		contract := strings.TrimSuffix(filepath.Base(file), ".yaml")
		names, err := os.ReadFile(file)
		if err != nil {
			t.Fatal(err)
		}
		api := reflect.ValueOf(client).Elem().FieldByName(contractFields[contract])
		if !api.IsValid() {
			t.Fatalf("the client has no field for %s", contract)
		}
		for _, line := range operationLine.FindAllStringSubmatch(string(names), -1) {
			operations++
			operation, found := runtime.Lookup(contract + "." + line[1])
			if !found || operation.Contract != contract || operation.Resource != line[2] || operation.Name != line[3] || operation.Iterator != line[4] {
				t.Errorf("%s.%s is registered as %+v", contract, line[1], operation)
				continue
			}
			resource := api.FieldByName(line[2])
			for _, method := range []string{line[3], line[4]} {
				if method != "" && !resource.MethodByName(method).IsValid() {
					t.Errorf("%s.%s.%s is missing", contract, line[2], method)
				}
			}
			if line[4] != "" {
				iterators++
			}
		}
	}
	if operations != 339 || iterators != 35 {
		t.Errorf("%d operations and %d iterators", operations, iterators)
	}
}

func TestNewClientValidatesItsArguments(t *testing.T) {
	cases := map[string][]ebaysell.Option{
		"no credentials":      nil,
		"id without secret":   {ebaysell.WithClientCredentials(clientID, "")},
		"secret without id":   {ebaysell.WithClientCredentials("", clientSecret)},
		"unknown environment": {ebaysell.WithUserToken(userToken), ebaysell.WithEnvironment("staging")},
		"hosts missing a key": {ebaysell.WithUserToken(userToken), ebaysell.WithHosts(map[string]string{"api": "http://localhost"})},
		"bad signing key":     {ebaysell.WithUserToken(userToken), ebaysell.WithSigningKey(ebaysell.SigningKey{PrivateKey: "not a key", JWE: "jwe"})},
		"no app scopes":       {ebaysell.WithClientCredentials(clientID, clientSecret), ebaysell.WithAppScopes()},
		"blank app scope":     {ebaysell.WithClientCredentials(clientID, clientSecret), ebaysell.WithAppScopes(" ")},
	}
	for name, options := range cases {
		t.Run(name, func(t *testing.T) {
			if _, err := ebaysell.NewClient(options...); err == nil {
				t.Fatal("expected an error")
			}
		})
	}
}

func TestEachOperationGetsTheTokenItsScopesAccept(t *testing.T) {
	client, seen := server(t, accepting, ebaysell.WithAppToken(appToken), ebaysell.WithUserToken(userToken))
	if err := defaultTree(client); err != nil {
		t.Fatal(err)
	}
	if err := order(client); err != nil {
		t.Fatal(err)
	}
	requests := seen.all()
	if got := requests[0].header.Get("Authorization"); got != "Bearer "+appToken {
		t.Errorf("the taxonomy call sent %q", got)
	}
	if got := requests[1].header.Get("Authorization"); got != "Bearer "+userToken {
		t.Errorf("the order call sent %q", got)
	}
}

func TestWithoutAnApplicationTokenTheUserTokenIsSent(t *testing.T) {
	client, seen := server(t, accepting, ebaysell.WithUserToken(userToken))
	if err := defaultTree(client); err != nil {
		t.Fatal(err)
	}
	if got := seen.all()[0].header.Get("Authorization"); got != "Bearer "+userToken {
		t.Errorf("sent %q", got)
	}
}

func TestAMissingTokenFailsBeforeAnythingIsSent(t *testing.T) {
	client, seen := server(t, accepting, ebaysell.WithAppToken(appToken))
	err := order(client)
	if err == nil || !strings.Contains(err.Error(), "sell_fulfillment.getOrder needs a user token") {
		t.Fatalf("error is %v", err)
	}
	if len(seen.all()) != 0 {
		t.Errorf("sent %v", seen.paths())
	}
}

func TestApplicationTokensAreMintedOnceAndReused(t *testing.T) {
	client, seen := server(t, accepting, ebaysell.WithClientCredentials(clientID, clientSecret))
	for range 2 {
		if err := defaultTree(client); err != nil {
			t.Fatal(err)
		}
	}
	if want := []string{tokenPath, treePath, treePath}; !reflect.DeepEqual(seen.paths(), want) {
		t.Fatalf("paths are %v", seen.paths())
	}
	mint := seen.all()[0]
	form, _ := url.ParseQuery(mint.body)
	if mint.host != "api" || mint.header.Get("Authorization") != basic || form.Get("grant_type") != "client_credentials" || form.Get("scope") != ebaysell.APIScope {
		t.Errorf("the token request is %+v", mint)
	}
	if got := seen.all()[2].header.Get("Authorization"); got != "Bearer "+newAppToken {
		t.Errorf("sent %q", got)
	}
}

func TestAnApplicationTokenAboutToExpireIsReplaced(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == tokenPath {
			token(w, newAppToken, 30)
			return
		}
		accepting(w, r)
	}, ebaysell.WithClientCredentials(clientID, clientSecret), ebaysell.WithAppScopes(ebaysell.APIScope, ebaysell.APIScope+"/metadata.insights"))
	for range 2 {
		if err := defaultTree(client); err != nil {
			t.Fatal(err)
		}
	}
	if want := []string{tokenPath, treePath, tokenPath, treePath}; !reflect.DeepEqual(seen.paths(), want) {
		t.Fatalf("paths are %v", seen.paths())
	}
	form, _ := url.ParseQuery(seen.all()[0].body)
	if want := ebaysell.APIScope + " " + ebaysell.APIScope + "/metadata.insights"; form.Get("scope") != want {
		t.Errorf("scope is %q", form.Get("scope"))
	}
}

func TestA401OnAnApplicationOperationMintsANewToken(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path != tokenPath && r.Header.Get("Authorization") != "Bearer "+newAppToken {
			replyJSON(w, http.StatusUnauthorized, `{"errors":[{"errorId":1001,"message":"Invalid access token"}]}`)
			return
		}
		accepting(w, r)
	}, ebaysell.WithClientCredentials(clientID, clientSecret), ebaysell.WithAppToken(appToken))
	if err := defaultTree(client); err != nil {
		t.Fatal(err)
	}
	if want := []string{treePath, tokenPath, treePath}; !reflect.DeepEqual(seen.paths(), want) {
		t.Errorf("paths are %v", seen.paths())
	}
}

func TestA401WithAnApplicationTokenThatCannotBeMintedIsReturned(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		replyJSON(w, http.StatusUnauthorized, `{}`)
	}, ebaysell.WithAppToken(appToken), ebaysell.WithUserToken(userToken), ebaysell.WithRefreshToken(refreshToken))
	if err := defaultTree(client); !errors.Is(err, ebaysell.ErrAuthentication) {
		t.Fatalf("error is %v", err)
	}
	if len(seen.all()) != 1 {
		t.Errorf("paths are %v", seen.paths())
	}
}

// expiring answers 401 until the user token is the refreshed one.
func expiring(w http.ResponseWriter, r *http.Request) {
	if r.URL.Path != tokenPath && r.Header.Get("Authorization") != "Bearer "+newUserToken {
		replyJSON(w, http.StatusUnauthorized, `{"errors":[{"errorId":1001,"message":"Invalid access token"}]}`)
		return
	}
	accepting(w, r)
}

func TestA401RefreshesTheUserTokenAndKeepsTheRefreshToken(t *testing.T) {
	var stored []ebaysell.Token
	client, seen := server(t, expiring,
		ebaysell.WithClientCredentials(clientID, clientSecret), ebaysell.WithUserToken(userToken), ebaysell.WithRefreshToken(refreshToken),
		ebaysell.WithUserScopes("https://api.ebay.com/oauth/api_scope/sell.fulfillment"),
		ebaysell.WithOnToken(func(token ebaysell.Token) { stored = append(stored, token) }))
	if err := order(client); err != nil {
		t.Fatal(err)
	}
	if want := []string{orderPath, tokenPath, orderPath}; !reflect.DeepEqual(seen.paths(), want) {
		t.Fatalf("paths are %v", seen.paths())
	}
	refresh := seen.all()[1]
	form, _ := url.ParseQuery(refresh.body)
	if refresh.header.Get("Authorization") != basic || form.Get("grant_type") != "refresh_token" || form.Get("refresh_token") != refreshToken ||
		form.Get("scope") != "https://api.ebay.com/oauth/api_scope/sell.fulfillment" {
		t.Errorf("the refresh request is %+v", refresh)
	}
	if len(stored) != 1 || stored[0].AccessToken != newUserToken || stored[0].RefreshToken != refreshToken || stored[0].ExpiresIn != 7200 || stored[0].TokenType != "User Access Token" {
		t.Errorf("stored %#v", stored)
	}
}

func TestConcurrent401sShareOneRefresh(t *testing.T) {
	var refreshes atomic.Int32
	client, _ := server(t, func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == tokenPath {
			refreshes.Add(1)
			time.Sleep(20 * time.Millisecond)
		}
		expiring(w, r)
	}, ebaysell.WithClientCredentials(clientID, clientSecret), ebaysell.WithUserToken(userToken), ebaysell.WithRefreshToken(refreshToken))
	var group sync.WaitGroup
	failures := make(chan error, 8)
	for range 8 {
		group.Add(1)
		go func() {
			defer group.Done()
			failures <- order(client)
		}()
	}
	group.Wait()
	close(failures)
	for err := range failures {
		if err != nil {
			t.Error(err)
		}
	}
	if refreshes.Load() != 1 {
		t.Errorf("refreshed %d times", refreshes.Load())
	}
}

// atOnce runs each call in its own goroutine and returns their errors.
func atOnce(calls ...func() error) []error {
	var group sync.WaitGroup
	failures := make([]error, len(calls))
	for index, call := range calls {
		group.Add(1)
		go func() {
			defer group.Done()
			failures[index] = call()
		}()
	}
	group.Wait()
	return failures
}

func grants(seen *recorder) []string {
	var found []string
	for _, request := range seen.to(tokenPath) {
		form, _ := url.ParseQuery(request.body)
		found = append(found, form.Get("grant_type"))
	}
	slices.Sort(found)
	return found
}

func TestConcurrentFirstCallsShareOneApplicationToken(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == tokenPath {
			time.Sleep(20 * time.Millisecond)
		}
		accepting(w, r)
	}, ebaysell.WithClientCredentials(clientID, clientSecret))
	call := func() error { return defaultTree(client) }
	for _, err := range atOnce(call, call, call, call) {
		if err != nil {
			t.Error(err)
		}
	}
	if got := grants(seen); !reflect.DeepEqual(got, []string{"client_credentials"}) {
		t.Errorf("token requests are %v", got)
	}
}

func TestAnApplication401AndAUser401AtOnceEachRefreshTheirOwnToken(t *testing.T) {
	// Each first refusal waits for the other, so that both calls fail before either refreshes.
	var refusals atomic.Int32
	var held sync.WaitGroup
	held.Add(2)
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		bearer := strings.TrimPrefix(r.Header.Get("Authorization"), "Bearer ")
		if r.URL.Path != tokenPath && bearer != newAppToken && bearer != newUserToken {
			if refusals.Add(1) <= 2 {
				held.Done()
				held.Wait()
			}
			replyJSON(w, http.StatusUnauthorized, `{"errors":[{"errorId":1001,"message":"Invalid access token"}]}`)
			return
		}
		accepting(w, r)
	}, ebaysell.WithClientCredentials(clientID, clientSecret), ebaysell.WithAppToken(appToken),
		ebaysell.WithUserToken(userToken), ebaysell.WithRefreshToken(refreshToken))
	for _, err := range atOnce(func() error { return defaultTree(client) }, func() error { return order(client) }) {
		if err != nil {
			t.Error(err)
		}
	}
	if got := grants(seen); !reflect.DeepEqual(got, []string{"client_credentials", "refresh_token"}) {
		t.Errorf("token requests are %v", got)
	}
}

func TestWithoutARefreshTokenA401IsReturned(t *testing.T) {
	client, seen := server(t, expiring, ebaysell.WithClientCredentials(clientID, clientSecret), ebaysell.WithUserToken(userToken))
	err := order(client)
	var failure *ebaysell.APIError
	if !errors.As(err, &failure) || failure.Kind != ebaysell.KindAuthentication || failure.Code != "1001" || failure.Detail != "Invalid access token" {
		t.Fatalf("error is %v", err)
	}
	if len(seen.all()) != 1 {
		t.Errorf("paths are %v", seen.paths())
	}
}

func TestAFailedRefreshReturnsItsErrorWithoutTheRefreshToken(t *testing.T) {
	client, _ := server(t, func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == tokenPath {
			replyJSON(w, http.StatusBadRequest, fmt.Sprintf(`{"error":"invalid_grant","error_description":"bad %s"}`, refreshToken))
			return
		}
		expiring(w, r)
	}, ebaysell.WithClientCredentials(clientID, clientSecret), ebaysell.WithUserToken(userToken), ebaysell.WithRefreshToken(refreshToken))
	err := order(client)
	var failure *ebaysell.APIError
	if !errors.As(err, &failure) || failure.Kind != ebaysell.KindBadRequest {
		t.Fatalf("error is %v", err)
	}
	if strings.Contains(failure.RawBody, refreshToken) || strings.Contains(err.Error(), refreshToken) {
		t.Errorf("the error shows the refresh token: %q", failure.RawBody)
	}
}

func TestATokenResponseWithoutAnAccessTokenIsADecodeError(t *testing.T) {
	client, _ := server(t, func(w http.ResponseWriter, r *http.Request) {
		replyJSON(w, http.StatusOK, `{"expires_in":7200}`)
	}, ebaysell.WithClientCredentials(clientID, clientSecret))
	if _, err := client.OAuth.AppToken(context.Background()); !errors.Is(err, ebaysell.ErrDecode) {
		t.Fatalf("error is %v", err)
	}
}

func TestExchangeCodeStoresTheUserTokenForLaterCalls(t *testing.T) {
	const code = "synthetic-authorization-code"
	var stored []ebaysell.Token
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == tokenPath {
			replyJSON(w, http.StatusOK, fmt.Sprintf(`{"access_token":%q,"expires_in":7200,"refresh_token":%q,"refresh_token_expires_in":47304000}`, newUserToken, refreshToken))
			return
		}
		accepting(w, r)
	}, ebaysell.WithClientCredentials(clientID, clientSecret), ebaysell.WithRuName("synthetic-ru-name"),
		ebaysell.WithOnToken(func(token ebaysell.Token) { stored = append(stored, token) }))
	exchanged, err := client.OAuth.ExchangeCode(context.Background(), code)
	if err != nil {
		t.Fatal(err)
	}
	if exchanged.RefreshToken != refreshToken || exchanged.RefreshTokenExpiresIn != 47304000 || len(stored) != 1 {
		t.Errorf("exchanged %#v, stored %d", exchanged, len(stored))
	}
	form, _ := url.ParseQuery(seen.all()[0].body)
	if form.Get("grant_type") != "authorization_code" || form.Get("code") != code || form.Get("redirect_uri") != "synthetic-ru-name" {
		t.Errorf("the exchange form is %v", form)
	}
	if err := order(client); err != nil {
		t.Fatal(err)
	}
	if got := seen.all()[1].header.Get("Authorization"); got != "Bearer "+newUserToken {
		t.Errorf("sent %q", got)
	}
}

func TestTheAuthorizationCodeGrantNeedsTheKeysetAndRuName(t *testing.T) {
	client, _ := server(t, accepting, ebaysell.WithClientCredentials(clientID, clientSecret))
	if _, err := client.OAuth.ExchangeCode(context.Background(), "code"); err == nil || !strings.Contains(err.Error(), "WithRuName") {
		t.Errorf("error is %v", err)
	}
	userOnly, _ := server(t, accepting, ebaysell.WithUserToken(userToken), ebaysell.WithRuName("synthetic-ru-name"))
	if _, err := userOnly.OAuth.AuthorizationRequest(ebaysell.AuthorizationParams{Scopes: []string{ebaysell.APIScope}}); err == nil {
		t.Error("expected an error without the keyset")
	}
	if _, err := userOnly.OAuth.Refresh(context.Background()); err == nil {
		t.Error("expected an error without a refresh token")
	}
}

func TestAuthorizationRequestNamesTheRuNameScopesAndState(t *testing.T) {
	client, _ := server(t, accepting, ebaysell.WithClientCredentials(clientID, clientSecret), ebaysell.WithRuName("synthetic-ru-name"), ebaysell.WithEnvironment(ebaysell.Sandbox))
	request, err := client.OAuth.AuthorizationRequest(ebaysell.AuthorizationParams{Scopes: []string{"scope-a", "scope-b"}, Prompt: "login"})
	if err != nil {
		t.Fatal(err)
	}
	parsed, _ := url.Parse(request.URL)
	query := parsed.Query()
	if parsed.Host != "auth.sandbox.ebay.com" || query.Get("client_id") != clientID || query.Get("redirect_uri") != "synthetic-ru-name" ||
		query.Get("response_type") != "code" || query.Get("scope") != "scope-a scope-b" || query.Get("prompt") != "login" ||
		query.Get("state") != request.State || len(request.State) < 40 {
		t.Errorf("the request is %+v", request)
	}
	kept, err := ebaysell.NewAuthorizationRequest(clientID, "ru", ebaysell.Production, ebaysell.AuthorizationParams{Scopes: []string{"s"}, State: "kept"})
	if err != nil || kept.State != "kept" || !strings.HasPrefix(kept.URL, "https://auth.ebay.com/oauth2/authorize?") || strings.Contains(kept.URL, "prompt") {
		t.Errorf("the request is %+v, %v", kept, err)
	}
	for _, params := range []ebaysell.AuthorizationParams{{}, {Scopes: []string{}}} {
		if _, err := ebaysell.NewAuthorizationRequest(clientID, "ru", ebaysell.Production, params); err == nil {
			t.Error("expected an error without scopes")
		}
	}
	if _, err := ebaysell.NewAuthorizationRequest(clientID, "ru", "staging", ebaysell.AuthorizationParams{Scopes: []string{"s"}}); err == nil {
		t.Error("expected an error for an unknown environment")
	}
}

type roundTripper func(*http.Request) (*http.Response, error)

func (f roundTripper) RoundTrip(request *http.Request) (*http.Response, error) { return f(request) }

func TestTheSandboxSendsEachOperationToItsSandboxHost(t *testing.T) {
	var lock sync.Mutex
	var hosts []string
	transport := roundTripper(func(request *http.Request) (*http.Response, error) {
		lock.Lock()
		hosts = append(hosts, request.URL.Host)
		lock.Unlock()
		return &http.Response{StatusCode: http.StatusOK, Header: http.Header{"Content-Type": {"application/json"}}, Body: io.NopCloser(strings.NewReader(`{}`)), Request: request}, nil
	})
	client, err := ebaysell.NewClient(ebaysell.WithUserToken(userToken), ebaysell.WithEnvironment(ebaysell.Sandbox), ebaysell.WithHTTPTransport(transport))
	if err != nil {
		t.Fatal(err)
	}
	ctx := context.Background()
	if _, err := client.Finances.SellerFunds.GetSummary(ctx, nil); err != nil {
		t.Fatal(err)
	}
	if err := order(client); err != nil {
		t.Fatal(err)
	}
	if want := []string{"apiz.sandbox.ebay.com", "api.sandbox.ebay.com"}; !reflect.DeepEqual(hosts, want) {
		t.Errorf("hosts are %v", hosts)
	}
	environments := ebaysell.Environments()
	environments[ebaysell.Sandbox]["api"] = "http://changed"
	if ebaysell.Environments()[ebaysell.Sandbox]["api"] != "https://api.sandbox.ebay.com" {
		t.Error("Environments returned the package's own map")
	}
}

func TestHeaderDefaultsAreSentWhereDeclaredAndACallsOwnValueWins(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) { w.WriteHeader(http.StatusNoContent) },
		ebaysell.WithUserToken(userToken), ebaysell.WithMarketplaceID("EBAY_US"), ebaysell.WithContentLanguage("en-US"))
	ctx := context.Background()
	item := &inventory.InventoryItem{Condition: ebaysell.Ptr("NEW")}
	if _, err := client.Inventory.InventoryItems.CreateOrReplace(ctx, "SYNTHETIC-SKU-1", item, nil); err != nil {
		t.Fatal(err)
	}
	if _, err := client.Inventory.InventoryItems.CreateOrReplace(ctx, "SYNTHETIC-SKU-1", item, &inventory.InventoryItemsCreateOrReplaceParams{ContentLanguage: ebaysell.Ptr("de-DE")}); err != nil {
		t.Fatal(err)
	}
	requests := seen.all()
	if requests[0].header.Get("Content-Language") != "en-US" || requests[1].header.Get("Content-Language") != "de-DE" || requests[0].header.Get("X-EBAY-C-MARKETPLACE-ID") != "" {
		t.Errorf("headers are %v and %v", requests[0].header, requests[1].header)
	}
	if requests[0].body != `{"condition":"NEW"}` {
		t.Errorf("body is %s", requests[0].body)
	}
}

func TestAPostOrderUploadSendsTheUserTokenMarketplaceAndAJSONFile(t *testing.T) {
	client, seen := server(t, accepting, ebaysell.WithUserToken(userToken), ebaysell.WithMarketplaceID("EBAY_GB"))
	file := &postorder.UploadFileRequest{Data: ebaysell.Ptr("c3ludGhldGlj"), FilePurpose: ebaysell.Ptr(postorder.FilePurposeEnumLabelRelated)}
	if _, err := client.PostOrder.Returns.UploadFile(context.Background(), "5000000001", file, nil); err != nil {
		t.Fatal(err)
	}
	request := seen.all()[0]
	if request.host != "api" || request.path != "/post-order/v2/return/5000000001/file/upload" {
		t.Errorf("sent to %s %s", request.host, request.path)
	}
	if request.header.Get("Authorization") != "Bearer "+userToken || request.header.Get("X-EBAY-C-MARKETPLACE-ID") != "EBAY_GB" || request.header.Get("Content-Type") != "application/json" {
		t.Errorf("headers are %v", request.header)
	}
	if request.body != `{"data":"c3ludGhldGlj","filePurpose":"LABEL_RELATED"}` {
		t.Errorf("body is %s", request.body)
	}
}

func TestTheIteratorFollowsNextOnTheOperationsHost(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Query().Get("offset") == "" {
			replyJSON(w, http.StatusOK, `{"orders":[{"orderId":"o1"}],"next":"https://elsewhere.invalid/sell/fulfillment/v1/order?limit=1&offset=1"}`)
			return
		}
		replyJSON(w, http.StatusOK, `{"orders":[{"orderId":"o2"}]}`)
	}, ebaysell.WithUserToken(userToken))
	var ids []string
	for order, err := range client.Fulfillment.Orders.Iter(context.Background(), &fulfillment.OrdersListParams{Limit: ebaysell.Ptr("1")}) {
		if err != nil {
			t.Fatal(err)
		}
		ids = append(ids, *order.OrderID)
	}
	if !reflect.DeepEqual(ids, []string{"o1", "o2"}) {
		t.Errorf("ids are %v", ids)
	}
	requests := seen.all()
	if len(requests) != 2 || requests[1].host != "api" || requests[1].query.Get("offset") != "1" || requests[1].query.Get("limit") != "1" {
		t.Errorf("requests are %+v", requests)
	}
}

func TestErrorsCarryTheFirstErrorAndTheirDetails(t *testing.T) {
	client, _ := server(t, func(w http.ResponseWriter, r *http.Request) {
		replyJSON(w, http.StatusNotFound, `{"errors":[{"errorId":25710,"domain":"API_INVENTORY","category":"REQUEST","message":"Not found",`+
			`"longMessage":"No item","parameters":[{"name":"sku","value":"MISSING"},"junk"]},{"errorId":"wrong","message":"second"},7]}`)
	}, ebaysell.WithUserToken(userToken))
	_, err := client.Inventory.InventoryItems.Get(context.Background(), "MISSING")
	var failure *ebaysell.APIError
	if !errors.Is(err, ebaysell.ErrNotFound) || !errors.As(err, &failure) || failure.Status != 404 || failure.Code != "25710" || failure.Detail != "Not found" {
		t.Fatalf("error is %#v", err)
	}
	if err.Error() != "HTTP 404 (not_found): Not found" {
		t.Errorf("message is %q", err.Error())
	}
	want := []ebaysell.ErrorDetail{
		{ErrorID: 25710, Domain: "API_INVENTORY", Category: "REQUEST", Message: "Not found", LongMessage: "No item", Parameters: []ebaysell.ErrorParameter{{Name: "sku", Value: "MISSING"}}},
		{Message: "second"},
	}
	if got := ebaysell.ErrorDetails(err); !reflect.DeepEqual(got, want) {
		t.Errorf("details are %#v", got)
	}
	if ebaysell.ErrorDetails(errors.New("other")) != nil {
		t.Error("an error that is not an APIError has details")
	}
}

func TestStatusesMapToKinds(t *testing.T) {
	for status, kind := range map[int]ebaysell.Kind{
		400: ebaysell.KindBadRequest, 401: ebaysell.KindAuthentication, 403: ebaysell.KindPermission, 404: ebaysell.KindNotFound,
		409: ebaysell.KindConflict, 422: ebaysell.KindValidation, 429: ebaysell.KindRateLimited, 503: ebaysell.KindServer, 418: ebaysell.KindAPI,
	} {
		client, _ := server(t, func(w http.ResponseWriter, r *http.Request) { replyJSON(w, status, `not json`) }, ebaysell.WithUserToken(userToken), ebaysell.WithMaxRetries(0))
		var failure *ebaysell.APIError
		if err := order(client); !errors.As(err, &failure) || failure.Kind != kind || failure.Code != "" || failure.RawBody != "not json" {
			t.Errorf("%d gave %v", status, err)
		}
	}
}

func signingKey(t *testing.T) (ed25519.PublicKey, string) {
	t.Helper()
	public, private, err := ed25519.GenerateKey(rand.Reader)
	if err != nil {
		t.Fatal(err)
	}
	encoded, err := x509.MarshalPKCS8PrivateKey(private)
	if err != nil {
		t.Fatal(err)
	}
	return public, base64.StdEncoding.EncodeToString(encoded)
}

var signatureInput = regexp.MustCompile(`^sig1=\("content-digest" "x-ebay-signature-key" "@method" "@path" "@authority"\);created=(\d+)$`)

func TestASigningKeyAsEBayReturnsItSignsEveryRequest(t *testing.T) {
	public, private := signingKey(t)
	client, seen := server(t, accepting, ebaysell.WithUserToken(userToken), ebaysell.WithSigningKey(ebaysell.SigningKey{PrivateKey: private, JWE: "synthetic-jwe"}))
	body := &fulfillment.IssueRefundRequest{ReasonForRefund: ebaysell.Ptr("BUYER_CANCEL")}
	if _, err := client.Fulfillment.Orders.IssueRefund(context.Background(), "01-00000-00001", body); err != nil {
		t.Fatal(err)
	}
	request := seen.all()[0]
	digest := sha256.Sum256([]byte(request.body))
	if request.header.Get("x-ebay-signature-key") != "synthetic-jwe" || request.header.Get("Content-Digest") != "sha-256=:"+base64.StdEncoding.EncodeToString(digest[:])+":" {
		t.Fatalf("headers are %v", request.header)
	}
	input := request.header.Get("Signature-Input")
	match := signatureInput.FindStringSubmatch(input)
	if match == nil {
		t.Fatalf("Signature-Input is %q", input)
	}
	base := strings.Join([]string{
		`"content-digest": ` + request.header.Get("Content-Digest"),
		`"x-ebay-signature-key": synthetic-jwe`,
		`"@method": POST`,
		`"@path": /api/sell/fulfillment/v1/order/01-00000-00001/issue_refund`,
		`"@authority": ` + request.authority,
		`"@signature-params": ` + strings.TrimPrefix(input, "sig1="),
	}, "\n")
	signature, err := base64.StdEncoding.DecodeString(strings.TrimSuffix(strings.TrimPrefix(request.header.Get("Signature"), "sig1=:"), ":"))
	if err != nil || !ed25519.Verify(public, []byte(base), signature) {
		t.Errorf("the signature does not verify over %q", base)
	}
}

func TestASigningKeyInPEMFormWorksToo(t *testing.T) {
	_, private := signingKey(t)
	encoded, _ := base64.StdEncoding.DecodeString(private)
	text := string(pem.EncodeToMemory(&pem.Block{Type: "PRIVATE KEY", Bytes: encoded}))
	client, seen := server(t, accepting, ebaysell.WithUserToken(userToken), ebaysell.WithSigningKey(ebaysell.SigningKey{PrivateKey: text, JWE: "synthetic-jwe"}))
	if err := order(client); err != nil {
		t.Fatal(err)
	}
	request := seen.all()[0]
	if !strings.HasPrefix(request.header.Get("Signature-Input"), `sig1=("x-ebay-signature-key" "@method" "@path" "@authority");created=`) || request.header.Get("Content-Digest") != "" {
		t.Errorf("headers are %v", request.header)
	}
}

func TestLogsAndErrorsNeverHoldASecret(t *testing.T) {
	_, private := signingKey(t)
	var logs bytes.Buffer
	client, _ := server(t, func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == tokenPath {
			token(w, newAppToken, 7200)
			return
		}
		replyJSON(w, http.StatusBadRequest, fmt.Sprintf(`{"errors":[{"message":"%s %s %s %s %s"}]}`, clientSecret, newAppToken, userToken, refreshToken, private))
	}, ebaysell.WithClientCredentials(clientID, clientSecret), ebaysell.WithUserToken(userToken), ebaysell.WithRefreshToken(refreshToken),
		ebaysell.WithSigningKey(ebaysell.SigningKey{PrivateKey: private, JWE: "synthetic-jwe"}),
		ebaysell.WithLogger(slog.New(slog.NewTextHandler(&logs, &slog.HandlerOptions{Level: slog.LevelDebug}))))
	errs := []error{defaultTree(client), order(client)}
	for _, err := range errs {
		var failure *ebaysell.APIError
		if !errors.As(err, &failure) {
			t.Fatalf("error is %v", err)
		}
		text := failure.RawBody + failure.Detail + err.Error() + fmt.Sprintf("%#v", failure)
		for _, secret := range []string{clientSecret, newAppToken, userToken, refreshToken, private, strings.TrimPrefix(basic, "Basic ")} {
			if strings.Contains(text, secret) || strings.Contains(logs.String(), secret) {
				t.Errorf("%q leaked", secret)
			}
		}
	}
}

func TestPrintingTokensAndKeysHidesTheSecrets(t *testing.T) {
	token := ebaysell.Token{AccessToken: userToken, RefreshToken: refreshToken}
	key := ebaysell.SigningKey{PrivateKey: "synthetic-private-key", JWE: "synthetic-jwe"}
	var logs bytes.Buffer
	slog.New(slog.NewTextHandler(&logs, nil)).Info("token", "token", token)
	text := fmt.Sprint(token) + fmt.Sprintf("%v %+v %#v", token, token, token) + fmt.Sprintf("%v %+v %#v", key, key, key) + logs.String()
	for _, secret := range []string{userToken, refreshToken, "synthetic-private-key"} {
		if strings.Contains(text, secret) {
			t.Errorf("%q is shown in %q", secret, text)
		}
	}
	if !strings.Contains(fmt.Sprint(key), "synthetic-jwe") {
		t.Error("the JWE is hidden")
	}
}

func TestAnEmpty204IsNoResult(t *testing.T) {
	client, _ := server(t, func(w http.ResponseWriter, r *http.Request) { w.WriteHeader(http.StatusNoContent) }, ebaysell.WithAppToken(appToken))
	limits, err := client.DeveloperAnalytics.RateLimits.List(context.Background(), &developeranalytics.RateLimitsListParams{})
	if err != nil || limits != nil {
		t.Fatalf("result is %v, error is %v", limits, err)
	}
}
