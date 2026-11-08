package etsyseller_test

import (
	"bytes"
	"context"
	"crypto/sha256"
	"encoding/base64"
	"errors"
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"net/http/httptest"
	"net/url"
	"os"
	"reflect"
	"regexp"
	"slices"
	"strings"
	"sync"
	"testing"
	"time"

	etsy "github.com/fdhoff/api-sdks/apis/etsy/packages/go/etsyseller"
	"github.com/fdhoff/api-sdks/apis/etsy/packages/go/internal/runtime"
)

const (
	key        = "synthetic-keystring"
	secret     = "synthetic-shared-secret"
	access     = "12345678.synthetic-access"
	refresh    = "12345678.synthetic-refresh"
	newAccess  = "12345678.synthetic-access-2"
	newRefresh = "12345678.synthetic-refresh-2"
	tokenPath  = "/v3/public/oauth/token"
	mePath     = "/v3/application/users/me"
)

// recorder answers with handle and keeps every request with its body.
type recorder struct {
	lock     sync.Mutex
	requests []*http.Request
	bodies   []string
}

func (r *recorder) all() []*http.Request {
	r.lock.Lock()
	defer r.lock.Unlock()
	return slices.Clone(r.requests)
}

func (r *recorder) request(index int) *http.Request { return r.all()[index] }

func (r *recorder) body(index int) string {
	r.lock.Lock()
	defer r.lock.Unlock()
	return r.bodies[index]
}

func (r *recorder) paths() []string {
	paths := []string{}
	for _, request := range r.all() {
		paths = append(paths, request.URL.Path)
	}
	return paths
}

func (r *recorder) form(index int) url.Values {
	values, _ := url.ParseQuery(r.body(index))
	return values
}

func server(t *testing.T, handle http.HandlerFunc, options ...etsy.Option) (*etsy.Client, *recorder) {
	t.Helper()
	seen := &recorder{}
	mock := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		body, _ := io.ReadAll(r.Body)
		seen.lock.Lock()
		seen.requests = append(seen.requests, r)
		seen.bodies = append(seen.bodies, string(body))
		seen.lock.Unlock()
		handle(w, r)
	}))
	t.Cleanup(mock.Close)
	defaults := []etsy.Option{etsy.WithBaseURL(mock.URL), etsy.WithRetryBaseDelay(time.Millisecond), etsy.WithRateLimitWait(time.Millisecond)}
	client, err := etsy.NewClient(key, secret, append(defaults, options...)...)
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

func newToken(w http.ResponseWriter) {
	replyJSON(w, http.StatusOK, fmt.Sprintf(`{"access_token":%q,"refresh_token":%q,"expires_in":3600,"token_type":"Bearer"}`, newAccess, newRefresh))
}

// expiring answers 401 until the access token is the refreshed one.
func expiring(w http.ResponseWriter, r *http.Request) {
	switch {
	case r.URL.Path == tokenPath:
		newToken(w)
	case r.Header.Get("Authorization") != "Bearer "+newAccess:
		replyJSON(w, http.StatusUnauthorized, `{"error":"invalid_token"}`)
	default:
		replyJSON(w, http.StatusOK, `{"user_id":12345678,"shop_id":1}`)
	}
}

var operationLine = regexp.MustCompile(`(?m)^(\w+): \{ resource: (\w+), method: (\w+)(?:, iterator: (\w+))?`)

func TestEveryOperationHasAPublicMethod(t *testing.T) {
	names, err := os.ReadFile("../operations.yaml")
	if err != nil {
		t.Fatal(err)
	}
	client, _ := server(t, func(w http.ResponseWriter, r *http.Request) {})
	lines := operationLine.FindAllStringSubmatch(string(names), -1)
	iterators := 0
	for _, line := range lines {
		operation, found := runtime.Lookup(line[1])
		if !found || operation.Resource != line[2] || operation.Name != line[3] || operation.Iterator != line[4] {
			t.Errorf("%s is registered as %+v", line[1], operation)
			continue
		}
		resource := reflect.ValueOf(client).Elem().FieldByName(line[2])
		for _, method := range []string{line[3], line[4]} {
			if method != "" && !resource.MethodByName(method).IsValid() {
				t.Errorf("%s.%s is missing", line[2], method)
			}
		}
		if line[4] != "" {
			iterators++
		}
	}
	if len(lines) != 107 || iterators != 16 {
		t.Errorf("%d operations and %d iterators", len(lines), iterators)
	}
}

