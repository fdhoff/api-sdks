package runtime

import (
	"context"
	"encoding/json"
	"net/http"
	"net/http/httptest"
	"reflect"
	"strings"
	"sync"
	"testing"
	"time"
)

var (
	listItems = &Operation{ID: "list-items", Method: "GET", Path: "/items", HeaderParams: []string{"X-Tenant"}, Security: []Requirement{{{Name: "key"}}}}
	listFiles = &Operation{
		ID: "list-files", Method: "GET", Path: "/files", Host: "files", QueryParams: []string{"offset"},
		Paging: Offset{Items: "results", Total: "count", Offset: "offset"}, Security: []Requirement{{{Name: "key"}}},
	}
	unknownHost = &Operation{ID: "list-other", Method: "GET", Path: "/other", Host: "other", Security: []Requirement{{{Name: "key"}}}}
)

type itemsParams struct {
	Tenant *string `header:"X-Tenant"`
}

type sentRequest struct {
	host   string
	path   string
	header http.Header
}

// hosted serves two hosts, each answering a page of one item and then an empty page, and records
// which host every request reached.
func hosted(t *testing.T, defaults map[string]string, credentials Credentials, headers http.Header) (*Transport, func() []sentRequest) {
	t.Helper()
	var lock sync.Mutex
	var sent []sentRequest
	serve := func(host string) *httptest.Server {
		server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
			lock.Lock()
			defer lock.Unlock()
			sent = append(sent, sentRequest{host: host, path: r.URL.RequestURI(), header: r.Header.Clone()})
			w.Header().Set("Content-Type", "application/json")
			results := []any{map[string]any{"id": host}}
			if r.URL.Query().Get("offset") != "" {
				results = []any{}
			}
			_ = json.NewEncoder(w).Encode(map[string]any{"results": results})
		}))
		t.Cleanup(server.Close)
		return server
	}
	main, files := serve("main"), serve("files")
	transport := mustTransport(t, Settings{
		BaseURL:        main.URL,
		Hosts:          map[string]string{"main": main.URL, "files": files.URL},
		HeaderDefaults: defaults,
		Credentials:    credentials,
		Headers:        headers,
		Timeout:        time.Second,
	})
	return transport, func() []sentRequest {
		lock.Lock()
		defer lock.Unlock()
		return append([]sentRequest(nil), sent...)
	}
}

func TestAnOperationWithoutAHostGoesToTheBaseURL(t *testing.T) {
	transport, sent := hosted(t, nil, nil, nil)
	if _, err := Call[map[string]any](context.Background(), transport, listItems, Input{}); err != nil {
		t.Fatal(err)
	}
	if got := sent(); len(got) != 1 || got[0].host != "main" || got[0].path != "/items" {
		t.Errorf("sent %+v", got)
	}
}

func TestAnOperationGoesToItsHostWithItsCredentials(t *testing.T) {
	transport, sent := hosted(t, nil, StaticCredentials{Header: http.Header{"Authorization": {"Basic " + syntheticKey}}, Values: []string{syntheticKey}}, nil)
	if _, err := Call[map[string]any](context.Background(), transport, listFiles, Input{}); err != nil {
		t.Fatal(err)
	}
	got := sent()
	if len(got) != 1 || got[0].host != "files" || got[0].path != "/files" || got[0].header.Get("Authorization") != "Basic "+syntheticKey {
		t.Errorf("sent %+v", got)
	}
}

func TestAnIteratorReissuesEveryPageAgainstTheOperationsHost(t *testing.T) {
	transport, sent := hosted(t, nil, nil, nil)
	var items []map[string]any
	for item, err := range Paginate[map[string]any](context.Background(), transport, listFiles, Input{}) {
		if err != nil {
			t.Fatal(err)
		}
		items = append(items, item)
	}
	got := sent()
	if len(items) != 1 || len(got) != 2 || got[0].host != "files" || got[1].host != "files" || got[1].path != "/files?offset=1" {
		t.Errorf("items %v, sent %+v", items, got)
	}
}

func TestAnUnknownHostKeyFailsBeforeAnythingIsAppliedOrSent(t *testing.T) {
	credentials := &tokens{version: 1}
	transport, sent := hosted(t, nil, credentials, nil)
	_, err := Call[map[string]any](context.Background(), transport, unknownHost, Input{})
	if err == nil || !strings.Contains(err.Error(), `"other"`) {
		t.Errorf("error %v", err)
	}
	if len(credentials.seen) != 0 || len(sent()) != 0 {
		t.Errorf("applied %d times, sent %+v", len(credentials.seen), sent())
	}
}

