package mercurybanking_test

import (
	"bytes"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"log/slog"
	"net/http"
	"net/http/httptest"
	"os"
	"strings"
	"sync"
	"testing"
	"time"

	mercury "github.com/fdhoff/api-sdks/apis/mercury/packages/go/mercurybanking"
)

const token = "secret-token:synthetic-test-token"

type seen struct {
	method, path, query string
	header              http.Header
	body                []byte
}

// server answers every request with handler, after recording it. Both hosts point at it.
func server(t *testing.T, handler func(w http.ResponseWriter, r *http.Request, count int), options ...mercury.Option) (*mercury.Client, func() []seen) {
	t.Helper()
	var lock sync.Mutex
	var requests []seen
	mock := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		body, _ := io.ReadAll(r.Body)
		lock.Lock()
		requests = append(requests, seen{r.Method, r.URL.Path, r.URL.RawQuery, r.Header.Clone(), body})
		count := len(requests)
		lock.Unlock()
		handler(w, r, count)
	}))
	t.Cleanup(mock.Close)
	defaults := []mercury.Option{
		mercury.WithHosts(map[string]string{"api": mock.URL + "/api/v1", "vault": mock.URL + "/vault/v1"}),
		mercury.WithRetryBaseDelay(time.Millisecond),
		mercury.WithRateLimitWait(time.Millisecond),
	}
	client, err := mercury.NewClient(token, append(defaults, options...)...)
	if err != nil {
		t.Fatal(err)
	}
	return client, func() []seen {
		lock.Lock()
		defer lock.Unlock()
		return append([]seen(nil), requests...)
	}
}

func replyJSON(w http.ResponseWriter, status int, body string) {
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(status)
	fmt.Fprint(w, body)
}

func TestNewClientValidatesItsArguments(t *testing.T) {
	cases := map[string]struct {
		token   string
		options []mercury.Option
	}{
		"no token":         {"", nil},
		"bad environment":  {token, []mercury.Option{mercury.WithEnvironment("staging")}},
		"unknown host key": {token, []mercury.Option{mercury.WithHosts(map[string]string{"elsewhere": "https://example.com"})}},
	}
	for name, item := range cases {
		t.Run(name, func(t *testing.T) {
			if _, err := mercury.NewClient(item.token, item.options...); err == nil {
				t.Fatal("expected an error")
			}
		})
	}
}

func TestEnvironmentsAreACopy(t *testing.T) {
	environments := mercury.Environments()
	if environments[mercury.Production]["api"] != "https://api.mercury.com/api/v1" || environments[mercury.Sandbox]["vault"] != "https://api-sandbox.mercury.com/api/v1" {
		t.Fatalf("environments are %v", environments)
	}
	environments[mercury.Production]["api"] = "https://example.com"
	if mercury.Environments()[mercury.Production]["api"] != "https://api.mercury.com/api/v1" {
		t.Fatal("changing the copy changed the client's environments")
	}
}

func TestTheTokenIsABearerTokenAndRevealGoesToTheVault(t *testing.T) {
	client, requests := server(t, func(w http.ResponseWriter, r *http.Request, _ int) {
		if strings.HasPrefix(r.URL.Path, "/vault/") {
			replyJSON(w, 200, `{"cardNumber":"4000000000000002","cvc":"123"}`)
			return
		}
		replyJSON(w, 200, `{"accounts":[],"page":{}}`)
	}, mercury.WithUserAgent("example-app/1.0"))
	ctx := context.Background()
	if _, err := client.Accounts.List(ctx, nil); err != nil {
		t.Fatal(err)
	}
	revealed, err := client.Cards.Reveal(ctx, "00000000-0000-4000-8000-0000000ca4d1")
	if err != nil || *revealed.CardNumber != "4000000000000002" {
		t.Fatalf("reveal is %v, %v", revealed, err)
	}
	got := requests()
	if got[0].path != "/api/v1/accounts" || got[1].path != "/vault/v1/cards/00000000-0000-4000-8000-0000000ca4d1/reveal" {
		t.Fatalf("paths are %q and %q", got[0].path, got[1].path)
	}
	for _, request := range got {
		if request.header.Get("Authorization") != "Bearer "+token || request.header.Get("User-Agent") != "example-app/1.0" || request.header.Get("Accept") != "application/json" {
			t.Fatalf("headers are %v", request.header)
		}
	}
}

