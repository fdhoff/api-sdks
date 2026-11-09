package runtime

import (
	"context"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"reflect"
	"sync"
	"testing"
	"time"
)

var (
	getSiteItem = &Operation{
		ID: "get-item", Method: "GET", Path: "/items/{id}", PathParams: []string{"id"}, QueryParams: []string{"site"},
		QueryDefaults: []string{"site"},
	}
	listSiteItems = &Operation{
		ID: "list-items", Method: "GET", Path: "/items", QueryParams: []string{"site", "after"}, QueryDefaults: []string{"site"},
		Paging: Cursor{Items: "results", Next: "next", Param: "after"},
	}
	listSiteFiles = &Operation{ID: "list-files", Method: "GET", Path: "/files", QueryParams: []string{"site"}}
)

type siteParams struct {
	Site *string `query:"site"`
}

// queried answers each request with one page that links to the next until `after` is set, and records
// every request URI.
func queried(t *testing.T, defaults map[string]string) (*Transport, func() []string) {
	t.Helper()
	var lock sync.Mutex
	var sent []string
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		lock.Lock()
		defer lock.Unlock()
		sent = append(sent, r.URL.RequestURI())
		w.Header().Set("Content-Type", "application/json")
		page := map[string]any{"results": []any{map[string]any{"id": len(sent)}}, "next": "b"}
		if r.URL.Query().Has("after") {
			page["next"] = nil
		}
		_ = json.NewEncoder(w).Encode(page)
	}))
	t.Cleanup(server.Close)
	transport := mustTransport(t, Settings{BaseURL: server.URL, QueryDefaults: defaults, Timeout: time.Second})
	return transport, func() []string {
		lock.Lock()
		defer lock.Unlock()
		return append([]string(nil), sent...)
	}
}

func TestAQueryDefaultIsSentUnlessTheCallGivesAValue(t *testing.T) {
	transport, sent := queried(t, map[string]string{"site": "north"})
	south := "south"
	for _, params := range []*siteParams{nil, {Site: &south}} {
		input := Input{Path: []any{"1"}}
		if params != nil {
			input.Params = params
		}
		if _, err := Call[map[string]any](context.Background(), transport, getSiteItem, input); err != nil {
			t.Fatal(err)
		}
	}
	if got, want := sent(), []string{"/items/1?site=north", "/items/1?site=south"}; !reflect.DeepEqual(got, want) {
		t.Errorf("sent %v, want %v", got, want)
	}
}

func TestAQueryParameterWithNeitherArgumentNorDefaultIsNotSent(t *testing.T) {
	transport, sent := queried(t, nil)
	if _, err := Call[map[string]any](context.Background(), transport, getSiteItem, Input{Path: []any{"1"}, Params: &siteParams{}}); err != nil {
		t.Fatal(err)
	}
	if got, want := sent(), []string{"/items/1"}; !reflect.DeepEqual(got, want) {
		t.Errorf("sent %v, want %v", got, want)
	}
}

func TestQueryDefaultNamesMatchExactly(t *testing.T) {
	transport, sent := queried(t, map[string]string{"Site": "north"})
	if _, err := Call[map[string]any](context.Background(), transport, getSiteItem, Input{Path: []any{"1"}}); err != nil {
		t.Fatal(err)
	}
	if got, want := sent(), []string{"/items/1"}; !reflect.DeepEqual(got, want) {
		t.Errorf("sent %v, want %v", got, want)
	}
}

func TestAQueryDefaultNeverReachesAParameterThatDoesNotTakeOne(t *testing.T) {
	transport, sent := queried(t, map[string]string{"site": "north"})
	if _, err := Call[map[string]any](context.Background(), transport, listSiteFiles, Input{}); err != nil {
		t.Fatal(err)
	}
	if got, want := sent(), []string{"/files"}; !reflect.DeepEqual(got, want) {
		t.Errorf("sent %v, want %v", got, want)
	}
}

func TestAnIteratorSendsTheQueryDefaultOnEveryPage(t *testing.T) {
	transport, sent := queried(t, map[string]string{"site": "north"})
	count := 0
	for _, err := range Paginate[map[string]any](context.Background(), transport, listSiteItems, Input{}) {
		if err != nil {
			t.Fatal(err)
		}
		count++
	}
	if got, want := sent(), []string{"/items?site=north", "/items?after=b&site=north"}; count != 2 || !reflect.DeepEqual(got, want) {
		t.Errorf("sent %v for %d items, want %v", got, count, want)
	}
}
