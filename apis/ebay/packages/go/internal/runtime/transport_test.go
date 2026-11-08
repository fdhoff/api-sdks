package runtime

import (
	"context"
	"encoding/json"
	"errors"
	"net/http"
	"net/http/httptest"
	"net/url"
	"reflect"
	"strconv"
	"strings"
	"sync"
	"testing"
	"time"
)

func TestARequestThatCannotBeBuiltDoesNotShowTheTokenEvenEscaped(t *testing.T) {
	const secret = "synthetic/test+token="
	transport := mustTransport(t, Settings{BaseURL: "http://example.invalid\x7f", Credentials: StaticCredentials{Values: []string{secret}}, Timeout: time.Second})
	operation := &Operation{ID: "op", Method: "GET", Path: "/items/{id}", PathParams: []string{"id"}}
	_, err := Call[any](context.Background(), transport, operation, Input{Path: []any{secret}})
	var failure *Error
	if !errors.As(err, &failure) || failure.Kind != KindConnection || !strings.HasPrefix(err.Error(), "the request could not be built: ") {
		t.Fatalf("error is %v", err)
	}
	for _, form := range []string{secret, url.PathEscape(secret)} {
		if strings.Contains(err.Error(), form) {
			t.Errorf("error shows %q: %q", form, err.Error())
		}
	}
	var parse *url.Error
	if !errors.As(err, &parse) {
		t.Errorf("error does not unwrap to its cause: %v", err)
	}
}

type pageParams struct {
	Limit *int    `query:"limit"`
	Start *int    `query:"start"`
	Token *string `query:"token"`
}

// walk serves the bodies in order and returns every item and the query of every request.
func walk(t *testing.T, operation *Operation, params any, serve func(query url.Values) any) ([]map[string]any, []string, error) {
	t.Helper()
	var lock sync.Mutex
	var queries []string
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		lock.Lock()
		defer lock.Unlock()
		queries = append(queries, r.URL.RawQuery)
		w.Header().Set("Content-Type", "application/json")
		_ = json.NewEncoder(w).Encode(serve(r.URL.Query()))
	}))
	t.Cleanup(server.Close)
	transport := mustTransport(t, Settings{BaseURL: server.URL, Timeout: time.Second})
	var items []map[string]any
	var failure error
	for item, err := range Paginate[map[string]any](context.Background(), transport, operation, Input{Params: params}) {
		if err != nil {
			failure = err
			break
		}
		items = append(items, item)
	}
	lock.Lock()
	defer lock.Unlock()
	return items, queries, failure
}

var offsetList = &Operation{
	ID: "list-items", Method: "GET", Path: "/items", QueryParams: []string{"limit", "start"},
	Paging: Offset{Items: "data", Total: "total", Offset: "start"},
}

func numbered(from, to int) []map[string]any {
	items := []map[string]any{}
	for n := from; n < to; n++ {
		items = append(items, map[string]any{"n": float64(n)})
	}
	return items
}

func TestOffsetPagingAdvancesByTheItemsReceivedUntilTheTotal(t *testing.T) {
	limit := 2
	items, queries, err := walk(t, offsetList, pageParams{Limit: &limit}, func(query url.Values) any {
		start, _ := strconv.Atoi(query.Get("start"))
		return map[string]any{"total": 5, "data": numbered(start, min(start+2, 5))}
	})
	if err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(items, numbered(0, 5)) {
		t.Errorf("items are %v", items)
	}
	if want := []string{"limit=2", "limit=2&start=2", "limit=2&start=4"}; !reflect.DeepEqual(queries, want) {
		t.Errorf("queries are %q, want %q", queries, want)
	}
}

func TestOffsetPagingStartsAtTheCallersOffsetAndStopsAtAnEmptyPage(t *testing.T) {
	start := 3
	bodies := []any{map[string]any{"total": nil, "data": numbered(3, 4)}, map[string]any{"data": []any{}}}
	items, queries, err := walk(t, offsetList, pageParams{Start: &start}, func(url.Values) any {
		body := bodies[0]
		bodies = bodies[1:]
		return body
	})
	if err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(items, numbered(3, 4)) {
		t.Errorf("items are %v", items)
	}
	if want := []string{"start=3", "start=4"}; !reflect.DeepEqual(queries, want) {
		t.Errorf("queries are %q, want %q", queries, want)
	}
}

func TestOffsetPagingRejectsAPageThatIsNotAnObject(t *testing.T) {
	_, _, err := walk(t, offsetList, pageParams{}, func(url.Values) any { return []any{} })
	var failure *Error
	if !errors.As(err, &failure) || failure.Kind != KindDecode {
		t.Fatalf("error is %v", err)
	}
}