func TestIterFollowsNextPageUntilItIsNull(t *testing.T) {
	pages := []string{
		`{"accounts":[{"id":"a1"},{"id":"a2"}],"page":{"nextPage":"a2"}}`,
		`{"accounts":[{"id":"a3"}],"page":{"nextPage":null}}`,
	}
	client, requests := server(t, func(w http.ResponseWriter, r *http.Request, count int) {
		replyJSON(w, 200, pages[count-1])
	})
	var ids []string
	for account, err := range client.Accounts.Iter(context.Background(), &mercury.AccountsListParams{Limit: mercury.Ptr[int64](2)}) {
		if err != nil {
			t.Fatal(err)
		}
		ids = append(ids, *account.ID)
	}
	if strings.Join(ids, ",") != "a1,a2,a3" {
		t.Fatalf("ids are %v", ids)
	}
	got := requests()
	if got[0].query != "limit=2" || got[1].query != "limit=2&start_after=a2" {
		t.Fatalf("queries are %q and %q", got[0].query, got[1].query)
	}
}

func TestAMoneyMovingWriteIsRetriedWithTheSameKey(t *testing.T) {
	client, requests := server(t, func(w http.ResponseWriter, r *http.Request, count int) {
		if count == 1 {
			replyJSON(w, 503, `{}`)
			return
		}
		replyJSON(w, 200, `{"id":"t1","status":"pending"}`)
	})
	body := &mercury.PostTransactionAPIRequest{
		RecipientID:    mercury.Ptr("00000000-0000-4000-8000-00000004ec11"),
		Amount:         mercury.Ptr(12.5),
		PaymentMethod:  mercury.Ptr(mercury.PostTransactionPaymentMethodAch),
		IdempotencyKey: mercury.Ptr("synthetic-key-1"),
	}
	transaction, err := client.Accounts.SendMoney(context.Background(), "00000000-0000-4000-8000-0000000acc01", body)
	if err != nil || *transaction.ID != "t1" {
		t.Fatalf("transaction is %v, %v", transaction, err)
	}
	got := requests()
	if len(got) != 2 || !bytes.Equal(got[0].body, got[1].body) || !bytes.Contains(got[0].body, []byte(`"idempotencyKey":"synthetic-key-1"`)) {
		t.Fatalf("requests are %d: %s / %s", len(got), got[0].body, got[len(got)-1].body)
	}
}

func TestAWriteWithoutAKeyIsNotRetried(t *testing.T) {
	client, requests := server(t, func(w http.ResponseWriter, r *http.Request, _ int) {
		replyJSON(w, 503, `{}`)
	})
	ctx := context.Background()
	_, err := client.Accounts.SendMoney(ctx, "00000000-0000-4000-8000-0000000acc01", &mercury.PostTransactionAPIRequest{Amount: mercury.Ptr(1.0)})
	if !errors.Is(err, mercury.ErrServer) {
		t.Fatalf("error is %v", err)
	}
	_, err = client.Cards.Create(ctx, &mercury.CreateCardRequest{AccountID: mercury.Ptr("00000000-0000-4000-8000-0000000acc01")})
	if !errors.Is(err, mercury.ErrServer) {
		t.Fatalf("error is %v", err)
	}
	if got := len(requests()); got != 2 {
		t.Fatalf("sent %d requests, want 2", got)
	}
}

func TestErrorsAreTypedAndHideTheToken(t *testing.T) {
	statuses := map[int]error{
		400: mercury.ErrBadRequest,
		401: mercury.ErrAuthentication,
		403: mercury.ErrPermission,
		404: mercury.ErrNotFound,
		409: mercury.ErrConflict,
		422: mercury.ErrValidation,
		418: mercury.ErrAPI,
	}
	for status, want := range statuses {
		t.Run(fmt.Sprint(status), func(t *testing.T) {
			client, _ := server(t, func(w http.ResponseWriter, r *http.Request, _ int) {
				replyJSON(w, status, `{"echo":"`+r.Header.Get("Authorization")+`"}`)
			})
			_, err := client.Recipients.Get(context.Background(), "00000000-0000-4000-8000-00000004ec11")
			var failure *mercury.APIError
			if !errors.Is(err, want) || !errors.As(err, &failure) || failure.Status != status {
				t.Fatalf("error is %v", err)
			}
			if strings.Contains(failure.RawBody, token) || strings.Contains(err.Error(), token) || !strings.Contains(failure.RawBody, "echo") {
				t.Fatalf("raw body is %q", failure.RawBody)
			}
		})
	}
}