func TestNewClientValidatesItsArguments(t *testing.T) {
	cases := map[string]struct {
		key, secret string
		options     []etsy.Option
	}{
		"no key":       {"", secret, nil},
		"no secret":    {key, "", nil},
		"relative url": {key, secret, []etsy.Option{etsy.WithBaseURL("/relative")}},
	}
	for name, item := range cases {
		t.Run(name, func(t *testing.T) {
			if _, err := etsy.NewClient(item.key, item.secret, item.options...); err == nil {
				t.Fatal("expected an error")
			}
		})
	}
}

func TestKeyOnlyOperationsSendNoAccessToken(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		replyJSON(w, http.StatusOK, `{"application_id":1}`)
	}, etsy.WithAccessToken(access), etsy.WithUserAgent("synthetic-agent"))
	if _, err := client.Application.Ping(context.Background()); err != nil {
		t.Fatal(err)
	}
	header := seen.request(0).Header
	if header.Get("x-api-key") != key+":"+secret || header.Get("Authorization") != "" || header.Get("User-Agent") != "synthetic-agent" {
		t.Errorf("sent %v", header)
	}
}

func TestOAuthOperationsSendBothHeaders(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		replyJSON(w, http.StatusOK, `{"user_id":12345678,"shop_id":1}`)
	}, etsy.WithAccessToken(access))
	me, err := client.Users.GetMe(context.Background())
	if err != nil {
		t.Fatal(err)
	}
	header := seen.request(0).Header
	if *me.UserID != 12345678 || header.Get("x-api-key") != key+":"+secret || header.Get("Authorization") != "Bearer "+access {
		t.Errorf("got %+v after sending %v", me, header)
	}
}

func TestFormBodiesAreURLEncodedWithRepeatedFields(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		replyJSON(w, http.StatusCreated, `{"listing_id":1}`)
	}, etsy.WithAccessToken(access))
	listing, err := client.Listings.CreateDraft(context.Background(), 1, &etsy.ListingsCreateDraftParams{
		Quantity:   etsy.Ptr[int64](1),
		Title:      etsy.Ptr("Synthetic listing"),
		Price:      etsy.Ptr[float32](1.5),
		TaxonomyID: etsy.Ptr[int64](1),
		Tags:       []string{"one", "two"},
		IsSupply:   etsy.Ptr(false),
	})
	if err != nil {
		t.Fatal(err)
	}
	if *listing.ListingID != 1 || seen.request(0).Header.Get("Content-Type") != "application/x-www-form-urlencoded" {
		t.Errorf("got %+v after sending %v", listing, seen.request(0).Header)
	}
	want := url.Values{"quantity": {"1"}, "title": {"Synthetic listing"}, "price": {"1.5"}, "taxonomy_id": {"1"}, "tags": {"one", "two"}, "is_supply": {"false"}}
	if form := seen.form(0); form.Encode() != want.Encode() {
		t.Errorf("sent %v", form)
	}
}

func TestQueryParametersAndFormFieldsShareOneParamsStruct(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		replyJSON(w, http.StatusOK, `{"receipt_id":2}`)
	}, etsy.WithAccessToken(access))
	params := &etsy.ReceiptsUpdateParams{Legacy: etsy.Ptr(true), WasShipped: etsy.Ptr(true)}
	if _, err := client.Receipts.Update(context.Background(), 1, 2, params); err != nil {
		t.Fatal(err)
	}
	if seen.request(0).URL.RawQuery != "legacy=true" || seen.form(0).Encode() != "was_shipped=true" {
		t.Errorf("sent %q with %q", seen.request(0).URL.RawQuery, seen.body(0))
	}
}

