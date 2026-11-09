package miraklseller_test

import (
	"bytes"
	"context"
	"errors"
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"net/http/httptest"
	"strings"
	"sync"
	"testing"
	"time"

	mirakl "github.com/fdhoff/api-sdks/apis/mirakl/packages/go/miraklseller"
)

const key = "00000000-0000-4000-8000-5e11e4000099"

type seen struct {
	method, path, query string
	header              http.Header
}

type recorder struct {
	lock     sync.Mutex
	requests []seen
}

func (r *recorder) add(request *http.Request) int {
	r.lock.Lock()
	defer r.lock.Unlock()
	r.requests = append(r.requests, seen{request.Method, request.URL.Path, request.URL.RawQuery, request.Header.Clone()})
	return len(r.requests)
}

func (r *recorder) all() []seen {
	r.lock.Lock()
	defer r.lock.Unlock()
	return append([]seen(nil), r.requests...)
}

// mock serves handler at a fresh origin, recording every request.
func mock(t *testing.T, handler func(w http.ResponseWriter, r *http.Request, count int)) (*httptest.Server, *recorder) {
	t.Helper()
	record := &recorder{}
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		handler(w, r, record.add(r))
	}))
	t.Cleanup(server.Close)
	return server, record
}

func newClient(t *testing.T, baseURL string, options ...mirakl.Option) *mirakl.Client {
	t.Helper()
	defaults := []mirakl.Option{mirakl.WithRetryBaseDelay(time.Millisecond), mirakl.WithRateLimitWait(time.Millisecond)}
	client, err := mirakl.NewClient(baseURL, mirakl.APIKey(key), append(defaults, options...)...)
	if err != nil {
		t.Fatal(err)
	}
	return client
}

func replyJSON(w http.ResponseWriter, status int, body string) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	fmt.Fprint(w, body)
}

func TestNewClientValidatesItsArguments(t *testing.T) {
	cases := map[string]struct {
		baseURL     string
		credentials mirakl.Credentials
	}{
		"no base URL":       {"", mirakl.APIKey(key)},
		"a relative URL":    {"example.mirakl.net", mirakl.APIKey(key)},
		"another scheme":    {"ftp://example.mirakl.net", mirakl.APIKey(key)},
		"a query":           {"https://example.mirakl.net?shop=1", mirakl.APIKey(key)},
		"no credentials":    {"https://example.mirakl.net", nil},
		"an empty API key":  {"https://example.mirakl.net", mirakl.APIKey("")},
		"a fragment":        {"https://example.mirakl.net/#top", mirakl.APIKey(key)},
		"no host":           {"https:///api", mirakl.APIKey(key)},
		"an unparsable URL": {"https://exa mple.mirakl.net", mirakl.APIKey(key)},
	}
	for name, item := range cases {
		t.Run(name, func(t *testing.T) {
			if _, err := mirakl.NewClient(item.baseURL, item.credentials); err == nil {
				t.Fatal("expected an error")
			}
		})
	}
}

func TestTheKeyIsTheWholeAuthorizationHeaderAtTheBaseURL(t *testing.T) {
	server, record := mock(t, func(w http.ResponseWriter, _ *http.Request, _ int) {
		replyJSON(w, 200, `{"shop_id":2001,"shop_name":"Synthetic shop"}`)
	})
	client := newClient(t, server.URL+"/", mirakl.WithUserAgent("example-app/1.0"))
	account, err := client.Account.Get(context.Background(), nil)
	if err != nil || *account.ShopID != 2001 || *account.ShopName != "Synthetic shop" {
		t.Fatalf("account is %v, %v", account, err)
	}
	got := record.all()[0]
	if got.method != http.MethodGet || got.path != "/api/account" || got.query != "" {
		t.Fatalf("request is %s %s?%s", got.method, got.path, got.query)
	}
	if got.header.Get("Authorization") != key || got.header.Get("User-Agent") != "example-app/1.0" || got.header.Get("Accept") != "application/json" {
		t.Fatalf("headers are %v", got.header)
	}
}

func TestTheShopIDDefaultsPerClientAndAPerCallValueWins(t *testing.T) {
	server, record := mock(t, func(w http.ResponseWriter, _ *http.Request, _ int) {
		replyJSON(w, 200, `{"shop_id":2001}`)
	})
	ctx := context.Background()
	withShop := newClient(t, server.URL, mirakl.WithShopID(2001))
	if _, err := withShop.Account.Get(ctx, nil); err != nil {
		t.Fatal(err)
	}
	if _, err := withShop.Account.Get(ctx, &mirakl.AccountGetParams{ShopID: mirakl.Ptr[int64](2002)}); err != nil {
		t.Fatal(err)
	}
	if _, err := newClient(t, server.URL).Account.Get(ctx, nil); err != nil {
		t.Fatal(err)
	}
	got := record.all()
	for index, expected := range []string{"shop_id=2001", "shop_id=2002", ""} {
		if got[index].query != expected {
			t.Fatalf("request %d has query %q, not %q", index, got[index].query, expected)
		}
	}
}