var environments = map[string]map[string]string{
	"production": {"main": "https://main.example.test", "files": "https://files.example.test"},
	"sandbox":    {"main": "https://main.sandbox.example.test/", "files": "https://files.sandbox.example.test"},
}

func TestSelectHostsPicksTheNamedEnvironment(t *testing.T) {
	hosts, err := SelectHosts(environments, "sandbox", nil)
	want := map[string]string{"main": "https://main.sandbox.example.test", "files": "https://files.sandbox.example.test"}
	if err != nil || !reflect.DeepEqual(hosts, want) {
		t.Fatalf("hosts %v, error %v", hosts, err)
	}
	hosts["main"] = "changed"
	if environments["sandbox"]["main"] == "changed" {
		t.Error("the environment was not copied")
	}
}

func TestSelectHostsRejectsAnUnknownEnvironment(t *testing.T) {
	_, err := SelectHosts(environments, "staging", nil)
	if err == nil || !strings.Contains(err.Error(), `"staging"`) || !strings.Contains(err.Error(), "production, sandbox") {
		t.Errorf("error %v", err)
	}
}

func TestSelectHostsTakesTheCallersOwnMap(t *testing.T) {
	hosts, err := SelectHosts(environments, "production", map[string]string{"main": "http://127.0.0.1:1/", "files": "http://127.0.0.1:2"})
	want := map[string]string{"main": "http://127.0.0.1:1", "files": "http://127.0.0.1:2"}
	if err != nil || !reflect.DeepEqual(hosts, want) {
		t.Errorf("hosts %v, error %v", hosts, err)
	}
}

func TestSelectHostsRejectsACallersMapWithMissingOrUnknownKeys(t *testing.T) {
	_, err := SelectHosts(environments, "production", map[string]string{"main": "http://127.0.0.1:1"})
	if err == nil || !strings.Contains(err.Error(), "lacks keys: files") {
		t.Errorf("missing: %v", err)
	}
	_, err = SelectHosts(environments, "production", map[string]string{"main": "a", "files": "b", "zeta": "c", "extra": "d"})
	if err == nil || !strings.Contains(err.Error(), "unknown keys: extra, zeta") {
		t.Errorf("unknown: %v", err)
	}
}

func tenantSent(t *testing.T, defaults map[string]string, headers http.Header, operation *Operation, params any) []string {
	t.Helper()
	transport, sent := hosted(t, defaults, nil, headers)
	if _, err := Call[map[string]any](context.Background(), transport, operation, Input{Params: params}); err != nil {
		t.Fatal(err)
	}
	got := sent()
	if len(got) != 1 {
		t.Fatalf("sent %+v", got)
	}
	return got[0].header.Values("X-Tenant")
}

func TestAHeaderDefaultIsSentOnAnOperationThatDeclaresIt(t *testing.T) {
	if got := tenantSent(t, map[string]string{"x-TENANT": "acme"}, nil, listItems, nil); !reflect.DeepEqual(got, []string{"acme"}) {
		t.Errorf("sent %v", got)
	}
}

func TestAHeaderArgumentOverridesTheDefault(t *testing.T) {
	other := "other"
	got := tenantSent(t, map[string]string{"X-Tenant": "acme"}, nil, listItems, &itemsParams{Tenant: &other})
	if !reflect.DeepEqual(got, []string{"other"}) {
		t.Errorf("sent %v", got)
	}
}

func TestAHeaderDefaultReplacesAClientWideHeaderOfTheSameName(t *testing.T) {
	got := tenantSent(t, map[string]string{"X-Tenant": "acme"}, http.Header{"X-Tenant": {"client-wide"}}, listItems, nil)
	if !reflect.DeepEqual(got, []string{"acme"}) {
		t.Errorf("sent %v", got)
	}
}

func TestAHeaderDefaultNeverReachesAnOperationThatDoesNotDeclareIt(t *testing.T) {
	if got := tenantSent(t, map[string]string{"X-Tenant": "acme"}, nil, listFiles, nil); len(got) != 0 {
		t.Errorf("sent %v", got)
	}
}

func TestHeaderDefaultsThatDifferOnlyByCaseAreRejectedAtConstruction(t *testing.T) {
	_, err := NewTransport(Settings{HeaderDefaults: map[string]string{"x-tenant": "acme", "X-Tenant": "other", "X-Other": "unused"}})
	if err == nil || err.Error() != "HeaderDefaults has names that differ only by case: X-Tenant, x-tenant" {
		t.Errorf("error %v", err)
	}
}

func TestAHeaderWithNeitherArgumentNorDefaultIsNotSent(t *testing.T) {
	if got := tenantSent(t, nil, nil, listItems, nil); len(got) != 0 {
		t.Errorf("sent %v", got)
	}
}