func TestTheOffsetIteratorWalksEveryPage(t *testing.T) {
	pages := map[string]string{"": `[{"listing_id":1},{"listing_id":2}]`, "2": `[{"listing_id":3}]`}
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		replyJSON(w, http.StatusOK, `{"count":3,"results":`+pages[r.URL.Query().Get("offset")]+`}`)
	})
	var ids []int64
	for listing, err := range client.Listings.IterActive(context.Background(), &etsy.ListingsListActiveParams{Limit: etsy.Ptr[int64](2)}) {
		if err != nil {
			t.Fatal(err)
		}
		ids = append(ids, *listing.ListingID)
	}
	offsets := []string{}
	for _, request := range seen.all() {
		offsets = append(offsets, request.URL.Query().Get("offset"))
	}
	if !slices.Equal(ids, []int64{1, 2, 3}) || !slices.Equal(offsets, []string{"", "2"}) {
		t.Errorf("got %v at offsets %q", ids, offsets)
	}
}

func TestErrorsCarryTheBodyMessage(t *testing.T) {
	for status, sentinel := range map[int]error{
		http.StatusBadRequest:          etsy.ErrBadRequest,
		http.StatusUnauthorized:        etsy.ErrAuthentication,
		http.StatusForbidden:           etsy.ErrPermission,
		http.StatusNotFound:            etsy.ErrNotFound,
		http.StatusConflict:            etsy.ErrConflict,
		http.StatusUnprocessableEntity: etsy.ErrValidation,
		http.StatusTeapot:              etsy.ErrAPI,
	} {
		client, _ := server(t, func(w http.ResponseWriter, r *http.Request) {
			replyJSON(w, status, `{"error":"Synthetic failure"}`)
		})
		_, err := client.Shops.Get(context.Background(), 1)
		var failure *etsy.APIError
		if !errors.Is(err, sentinel) || !errors.As(err, &failure) || failure.Detail != "Synthetic failure" || failure.Status != status {
			t.Errorf("%d: error is %v", status, err)
		}
	}
}

func TestA401RefreshesOnceThenRetriesWithTheNewToken(t *testing.T) {
	var stored []etsy.Token
	client, seen := server(t, expiring, etsy.WithAccessToken(access), etsy.WithRefreshToken(refresh), etsy.WithOnToken(func(token etsy.Token) {
		stored = append(stored, token)
	}))
	me, err := client.Users.GetMe(context.Background())
	if err != nil {
		t.Fatal(err)
	}
	if *me.ShopID != 1 || !slices.Equal(seen.paths(), []string{mePath, tokenPath, mePath}) {
		t.Errorf("got %+v after %v", me, seen.paths())
	}
	want := url.Values{"grant_type": {"refresh_token"}, "client_id": {key}, "refresh_token": {refresh}}
	token := seen.request(1)
	if seen.form(1).Encode() != want.Encode() || token.Header.Get("x-api-key") != "" || token.Header.Get("Authorization") != "" {
		t.Errorf("refreshed with %q and %v", seen.body(1), token.Header)
	}
	if len(stored) != 1 || stored[0].AccessToken != newAccess || stored[0].RefreshToken != newRefresh || stored[0].ExpiresIn != 3600 {
		t.Errorf("stored %d tokens", len(stored))
	}
	if _, err := client.Users.GetMe(context.Background()); err != nil {
		t.Fatal(err)
	}
	if paths := seen.paths(); len(paths) != 4 || paths[3] != mePath {
		t.Errorf("then sent %v", paths)
	}
}

func TestConcurrent401sShareOneRefresh(t *testing.T) {
	client, seen := server(t, expiring, etsy.WithAccessToken(access), etsy.WithRefreshToken(refresh))
	var group sync.WaitGroup
	errs := make([]error, 4)
	for index := range errs {
		group.Add(1)
		go func() {
			defer group.Done()
			_, errs[index] = client.Users.GetMe(context.Background())
		}()
	}
	group.Wait()
	if err := errors.Join(errs...); err != nil {
		t.Fatal(err)
	}
	if refreshes := slices.Index(seen.paths(), tokenPath); refreshes < 0 || slices.Contains(seen.paths()[refreshes+1:], tokenPath) {
		t.Errorf("sent %v", seen.paths())
	}
}

func (r *recorder) refreshTokens() []string {
	tokens := []string{}
	for index, request := range r.all() {
		if request.URL.Path == tokenPath {
			tokens = append(tokens, r.form(index).Get("refresh_token"))
		}
	}
	return tokens
}