func TestIterFollowsTheNextPageTokenWithTheShopID(t *testing.T) {
	server, record := mock(t, func(w http.ResponseWriter, _ *http.Request, count int) {
		if count == 1 {
			replyJSON(w, 200, `{"data":[{"id":"shipment-1"}],"next_page_token":"token-2"}`)
			return
		}
		replyJSON(w, 200, `{"data":[{"id":"shipment-2"}],"next_page_token":null}`)
	})
	client := newClient(t, server.URL, mirakl.WithShopID(2001))
	var ids []string
	for shipment, err := range client.Shipments.Iter(context.Background(), &mirakl.ShipmentsListParams{Limit: mirakl.Ptr[int64](1)}) {
		if err != nil {
			t.Fatal(err)
		}
		ids = append(ids, *shipment.ID)
	}
	if strings.Join(ids, ",") != "shipment-1,shipment-2" {
		t.Fatalf("shipments are %v", ids)
	}
	got := record.all()
	if got[0].query != "limit=1&shop_id=2001" || got[1].query != "limit=1&page_token=token-2&shop_id=2001" {
		t.Fatalf("queries are %q and %q", got[0].query, got[1].query)
	}
}

func TestIterAdvancesTheOffsetToTheTotal(t *testing.T) {
	server, record := mock(t, func(w http.ResponseWriter, _ *http.Request, count int) {
		if count == 1 {
			replyJSON(w, 200, `{"orders":[{"order_id":"order-1"},{"order_id":"order-2"}],"total_count":3}`)
			return
		}
		replyJSON(w, 200, `{"orders":[{"order_id":"order-3"}],"total_count":3}`)
	})
	client := newClient(t, server.URL)
	var ids []string
	for order, err := range client.Orders.Iter(context.Background(), &mirakl.OrdersListParams{Max: mirakl.Ptr[int64](2)}) {
		if err != nil {
			t.Fatal(err)
		}
		ids = append(ids, *order.OrderID)
	}
	got := record.all()
	if strings.Join(ids, ",") != "order-1,order-2,order-3" || len(got) != 2 || got[1].query != "max=2&offset=2" {
		t.Fatalf("orders are %v after %d requests, the last %q", ids, len(got), got[len(got)-1].query)
	}
}

func TestAWaitPollsUntilTheJobEndsAndReturnsAFailedStatus(t *testing.T) {
	server, record := mock(t, func(w http.ResponseWriter, _ *http.Request, count int) {
		if count < 3 {
			replyJSON(w, 200, `{"import_id":"stock-1","status":"RUNNING"}`)
			return
		}
		replyJSON(w, 200, `{"import_id":"stock-1","status":"FAILED","has_error_report":true}`)
	})
	client := newClient(t, server.URL)
	status, err := client.Offers.WaitStockImport(context.Background(), "stock-1", &mirakl.WaitOptions{Interval: time.Millisecond})
	if err != nil || *status.Status != "FAILED" || !*status.HasErrorReport {
		t.Fatalf("status is %v, %v", status, err)
	}
	got := record.all()
	if len(got) != 3 || got[2].path != "/api/offers/stock/imports/stock-1/status" {
		t.Fatalf("polled %d times, last at %s", len(got), got[len(got)-1].path)
	}
}

func TestAWaitStopsAtItsDeadlineWithTheLastStatus(t *testing.T) {
	server, _ := mock(t, func(w http.ResponseWriter, _ *http.Request, _ int) {
		replyJSON(w, 200, `{"status":"PENDING"}`)
	})
	client := newClient(t, server.URL)
	status, err := client.Orders.WaitExport(context.Background(), "tracking-9", &mirakl.WaitOptions{Interval: time.Millisecond, Timeout: 5 * time.Millisecond})
	var failure *mirakl.APIError
	if !errors.Is(err, mirakl.ErrJobTimeout) || !errors.As(err, &failure) || *status.Status != "PENDING" {
		t.Fatalf("wait returned %v, %v", status, err)
	}
	if last, isStatus := failure.Result.(*mirakl.OR14Response200); !isStatus || *last.Status != "PENDING" {
		t.Fatalf("the error holds %v", failure.Result)
	}
}

func TestAWaitStopsWhenItsContextEnds(t *testing.T) {
	server, _ := mock(t, func(w http.ResponseWriter, _ *http.Request, _ int) {
		replyJSON(w, 200, `{"status":"PENDING"}`)
	})
	client := newClient(t, server.URL)
	ctx, cancel := context.WithTimeout(context.Background(), 20*time.Millisecond)
	defer cancel()
	if _, err := client.Transactions.WaitExport(ctx, "tracking-1", nil); !errors.Is(err, context.DeadlineExceeded) {
		t.Fatalf("wait returned %v", err)
	}
}