func TestOffsetPagingStopsAtATotalThatIsNotAnInteger(t *testing.T) {
	items, queries, err := walk(t, offsetList, pageParams{}, func(url.Values) any {
		return map[string]any{"total": 2.0, "data": numbered(0, 2)}
	})
	if err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(items, numbered(0, 2)) {
		t.Errorf("items are %v", items)
	}
	if want := []string{""}; !reflect.DeepEqual(queries, want) {
		t.Errorf("queries are %q, want %q", queries, want)
	}
}

func TestOffsetPagingRejectsAnOffsetThatIsNotAnInteger(t *testing.T) {
	start := "later"
	params := struct {
		Start *string `query:"start"`
	}{Start: &start}
	_, _, err := walk(t, offsetList, params, func(url.Values) any { return map[string]any{"data": numbered(0, 1)} })
	var failure *Error
	if !errors.As(err, &failure) || failure.Kind != KindDecode || !strings.Contains(err.Error(), "start parameter is not an integer") {
		t.Fatalf("error is %v", err)
	}
}

func TestOffsetPagingRejectsAPageWithoutAnItemsList(t *testing.T) {
	for _, body := range []any{map[string]any{"total": 1}, map[string]any{"data": nil}, map[string]any{"data": map[string]any{"n": 1}}} {
		_, _, err := walk(t, offsetList, pageParams{}, func(url.Values) any { return body })
		var failure *Error
		if !errors.As(err, &failure) || failure.Kind != KindDecode {
			t.Errorf("for %v, error is %v", body, err)
		}
	}
}

func TestNextLinkPagingReadsTheConfiguredFields(t *testing.T) {
	operation := &Operation{
		ID: "list-items", Method: "GET", Path: "/items", QueryParams: []string{"token"},
		Paging: NextLink{Items: "data", Link: "more", Params: []string{"token"}},
	}
	bodies := []any{map[string]any{"more": "/items?token=b", "data": numbered(1, 2)}, map[string]any{"more": nil, "data": numbered(2, 3)}}
	items, queries, err := walk(t, operation, pageParams{}, func(url.Values) any {
		body := bodies[0]
		bodies = bodies[1:]
		return body
	})
	if err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(items, numbered(1, 3)) {
		t.Errorf("items are %v", items)
	}
	if want := []string{"", "token=b"}; !reflect.DeepEqual(queries, want) {
		t.Errorf("queries are %q, want %q", queries, want)
	}
}

func TestNextLinkPagingRejectsAPageWithoutAnItemsList(t *testing.T) {
	operation := &Operation{ID: "list-items", Method: "GET", Path: "/items", QueryParams: []string{"token"}, Paging: NextLink{Items: "data", Link: "more", Params: []string{"token"}}}
	for _, body := range []any{map[string]any{"total": 0}, map[string]any{"data": nil}, map[string]any{"data": "none", "more": nil}} {
		_, _, err := walk(t, operation, pageParams{}, func(url.Values) any { return body })
		var failure *Error
		if !errors.As(err, &failure) || failure.Kind != KindDecode {
			t.Errorf("for %v, error is %v", body, err)
		}
	}
}

// answer serves one response with this status and no body.
func answer(t *testing.T, status int) *Transport {
	t.Helper()
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) { w.WriteHeader(status) }))
	t.Cleanup(server.Close)
	return mustTransport(t, Settings{BaseURL: server.URL, Timeout: time.Second, MaxRetries: 0})
}

func TestAnEmpty204IsNoResultEvenWhereJSONIsDeclared(t *testing.T) {
	operation := &Operation{ID: "put-item", Method: "PUT", Path: "/items", ReturnsJSON: true}
	result, err := Call[*map[string]any](context.Background(), answer(t, http.StatusNoContent), operation, Input{})
	if err != nil || result != nil {
		t.Fatalf("result is %v, error is %v", result, err)
	}
}

func TestAnEmpty200IsADecodeErrorWhereJSONIsDeclared(t *testing.T) {
	operation := &Operation{ID: "put-item", Method: "PUT", Path: "/items", ReturnsJSON: true}
	_, err := Call[*map[string]any](context.Background(), answer(t, http.StatusOK), operation, Input{})
	var failure *Error
	if !errors.As(err, &failure) || failure.Kind != KindDecode {
		t.Fatalf("error is %v", err)
	}
}

func TestOperationsAreFoundByContractAndID(t *testing.T) {
	plain := Register(Operation{ID: "registry-test-get"})
	scoped := Register(Operation{ID: "registry-test-get", Contract: "registry_test"})
	if found, ok := Lookup("registry-test-get"); !ok || found != plain {
		t.Errorf("Lookup without a contract found %v", found)
	}
	if found, ok := Lookup("registry_test.registry-test-get"); !ok || found != scoped {
		t.Errorf("Lookup with a contract found %v", found)
	}
}
