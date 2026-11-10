package runtime

import (
	"context"
	"encoding/json"
	"errors"
	"io"
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

// bodiless is a page answered with this status and no body.
type bodiless int

// walk serves the bodies in order and returns every item and the query of every request.
func walk(t *testing.T, operation *Operation, params any, serve func(query url.Values) any) ([]map[string]any, []string, error) {
	t.Helper()
	var lock sync.Mutex
	var queries []string
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		lock.Lock()
		defer lock.Unlock()
		queries = append(queries, r.URL.RawQuery)
		body := serve(r.URL.Query())
		if status, ok := body.(bodiless); ok {
			w.WriteHeader(int(status))
			return
		}
		w.Header().Set("Content-Type", "application/json")
		_ = json.NewEncoder(w).Encode(body)
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

func TestPagingStopsAtAnEmpty204Page(t *testing.T) {
	limit := 2
	bodies := []any{map[string]any{"data": numbered(0, 2)}, bodiless(http.StatusNoContent)}
	items, queries, err := walk(t, offsetList, pageParams{Limit: &limit}, func(url.Values) any {
		body := bodies[0]
		bodies = bodies[1:]
		return body
	})
	if err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(items, numbered(0, 2)) {
		t.Errorf("items are %v", items)
	}
	if want := []string{"limit=2", "limit=2&start=2"}; !reflect.DeepEqual(queries, want) {
		t.Errorf("queries are %q, want %q", queries, want)
	}
	items, _, err = walk(t, offsetList, pageParams{}, func(url.Values) any { return bodiless(http.StatusNoContent) })
	if err != nil || len(items) != 0 {
		t.Errorf("a first page of 204 gives %v, %v", items, err)
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

type cursorParams struct {
	Limit *int    `query:"limit"`
	After *string `query:"start_after"`
}

var cursorList = &Operation{
	ID: "list-items", Method: "GET", Path: "/items", QueryParams: []string{"limit", "start_after"},
	Paging: Cursor{Items: "data", Next: "page.next_page", Param: "start_after"},
}

// served answers with the bodies in order.
func served(bodies ...any) func(url.Values) any {
	return func(url.Values) any {
		body := bodies[0]
		bodies = bodies[1:]
		return body
	}
}

func TestCursorPagingSendsTheNextValueBackUntilItIsNull(t *testing.T) {
	limit := 2
	items, queries, err := walk(t, cursorList, cursorParams{Limit: &limit}, served(
		map[string]any{"data": numbered(0, 2), "page": map[string]any{"next_page": "b"}},
		map[string]any{"data": numbered(2, 4), "page": map[string]any{"next_page": "d"}},
		map[string]any{"data": numbered(4, 5), "page": map[string]any{"next_page": nil}},
	))
	if err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(items, numbered(0, 5)) {
		t.Errorf("items are %v", items)
	}
	if want := []string{"limit=2", "limit=2&start_after=b", "limit=2&start_after=d"}; !reflect.DeepEqual(queries, want) {
		t.Errorf("queries are %q, want %q", queries, want)
	}
}

func TestCursorPagingStartsAtTheCallersPositionAndStopsWithoutANextValue(t *testing.T) {
	after := "a"
	items, queries, err := walk(t, cursorList, cursorParams{After: &after}, served(
		map[string]any{"data": numbered(1, 2), "page": map[string]any{"next_page": "b"}},
		map[string]any{"data": []any{}, "page": map[string]any{"next_page": ""}},
	))
	if err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(items, numbered(1, 2)) {
		t.Errorf("items are %v", items)
	}
	if want := []string{"start_after=a", "start_after=b"}; !reflect.DeepEqual(queries, want) {
		t.Errorf("queries are %q, want %q", queries, want)
	}
	for _, body := range []any{map[string]any{"data": []any{}}, map[string]any{"data": []any{}, "page": nil}} {
		if _, _, err := walk(t, cursorList, cursorParams{}, served(body)); err != nil {
			t.Errorf("for %v, error is %v", body, err)
		}
	}
}

func TestCursorPagingSendsAnIntegerNextValueBackAsItsDigits(t *testing.T) {
	items, queries, err := walk(t, cursorList, cursorParams{}, served(
		map[string]any{"data": numbered(0, 1), "page": map[string]any{"next_page": 0}},
		map[string]any{"data": numbered(1, 2), "page": map[string]any{"next_page": 7}},
		map[string]any{"data": numbered(2, 3), "page": map[string]any{"next_page": json.RawMessage("1.0")}},
		map[string]any{"data": numbered(3, 4), "page": map[string]any{"next_page": 9007199254740991}},
		map[string]any{"data": []any{}, "page": map[string]any{"next_page": nil}},
	))
	if err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(items, numbered(0, 4)) {
		t.Errorf("items are %v", items)
	}
	if want := []string{"", "start_after=0", "start_after=7", "start_after=1", "start_after=9007199254740991"}; !reflect.DeepEqual(queries, want) {
		t.Errorf("queries are %q, want %q", queries, want)
	}
}

func TestCursorPagingRejectsANextValueEqualToTheOneSent(t *testing.T) {
	for sent, next := range map[string]any{"a": "a", "3": 3} {
		_, queries, err := walk(t, cursorList, cursorParams{After: &sent}, served(map[string]any{"data": numbered(0, 1), "page": map[string]any{"next_page": next}}))
		var failure *Error
		if !errors.As(err, &failure) || failure.Kind != KindDecode || !strings.Contains(err.Error(), "does not advance the iteration") {
			t.Fatalf("for %v, error is %v", next, err)
		}
		if len(queries) != 1 {
			t.Errorf("queries are %q", queries)
		}
	}
}

func TestPagingRejectsAPositionThatCyclesBack(t *testing.T) {
	linkList := &Operation{
		ID: "list-items", Method: "GET", Path: "/items", QueryParams: []string{"token"},
		Paging: NextLink{Items: "data", Link: "more", Params: []string{"token"}},
	}
	cases := []struct {
		operation *Operation
		params    any
		bodies    []any
		want      []string
	}{
		{linkList, pageParams{}, []any{
			map[string]any{"more": "/items?token=b", "data": numbered(0, 1)},
			map[string]any{"more": "/items?token=a", "data": numbered(1, 2)},
			map[string]any{"more": "/items?token=b", "data": numbered(2, 3)},
		}, []string{"", "token=b", "token=a"}},
		{cursorList, cursorParams{}, []any{
			map[string]any{"data": numbered(0, 1), "page": map[string]any{"next_page": "a"}},
			map[string]any{"data": numbered(1, 2), "page": map[string]any{"next_page": "b"}},
			map[string]any{"data": numbered(2, 3), "page": map[string]any{"next_page": "a"}},
		}, []string{"", "start_after=a", "start_after=b"}},
	}
	for _, c := range cases {
		items, queries, err := walk(t, c.operation, c.params, served(c.bodies...))
		var failure *Error
		if !errors.As(err, &failure) || failure.Kind != KindDecode || !strings.Contains(err.Error(), "already requested") {
			t.Fatalf("for %T, error is %v", c.operation.paging(), err)
		}
		if !reflect.DeepEqual(items, numbered(0, 3)) {
			t.Errorf("items are %v", items)
		}
		if !reflect.DeepEqual(queries, c.want) {
			t.Errorf("queries are %q, want %q", queries, c.want)
		}
	}
}

func TestCursorPagingRejectsAMalformedPage(t *testing.T) {
	for _, body := range []any{
		map[string]any{"page": map[string]any{"next_page": "b"}},
		map[string]any{"data": nil},
		map[string]any{"data": numbered(0, 1), "page": map[string]any{"next_page": 2.5}},
		map[string]any{"data": numbered(0, 1), "page": map[string]any{"next_page": 9007199254740992}},
		map[string]any{"data": numbered(0, 1), "page": map[string]any{"next_page": int64(-1 << 63)}},
		map[string]any{"data": numbered(0, 1), "page": map[string]any{"next_page": true}},
		map[string]any{"data": numbered(0, 1), "page": map[string]any{"next_page": map[string]any{"id": "b"}}},
		map[string]any{"data": numbered(0, 1), "page": "b"},
	} {
		_, _, err := walk(t, cursorList, cursorParams{}, served(body))
		var failure *Error
		if !errors.As(err, &failure) || failure.Kind != KindDecode {
			t.Errorf("for %v, error is %v", body, err)
		}
	}
}

func TestAnEmpty204IsNoResultEvenWhereJSONIsDeclared(t *testing.T) {
	transport := mustTransport(t, Settings{BaseURL: "http://example.invalid", Credentials: StaticCredentials{}, Timeout: time.Second})
	operation := &Operation{ID: "get-item", Method: "GET", Path: "/items/1", ReturnsJSON: true}
	result, err := decode[*map[string]any](transport, operation, &response{status: http.StatusNoContent})
	if err != nil || result != nil {
		t.Fatalf("result is %v, %v", result, err)
	}
	if _, err := decode[*map[string]any](transport, operation, &response{status: http.StatusOK}); err == nil {
		t.Fatal("an empty 200 decoded")
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

type linkParams struct {
	Page  *int    `query:"page"`
	Limit *int    `query:"limit"`
	State *string `query:"state"`
}

// linked is a page answered with these Link header values.
type linked struct {
	links []string
	body  any
}

// walkLinked serves the pages in order and returns every item and the query of every request.
func walkLinked(t *testing.T, operation *Operation, params any, pages ...linked) ([]map[string]any, []string, error) {
	t.Helper()
	var lock sync.Mutex
	var queries []string
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		lock.Lock()
		defer lock.Unlock()
		queries = append(queries, r.URL.RawQuery)
		page := pages[0]
		pages = pages[1:]
		for _, link := range page.links {
			w.Header().Add("Link", link)
		}
		w.Header().Set("Content-Type", "application/json")
		_ = json.NewEncoder(w).Encode(page.body)
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

var linkList = &Operation{
	ID: "list-items", Method: "GET", Path: "/items", QueryParams: []string{"page", "limit", "state"},
	Paging: LinkHeader{Items: "$", Rel: "next", Params: []string{"page", "limit"}},
}

func TestLinkHeaderPagingFollowsTheNextLinkUntilThereIsNone(t *testing.T) {
	limit, state := 2, "open"
	items, queries, err := walkLinked(t, linkList, linkParams{Limit: &limit, State: &state},
		linked{[]string{`<https://example.test/items?page=2&limit=2>; rel="next"`}, numbered(0, 2)},
		linked{[]string{`<https://example.test/items?page=3&limit=2>; rel="next", <https://example.test/items?page=1&limit=2>; rel="prev"`}, numbered(2, 4)},
		linked{[]string{`<https://example.test/items?page=2&limit=2>; rel="prev"`}, numbered(4, 5)},
	)
	if err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(items, numbered(0, 5)) {
		t.Errorf("items are %v", items)
	}
	if want := []string{"limit=2&state=open", "limit=2&page=2&state=open", "limit=2&page=3&state=open"}; !reflect.DeepEqual(queries, want) {
		t.Errorf("queries are %q, want %q", queries, want)
	}
}

func TestLinkHeaderPagingReadsAnObjectPagesItemsField(t *testing.T) {
	operation := &Operation{
		ID: "list-bins", Method: "GET", Path: "/bins", QueryParams: []string{"page", "limit"},
		Paging: LinkHeader{Items: "bins", Rel: "next", Params: []string{"page", "limit"}},
	}
	items, queries, err := walkLinked(t, operation, linkParams{},
		linked{[]string{`</bins?page=2>; rel=next`}, map[string]any{"total_count": 2, "bins": numbered(0, 1)}},
		linked{nil, map[string]any{"total_count": 2, "bins": numbered(1, 2)}},
	)
	if err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(items, numbered(0, 2)) {
		t.Errorf("items are %v", items)
	}
	if want := []string{"", "page=2"}; !reflect.DeepEqual(queries, want) {
		t.Errorf("queries are %q, want %q", queries, want)
	}
	for _, body := range []any{map[string]any{"total_count": 0}, numbered(0, 1)} {
		_, _, err := walkLinked(t, operation, linkParams{}, linked{nil, body})
		var failure *Error
		if !errors.As(err, &failure) || failure.Kind != KindDecode {
			t.Errorf("for %v, error is %v", body, err)
		}
	}
}

func TestLinkHeaderPagingNeverFetchesALinkOnAnotherHost(t *testing.T) {
	elsewhere := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		t.Errorf("the other host was sent %s %s", r.Method, r.URL)
	}))
	t.Cleanup(elsewhere.Close)
	items, queries, err := walkLinked(t, linkList, linkParams{},
		linked{[]string{"<" + elsewhere.URL + "/api/v1/items?page=2>; rel=\"next\""}, numbered(0, 1)},
		linked{nil, numbered(1, 2)},
	)
	if err != nil {
		t.Fatal(err)
	}
	if !reflect.DeepEqual(items, numbered(0, 2)) {
		t.Errorf("items are %v", items)
	}
	if want := []string{"", "page=2"}; !reflect.DeepEqual(queries, want) {
		t.Errorf("queries are %q, want %q", queries, want)
	}
}

func TestLinkHeaderPagingRejectsARepeatedPosition(t *testing.T) {
	page := 1
	items, queries, err := walkLinked(t, linkList, linkParams{Page: &page},
		linked{[]string{`<https://example.test/items?page=2>; rel="next"`}, numbered(0, 1)},
		linked{[]string{`<https://example.test/items?page=1>; rel="next"`}, numbered(1, 2)},
	)
	var failure *Error
	if !errors.As(err, &failure) || failure.Kind != KindDecode || !strings.Contains(err.Error(), "already requested") {
		t.Fatalf("error is %v", err)
	}
	if !reflect.DeepEqual(items, numbered(0, 2)) {
		t.Errorf("items are %v", items)
	}
	if want := []string{"page=1", "page=2"}; !reflect.DeepEqual(queries, want) {
		t.Errorf("queries are %q, want %q", queries, want)
	}
	_, _, err = walkLinked(t, linkList, linkParams{Page: &page}, linked{[]string{`<https://example.test/items?page=1>; rel="next"`}, numbered(0, 1)})
	if !errors.As(err, &failure) || failure.Kind != KindDecode || !strings.Contains(err.Error(), "does not advance") {
		t.Fatalf("a link to the same page gives %v", err)
	}
}

func TestLinkHeaderPagingReadsSeveralHeadersEntriesAndRels(t *testing.T) {
	limit := 2
	items, queries, err := walkLinked(t, linkList, linkParams{Limit: &limit},
		linked{[]string{
			`<https://example.test/items?page=9&limit=2>; rel="prev first"`,
			`<https://example.test/items?a=1,2&page=7>; title="x, rel=next"; rel="last", <https://example.test/items?page=%32&limit=2>; REL="Last NEXT"; rel=prev`,
		}, numbered(0, 2)},
		linked{[]string{`<https://example.test/items?page=3&limit=2&state=closed>;rel=next`}, numbered(2, 4)},
		linked{[]string{`<https://example.test/items?page=>; rel=next`, `not a link; rel=next`}, numbered(4, 5)},
	)
	var failure *Error
	if !errors.As(err, &failure) || failure.Kind != KindDecode || !strings.Contains(err.Error(), "does not advance") {
		t.Fatalf("error is %v", err)
	}
	if !reflect.DeepEqual(items, numbered(0, 5)) {
		t.Errorf("items are %v", items)
	}
	if want := []string{"limit=2", "limit=2&page=2", "limit=2&page=3"}; !reflect.DeepEqual(queries, want) {
		t.Errorf("queries are %q, want %q", queries, want)
	}
}

func TestLinkHeaderPagingRejectsAPageThatIsNotAList(t *testing.T) {
	for _, body := range []any{map[string]any{"data": numbered(0, 1)}, nil, "items"} {
		_, _, err := walkLinked(t, linkList, linkParams{}, linked{nil, body})
		var failure *Error
		if !errors.As(err, &failure) || failure.Kind != KindDecode || !strings.Contains(err.Error(), "not a JSON list") {
			t.Errorf("for %v, error is %v", body, err)
		}
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

var createTransfer = &Operation{ID: "create-transfer", Method: "POST", Path: "/transfers", IdempotencyKey: "idempotencyKey"}

// writes sends one call to a server that fails every request with a 503, and returns the bodies it received.
func writes(t *testing.T, operation *Operation, body any) []string {
	t.Helper()
	var lock sync.Mutex
	var bodies []string
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		received, _ := io.ReadAll(r.Body)
		lock.Lock()
		bodies = append(bodies, string(received))
		lock.Unlock()
		w.WriteHeader(http.StatusServiceUnavailable)
	}))
	t.Cleanup(server.Close)
	transport := mustTransport(t, Settings{
		BaseURL:        server.URL,
		ToError:        func(context ErrorContext) *Error { return &Error{Kind: KindAPI, Status: context.Status} },
		Timeout:        time.Second,
		MaxRetries:     2,
		RetryBaseDelay: time.Millisecond,
	})
	_, err := Call[any](context.Background(), transport, operation, Input{Body: body})
	var failure *Error
	if !errors.As(err, &failure) || failure.Status != http.StatusServiceUnavailable {
		t.Fatalf("error is %v", err)
	}
	lock.Lock()
	defer lock.Unlock()
	return bodies
}

func TestAWriteWithItsIdempotencyKeySetIsRetriedWithTheSameBody(t *testing.T) {
	bodies := writes(t, createTransfer, map[string]any{"idempotencyKey": "k-1", "amount": 5})
	if len(bodies) != 3 || bodies[1] != bodies[0] || bodies[2] != bodies[0] {
		t.Errorf("bodies are %q", bodies)
	}
}

func TestAWriteWithoutAnIdempotencyKeyIsNotRetried(t *testing.T) {
	unmarked := &Operation{ID: "create-item", Method: "POST", Path: "/items"}
	cases := []struct {
		name      string
		operation *Operation
		body      any
	}{
		{"unmarked", unmarked, map[string]any{"idempotencyKey": "k-1"}},
		{"empty key", createTransfer, map[string]any{"idempotencyKey": "", "amount": 5}},
		{"null key", createTransfer, map[string]any{"idempotencyKey": nil, "amount": 5}},
		{"missing key", createTransfer, map[string]any{"amount": 5}},
	}
	for _, test := range cases {
		t.Run(test.name, func(t *testing.T) {
			if bodies := writes(t, test.operation, test.body); len(bodies) != 1 {
				t.Errorf("sent %d requests", len(bodies))
			}
		})
	}
}