func TestAnExplicitRefreshAndA401ShareOneTokenRequest(t *testing.T) {
	started := make(chan struct{})
	var once sync.Once
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		switch {
		case r.URL.Path == tokenPath:
			once.Do(func() { close(started) })
			time.Sleep(200 * time.Millisecond)
		case r.Header.Get("Authorization") == "Bearer "+access:
			<-started
		}
		expiring(w, r)
	}, etsy.WithAccessToken(access), etsy.WithRefreshToken(refresh))
	explicit := make(chan error, 1)
	go func() {
		_, err := client.OAuth.Refresh(context.Background())
		explicit <- err
	}()
	me, err := client.Users.GetMe(context.Background())
	if err != nil {
		t.Fatal(err)
	}
	if err := <-explicit; err != nil {
		t.Fatal(err)
	}
	if *me.ShopID != 1 || !slices.Equal(seen.refreshTokens(), []string{refresh}) {
		t.Errorf("sent %v", seen.paths())
	}
}

func TestA401SentBeforeAnExplicitRefreshRetriesWithoutAnother(t *testing.T) {
	refreshed := make(chan struct{})
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == mePath && r.Header.Get("Authorization") == "Bearer "+access {
			<-refreshed
		}
		expiring(w, r)
	}, etsy.WithAccessToken(access), etsy.WithRefreshToken(refresh))
	call := make(chan error, 1)
	go func() {
		_, err := client.Users.GetMe(context.Background())
		call <- err
	}()
	for !slices.Contains(seen.paths(), mePath) {
		time.Sleep(time.Millisecond)
	}
	if _, err := client.OAuth.Refresh(context.Background()); err != nil {
		t.Fatal(err)
	}
	close(refreshed)
	if err := <-call; err != nil {
		t.Fatal(err)
	}
	if !slices.Equal(seen.paths(), []string{mePath, tokenPath, mePath}) {
		t.Errorf("sent %v", seen.paths())
	}
}

func TestACancelledCallerDoesNotLoseARotatedToken(t *testing.T) {
	ctx, cancel := context.WithCancel(context.Background())
	var stored []etsy.Token
	client, _ := server(t, func(w http.ResponseWriter, r *http.Request) {
		cancel()
		time.Sleep(50 * time.Millisecond)
		newToken(w)
	}, etsy.WithRefreshToken(refresh), etsy.WithOnToken(func(token etsy.Token) { stored = append(stored, token) }))
	if _, err := client.OAuth.Refresh(ctx); err != nil {
		t.Fatal(err)
	}
	if len(stored) != 1 || stored[0].RefreshToken != newRefresh {
		t.Errorf("stored %d tokens", len(stored))
	}
}

func TestASecond401AfterARefreshIsReturned(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == tokenPath {
			newToken(w)
			return
		}
		replyJSON(w, http.StatusUnauthorized, `{"error":"invalid_token"}`)
	}, etsy.WithAccessToken(access), etsy.WithRefreshToken(refresh))
	if _, err := client.Users.GetMe(context.Background()); !errors.Is(err, etsy.ErrAuthentication) {
		t.Fatalf("error is %v", err)
	}
	if !slices.Equal(seen.paths(), []string{mePath, tokenPath, mePath}) {
		t.Errorf("sent %v", seen.paths())
	}
}

func TestA401OnAKeyOnlyOperationDoesNotRefresh(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		replyJSON(w, http.StatusUnauthorized, `{"error":"invalid_api_key"}`)
	}, etsy.WithAccessToken(access), etsy.WithRefreshToken(refresh))
	if _, err := client.Application.Ping(context.Background()); !errors.Is(err, etsy.ErrAuthentication) {
		t.Fatalf("error is %v", err)
	}
	if !slices.Equal(seen.paths(), []string{"/v3/application/openapi-ping"}) {
		t.Errorf("sent %v", seen.paths())
	}
}

func TestWithoutARefreshTokenA401IsReturned(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		replyJSON(w, http.StatusUnauthorized, `{"error":"invalid_token"}`)
	}, etsy.WithAccessToken(access))
	if _, err := client.Users.GetMe(context.Background()); !errors.Is(err, etsy.ErrAuthentication) {
		t.Fatalf("error is %v", err)
	}
	if !slices.Equal(seen.paths(), []string{mePath}) {
		t.Errorf("sent %v", seen.paths())
	}
	if _, err := client.OAuth.Refresh(context.Background()); err == nil {
		t.Error("refreshed without a refresh token")
	}
}