func TestDownloadURLSendsTheKeyOnlyToTheBaseURLsOrigin(t *testing.T) {
	other, otherRecord := mock(t, func(w http.ResponseWriter, _ *http.Request, _ int) {
		w.Header().Set("Content-Type", "application/json")
		fmt.Fprint(w, `[{"order_id":"order-1"}]`)
	})
	own, ownRecord := mock(t, func(w http.ResponseWriter, r *http.Request, _ int) {
		if r.URL.Path == "/exports/moved.json" {
			http.Redirect(w, r, other.URL+"/stored/moved.json?signature=synthetic-signature", http.StatusFound)
			return
		}
		w.Header().Set("Content-Type", "application/json")
		fmt.Fprint(w, `[]`)
	})
	var logs bytes.Buffer
	client := newClient(t, own.URL, mirakl.WithLogger(slog.New(slog.NewTextHandler(&logs, nil))))
	ctx := context.Background()
	for _, address := range []string{own.URL + "/exports/own.json", other.URL + "/exports/other.json?signature=synthetic-signature", own.URL + "/exports/moved.json"} {
		download, err := client.DownloadURL(ctx, address)
		if err != nil {
			t.Fatalf("%s: %v", address, err)
		}
		body, _ := io.ReadAll(download.Body)
		download.Body.Close()
		if download.ContentType != "application/json" || len(body) == 0 {
			t.Fatalf("%s: got %q, %q", address, download.ContentType, body)
		}
	}
	for _, request := range ownRecord.all() {
		if request.header.Get("Authorization") != key {
			t.Fatalf("%s had Authorization %q", request.path, request.header.Get("Authorization"))
		}
	}
	for _, request := range otherRecord.all() {
		if _, sent := request.header["Authorization"]; sent {
			t.Fatalf("the key went to another origin at %s", request.path)
		}
	}
	if len(otherRecord.all()) != 2 || strings.Contains(logs.String(), "synthetic-signature") || strings.Contains(logs.String(), key) {
		t.Fatalf("%d cross-origin requests; logs: %s", len(otherRecord.all()), logs.String())
	}
	if _, err := client.DownloadURL(ctx, "/exports/relative.json"); err == nil {
		t.Fatal("a relative URL was fetched")
	}
}

func TestErrorsAreTypedAndHideTheKey(t *testing.T) {
	server, _ := mock(t, func(w http.ResponseWriter, r *http.Request, _ int) {
		if r.URL.Path == "/api/orders" {
			replyJSON(w, 401, `"unknown key `+key+`"`)
			return
		}
		replyJSON(w, 404, `gone`)
	})
	var logs bytes.Buffer
	client := newClient(t, server.URL, mirakl.WithLogger(slog.New(slog.NewTextHandler(&logs, nil))))
	ctx := context.Background()
	_, err := client.Orders.List(ctx, nil)
	var failure *mirakl.APIError
	if !errors.Is(err, mirakl.ErrAuthentication) || !errors.As(err, &failure) || failure.Status != 401 || failure.RawBody != `"unknown key ***"` {
		t.Fatalf("error is %#v", err)
	}
	if _, err := client.Offers.GetStockImport(ctx, "missing-import", nil); !errors.Is(err, mirakl.ErrNotFound) {
		t.Fatalf("error is %v", err)
	}
	if strings.Contains(err.Error(), key) || strings.Contains(logs.String(), key) {
		t.Fatal("the key reached an error or the logs")
	}
}

type headerCredentials struct{ value string }

func (c headerCredentials) Apply(_ context.Context, request *mirakl.AuthRequest) error {
	request.Header.Set("Authorization", "Bearer "+c.value)
	return nil
}

func (c headerCredentials) Secrets() []string { return []string{c.value} }

func TestCustomCredentialsAreAppliedToEveryRequest(t *testing.T) {
	server, record := mock(t, func(w http.ResponseWriter, _ *http.Request, _ int) {
		replyJSON(w, 200, `{}`)
	})
	client, err := mirakl.NewClient(server.URL, headerCredentials{"synthetic-partner-token"})
	if err != nil {
		t.Fatal(err)
	}
	if _, err := client.Settings.ListChannels(context.Background(), nil); err != nil {
		t.Fatal(err)
	}
	if got := record.all()[0]; got.header.Get("Authorization") != "Bearer synthetic-partner-token" || got.path != "/api/channels" {
		t.Fatalf("request to %s had Authorization %q", got.path, got.header.Get("Authorization"))
	}
}
