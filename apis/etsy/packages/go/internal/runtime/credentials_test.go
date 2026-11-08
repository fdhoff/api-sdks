package runtime

import (
	"context"
	"errors"
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"net/http/httptest"
	"slices"
	"strings"
	"sync"
	"sync/atomic"
	"testing"
	"time"
)

const (
	syntheticKey    = "synthetic-key"
	syntheticShared = "synthetic-shared-secret"
)

var getItem = &Operation{
	ID: "get-item", Method: "GET", Path: "/items/{id}", PathParams: []string{"id"}, ReturnsJSON: true,
	Security: []Requirement{{{Name: "key"}, {Name: "user", Scopes: []string{"items_r"}}}},
}

// tokens is a synthetic bearer token that changes on each refresh, beside a fixed key.
type tokens struct {
	lock      sync.Mutex
	version   int
	refreshes int
	seen      []AuthRequest
}

func (c *tokens) token() string { return fmt.Sprintf("synthetic-access-%d", c.version) }

func (c *tokens) Apply(_ context.Context, request *AuthRequest) error {
	c.lock.Lock()
	defer c.lock.Unlock()
	c.seen = append(c.seen, *request)
	request.Header.Set("X-Api-Key", syntheticKey+":"+syntheticShared)
	for _, requirement := range request.Operation.Security {
		if slices.ContainsFunc(requirement, func(scheme Scheme) bool { return scheme.Name == "user" }) {
			request.Header.Set("Authorization", "Bearer "+c.token())
		}
	}
	return nil
}

func (c *tokens) Secrets() []string {
	c.lock.Lock()
	defer c.lock.Unlock()
	return []string{syntheticKey, syntheticShared, c.token(), "synthetic-refresh"}
}

func (c *tokens) Refresh(context.Context, *AuthRequest) (bool, error) {
	time.Sleep(10 * time.Millisecond)
	c.lock.Lock()
	defer c.lock.Unlock()
	c.refreshes++
	c.version++
	return true, nil
}

func mustTransport(t *testing.T, settings Settings) *Transport {
	t.Helper()
	transport, err := NewTransport(settings)
	if err != nil {
		t.Fatal(err)
	}
	return transport
}

func serveFor(t *testing.T, credentials Credentials, handler http.HandlerFunc, logger *slog.Logger) *Transport {
	t.Helper()
	server := httptest.NewServer(handler)
	t.Cleanup(server.Close)
	return mustTransport(t, Settings{
		BaseURL:     server.URL,
		Credentials: credentials,
		Headers:     http.Header{"User-Agent": {"test"}},
		ToError: func(context ErrorContext) *Error {
			return &Error{Kind: KindAPI, Message: "failed: " + context.Text, Status: context.Status, RawBody: context.Text}
		},
		Logger:     logger,
		Timeout:    time.Second,
		MaxRetries: 1,
	})
}

func accepts(token string) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		if r.Header.Get("Authorization") != "Bearer "+token {
			w.WriteHeader(http.StatusUnauthorized)
			return
		}
		w.Header().Set("Content-Type", "application/json")
		_, _ = w.Write([]byte(`{"id":1}`))
	}
}

func TestApplySeesTheFinalRequestOnEveryAttempt(t *testing.T) {
	credentials := &tokens{version: 1}
	var lock sync.Mutex
	var sent []http.Header
	transport := serveFor(t, credentials, func(w http.ResponseWriter, r *http.Request) {
		lock.Lock()
		defer lock.Unlock()
		sent = append(sent, r.Header.Clone())
		if len(sent) == 1 {
			w.WriteHeader(http.StatusServiceUnavailable)
			return
		}
		w.Header().Set("Content-Type", "application/json")
		_, _ = w.Write([]byte(`{"id":1}`))
	}, nil)
	if _, err := Call[map[string]any](context.Background(), transport, getItem, Input{Path: []any{"a b"}}); err != nil {
		t.Fatal(err)
	}
	if len(credentials.seen) != 2 {
		t.Fatalf("apply ran %d times", len(credentials.seen))
	}
	first := credentials.seen[0]
	if first.Method != "GET" || !strings.HasSuffix(first.URL, "/items/a%20b") || len(first.Body) != 0 || first.Operation != getItem {
		t.Errorf("apply saw %+v", first)
	}
	for _, header := range sent {
		if header.Get("Authorization") != "Bearer synthetic-access-1" || header.Get("X-Api-Key") != syntheticKey+":"+syntheticShared {
			t.Errorf("sent %v", header)
		}
	}
}