func TestAFailedRefreshReturnsItsErrorWithoutTheRefreshToken(t *testing.T) {
	client, _ := server(t, func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == tokenPath {
			replyJSON(w, http.StatusBadRequest, fmt.Sprintf(`{"error":"invalid_grant","error_description":"bad %s"}`, refresh))
			return
		}
		replyJSON(w, http.StatusUnauthorized, `{"error":"invalid_token"}`)
	}, etsy.WithAccessToken(access), etsy.WithRefreshToken(refresh))
	_, err := client.Users.GetMe(context.Background())
	var failure *etsy.APIError
	if !errors.Is(err, etsy.ErrBadRequest) || !errors.As(err, &failure) || failure.Detail != "invalid_grant" {
		t.Fatalf("error is %v", err)
	}
	if strings.Contains(failure.RawBody, refresh) || strings.Contains(err.Error(), refresh) {
		t.Errorf("error shows the refresh token: %q", failure.RawBody)
	}
}

func TestA401FromTheTokenEndpointIsReturnedWithoutAnotherRefresh(t *testing.T) {
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		replyJSON(w, http.StatusUnauthorized, `{"error":"invalid_client"}`)
	}, etsy.WithAccessToken(access), etsy.WithRefreshToken(refresh))
	_, err := client.Users.GetMe(context.Background())
	var failure *etsy.APIError
	if !errors.As(err, &failure) || failure.Kind != etsy.KindAuthentication || failure.Detail != "invalid_client" {
		t.Fatalf("error is %v", err)
	}
	if !slices.Equal(seen.paths(), []string{mePath, tokenPath}) {
		t.Errorf("sent %v", seen.paths())
	}
}

func TestATokenResponseWithoutTokensIsADecodeError(t *testing.T) {
	client, _ := server(t, func(w http.ResponseWriter, r *http.Request) {
		replyJSON(w, http.StatusOK, `{"token_type":"Bearer"}`)
	}, etsy.WithRefreshToken(refresh))
	if _, err := client.OAuth.Refresh(context.Background()); !errors.Is(err, etsy.ErrDecode) {
		t.Fatalf("error is %v", err)
	}
}

func TestExchangeCodeStoresTheTokenForLaterCalls(t *testing.T) {
	var stored []etsy.Token
	client, seen := server(t, func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == tokenPath {
			newToken(w)
			return
		}
		replyJSON(w, http.StatusOK, `{"user_id":12345678,"shop_id":1}`)
	}, etsy.WithOnToken(func(token etsy.Token) { stored = append(stored, token) }))
	verifier := strings.Repeat("v", 43)
	token, err := client.OAuth.ExchangeCode(context.Background(), "synthetic-code", verifier, "https://example.com/callback")
	if err != nil {
		t.Fatal(err)
	}
	if id, ok := token.UserID(); !ok || id != 12345678 || len(stored) != 1 || stored[0] != token {
		t.Errorf("got user %d and stored %d tokens", id, len(stored))
	}
	want := url.Values{
		"grant_type":    {"authorization_code"},
		"client_id":     {key},
		"redirect_uri":  {"https://example.com/callback"},
		"code":          {"synthetic-code"},
		"code_verifier": {verifier},
	}
	if seen.form(0).Encode() != want.Encode() {
		t.Errorf("sent %q", seen.body(0))
	}
	if _, err := client.Users.GetMe(context.Background()); err != nil {
		t.Fatal(err)
	}
	if seen.request(1).Header.Get("Authorization") != "Bearer "+newAccess {
		t.Errorf("then sent %v", seen.request(1).Header)
	}
}