func TestLogsHoldNeitherTheTokenNorTheCardNumber(t *testing.T) {
	var logs bytes.Buffer
	client, _ := server(t, func(w http.ResponseWriter, r *http.Request, _ int) {
		replyJSON(w, 200, `{"cardNumber":"4000000000000002","cvc":"123"}`)
	}, mercury.WithLogger(slog.New(slog.NewTextHandler(&logs, &slog.HandlerOptions{Level: slog.LevelDebug}))))
	if _, err := client.Cards.Reveal(context.Background(), "00000000-0000-4000-8000-0000000ca4d1"); err != nil {
		t.Fatal(err)
	}
	if logs.Len() == 0 || strings.Contains(logs.String(), token) || strings.Contains(logs.String(), "4000000000000002") {
		t.Fatalf("logs are %q", logs.String())
	}
}

func TestADownloadAsksForAPDF(t *testing.T) {
	pdf := []byte("%PDF-1.4\n\xff\xfe")
	client, requests := server(t, func(w http.ResponseWriter, r *http.Request, _ int) {
		w.Header().Set("Content-Type", "application/pdf")
		_, _ = w.Write(pdf)
	})
	download, err := client.Invoices.DownloadPDF(context.Background(), "00000000-0000-4000-8000-000000001a41")
	if err != nil {
		t.Fatal(err)
	}
	defer download.Body.Close()
	body, err := io.ReadAll(download.Body)
	if err != nil || !bytes.Equal(body, pdf) || download.ContentType != "application/pdf" {
		t.Fatalf("download is %q %q, %v", download.ContentType, body, err)
	}
	if got := requests()[0].header.Get("Accept"); got != "application/pdf" {
		t.Fatalf("Accept is %q", got)
	}
}

type webhookCase struct {
	Name      string   `json:"name"`
	Header    string   `json:"header"`
	Body      string   `json:"body"`
	Now       int64    `json:"now"`
	Tolerance *float64 `json:"tolerance"`
	Error     *string  `json:"error"`
}

func TestWebhookVectors(t *testing.T) {
	raw, err := os.ReadFile("../../../conformance/webhooks/mercury-signature.json")
	if err != nil {
		t.Fatal(err)
	}
	var vectors struct {
		HeaderName string        `json:"header_name"`
		Secret     string        `json:"secret"`
		Cases      []webhookCase `json:"cases"`
	}
	if err := json.Unmarshal(raw, &vectors); err != nil {
		t.Fatal(err)
	}
	if vectors.HeaderName != mercury.SignatureHeader {
		t.Fatalf("the vectors use %q", vectors.HeaderName)
	}
	reasons := map[string]error{
		"malformed_header":  mercury.ErrWebhookMalformedHeader,
		"too_old":           mercury.ErrWebhookTooOld,
		"bad_signature":     mercury.ErrWebhookBadSignature,
		"invalid_tolerance": mercury.ErrWebhookInvalidTolerance,
	}
	for _, c := range vectors.Cases {
		t.Run(c.Name, func(t *testing.T) {
			options := []mercury.WebhookOption{mercury.WithWebhookNow(time.Unix(c.Now, 0))}
			if c.Tolerance != nil {
				options = append(options, mercury.WithWebhookTolerance(time.Duration(*c.Tolerance*float64(time.Second))))
			}
			err := mercury.VerifyWebhook([]byte(c.Body), c.Header, vectors.Secret, options...)
			if c.Error == nil {
				if err != nil {
					t.Fatalf("got %v, want no error", err)
				}
				return
			}
			if !errors.Is(err, reasons[*c.Error]) {
				t.Fatalf("got %v, want %s", err, *c.Error)
			}
		})
	}
}