func TestApplyGetsTheBodyThatIsSent(t *testing.T) {
	credentials := &tokens{version: 1}
	received := make(chan []byte, 1)
	transport := serveFor(t, credentials, func(w http.ResponseWriter, r *http.Request) {
		body, _ := io.ReadAll(r.Body)
		received <- body
		w.WriteHeader(http.StatusNoContent)
	}, nil)
	operation := &Operation{ID: "create", Method: "POST", Path: "/items", Security: []Requirement{{{Name: "key"}}}}
	if _, err := Call[any](context.Background(), transport, operation, Input{Body: map[string]int{"n": 1}}); err != nil {
		t.Fatal(err)
	}
	if body := <-received; string(credentials.seen[0].Body) != `{"n":1}` || string(body) != `{"n":1}` {
		t.Errorf("apply saw %q, server got %q", credentials.seen[0].Body, body)
	}
	if credentials.seen[0].Header.Get("Authorization") != "" {
		t.Errorf("a key-only operation got a bearer token")
	}
}

func TestA401RefreshesOnceAndRetriesOnce(t *testing.T) {
	credentials := &tokens{version: 1}
	if _, err := Call[map[string]any](context.Background(), serveFor(t, credentials, accepts("synthetic-access-2"), nil), getItem, Input{Path: []any{1}}); err != nil {
		t.Fatal(err)
	}
	if credentials.refreshes != 1 {
		t.Errorf("refreshed %d times", credentials.refreshes)
	}

	stale := &tokens{version: 1}
	_, err := Call[map[string]any](context.Background(), serveFor(t, stale, accepts("never"), nil), getItem, Input{Path: []any{1}})
	var failure *Error
	if !errors.As(err, &failure) || failure.Status != http.StatusUnauthorized {
		t.Fatalf("error is %v", err)
	}
	if stale.refreshes != 1 || len(stale.seen) != 2 {
		t.Errorf("refreshed %d times over %d attempts", stale.refreshes, len(stale.seen))
	}
}

func TestA401IsFinalWhenTheCredentialsCannotRefresh(t *testing.T) {
	var attempts atomic.Int32
	static := StaticCredentials{Header: http.Header{"Authorization": {"Basic synthetic"}}, Values: []string{"synthetic"}}
	transport := serveFor(t, static, func(w http.ResponseWriter, r *http.Request) {
		attempts.Add(1)
		w.WriteHeader(http.StatusUnauthorized)
	}, nil)
	if _, err := Call[any](context.Background(), transport, getItem, Input{Path: []any{1}}); err == nil {
		t.Fatal("no error")
	}
	if attempts.Load() != 1 {
		t.Errorf("sent %d attempts", attempts.Load())
	}
}

func TestConcurrentCallsShareOneRefresh(t *testing.T) {
	credentials := &tokens{version: 1}
	transport := serveFor(t, credentials, accepts("synthetic-access-2"), nil)
	var group sync.WaitGroup
	errs := make([]error, 4)
	for index := range errs {
		group.Add(1)
		go func() {
			defer group.Done()
			_, errs[index] = Call[map[string]any](context.Background(), transport, getItem, Input{Path: []any{index}})
		}()
	}
	group.Wait()
	if err := errors.Join(errs...); err != nil {
		t.Fatal(err)
	}
	if credentials.refreshes != 1 {
		t.Errorf("refreshed %d times", credentials.refreshes)
	}
}

func TestEverySecretIsKeptOutOfErrorsAndLogs(t *testing.T) {
	credentials := &tokens{version: 1}
	var logs strings.Builder
	logger := slog.New(slog.NewTextHandler(&logs, &slog.HandlerOptions{Level: slog.LevelDebug}))
	body := "bad " + syntheticKey + ":" + syntheticShared + " and synthetic-access-1 and synthetic-refresh"
	transport := serveFor(t, credentials, func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusBadRequest)
		_, _ = w.Write([]byte(body))
	}, logger)
	_, err := Call[any](context.Background(), transport, getItem, Input{Path: []any{syntheticShared + "/x y"}})
	var failure *Error
	if !errors.As(err, &failure) {
		t.Fatalf("error is %v", err)
	}
	if failure.RawBody != "bad ***:*** and *** and ***" {
		t.Errorf("raw body is %q", failure.RawBody)
	}
	output := err.Error() + failure.RawBody + logs.String()
	for _, secret := range credentials.Secrets() {
		if strings.Contains(output, secret) {
			t.Errorf("output shows %q: %s", secret, output)
		}
	}
}

func TestA401OnAnOperationWithoutSecurityDoesNotRefresh(t *testing.T) {
	credentials := &tokens{version: 1}
	transport := serveFor(t, credentials, accepts("never"), nil)
	operation := &Operation{ID: "token", Method: "POST", Path: "/token"}
	if _, err := Call[any](context.Background(), transport, operation, Input{}); err == nil {
		t.Fatal("no error")
	}
	if credentials.refreshes != 0 || len(credentials.seen) != 1 {
		t.Errorf("refreshed %d times over %d attempts", credentials.refreshes, len(credentials.seen))
	}
}