func TestLogsAndErrorsNeverHoldASecret(t *testing.T) {
	secrets := []string{key, secret, access, refresh, newAccess, newRefresh}
	var logs bytes.Buffer
	client, _ := server(t, func(w http.ResponseWriter, r *http.Request) {
		if r.URL.Path == tokenPath {
			newToken(w)
			return
		}
		w.WriteHeader(http.StatusForbidden)
		fmt.Fprint(w, strings.Join(secrets, " ")+" "+r.Header.Get("Authorization"))
	}, etsy.WithAccessToken(access), etsy.WithRefreshToken(refresh), etsy.WithLogger(slog.New(slog.NewTextHandler(&logs, &slog.HandlerOptions{Level: slog.LevelDebug}))))
	token, err := client.OAuth.Refresh(context.Background())
	if err != nil {
		t.Fatal(err)
	}
	_, err = client.Users.GetMe(context.Background())
	var failure *etsy.APIError
	if !errors.As(err, &failure) {
		t.Fatalf("error is %v", err)
	}
	text := fmt.Sprintf("%v %s %s %v %+v %#v", err, failure.RawBody, logs.String(), token, token, token)
	if logs.Len() == 0 {
		t.Error("nothing was logged")
	}
	for _, value := range secrets {
		if strings.Contains(text, value) {
			t.Errorf("%q is shown in %q", value, text)
		}
	}
}

func TestAuthorizationRequestUsesPKCES256AndState(t *testing.T) {
	request, err := etsy.NewAuthorizationRequest(key, etsy.AuthorizationParams{RedirectURI: "https://example.com/callback", Scopes: []string{"listings_r", "shops_r"}})
	if err != nil {
		t.Fatal(err)
	}
	parsed, err := url.Parse(request.URL)
	if err != nil {
		t.Fatal(err)
	}
	digest := sha256.Sum256([]byte(request.CodeVerifier))
	want := url.Values{
		"response_type":         {"code"},
		"client_id":             {key},
		"redirect_uri":          {"https://example.com/callback"},
		"scope":                 {"listings_r shops_r"},
		"state":                 {request.State},
		"code_challenge":        {base64.RawURLEncoding.EncodeToString(digest[:])},
		"code_challenge_method": {"S256"},
	}
	if !strings.HasPrefix(request.URL, etsy.AuthorizationEndpoint+"?") || parsed.Query().Encode() != want.Encode() {
		t.Errorf("URL is %q", request.URL)
	}
	if length := len(request.CodeVerifier); length < 43 || length > 128 || request.State == "" {
		t.Errorf("verifier %d long, state %q", length, request.State)
	}
	other, err := etsy.NewAuthorizationRequest(key, etsy.AuthorizationParams{RedirectURI: "https://example.com/callback", Scopes: []string{"listings_r"}})
	if err != nil || other.State == request.State || other.CodeVerifier == request.CodeVerifier {
		t.Errorf("a second request reused the state or verifier: %v", err)
	}
}

func TestPrintingAnAuthorizationRequestHidesItsVerifier(t *testing.T) {
	request, err := etsy.NewAuthorizationRequest(key, etsy.AuthorizationParams{RedirectURI: "https://example.com/callback", Scopes: []string{"shops_r"}})
	if err != nil {
		t.Fatal(err)
	}
	var logs bytes.Buffer
	slog.New(slog.NewTextHandler(&logs, nil)).Info("authorize", "request", request)
	text := fmt.Sprintf("%v %+v %#v %v %s", request, request, request, *request, logs.String())
	if strings.Contains(text, request.CodeVerifier) || !strings.Contains(text, request.State) {
		t.Errorf("printed %q", text)
	}
}

func TestAuthorizationRequestKeepsAGivenStateAndRejectsBadInput(t *testing.T) {
	client, _ := server(t, func(w http.ResponseWriter, r *http.Request) {})
	request, err := client.OAuth.AuthorizationRequest(etsy.AuthorizationParams{RedirectURI: "https://example.com/callback", Scopes: []string{"shops_r"}, State: "synthetic-state"})
	if err != nil || request.State != "synthetic-state" {
		t.Errorf("got %+v, %v", request, err)
	}
	for name, params := range map[string]etsy.AuthorizationParams{
		"short verifier": {RedirectURI: "https://example.com/callback", Scopes: []string{"shops_r"}, CodeVerifier: "short"},
		"no scopes":      {RedirectURI: "https://example.com/callback"},
	} {
		if _, err := etsy.NewAuthorizationRequest(key, params); err == nil {
			t.Errorf("%s: no error", name)
		}
	}
}

func TestATokenWithoutAUserPrefixHasNoUserID(t *testing.T) {
	if _, ok := (etsy.Token{AccessToken: "synthetic"}).UserID(); ok {
		t.Error("found a user ID")
	}
}
