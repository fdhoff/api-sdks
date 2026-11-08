package backmarketseller_test

import (
	"bytes"
	"compress/gzip"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"log/slog"
	"math"
	"mime"
	"mime/multipart"
	"net"
	"net/http"
	"net/http/httptest"
	"strings"
	"testing"
	"time"

	bm "github.com/fdhoff/backmarket-seller-sdk/apis/backmarket/packages/go/backmarketseller"
)

const token = "synthetic-test-token"

func server(t *testing.T, handler http.HandlerFunc, options ...bm.Option) *bm.Client {
	t.Helper()
	mock := httptest.NewServer(handler)
	t.Cleanup(mock.Close)
	defaults := []bm.Option{
		bm.WithBaseURL(mock.URL),
		bm.WithRetryBaseDelay(time.Millisecond),
		bm.WithRateLimitWait(time.Millisecond),
	}
	client, err := bm.NewClient(token, "BM-Example-Test;test@example.com", "en-us", append(defaults, options...)...)
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

func encode(t *testing.T, value any) string {
	t.Helper()
	encoded, err := json.Marshal(value)
	if err != nil {
		t.Fatal(err)
	}
	return string(encoded)
}

func TestNewClientValidatesItsArguments(t *testing.T) {
	cases := map[string]struct {
		token, agent string
		options      []bm.Option
	}{
		"no token":      {"", "agent", []bm.Option{bm.WithRegion(bm.RegionEU)}},
		"no user agent": {"token", "", []bm.Option{bm.WithRegion(bm.RegionEU)}},
		"no server":     {"token", "agent", nil},
		"two servers":   {"token", "agent", []bm.Option{bm.WithRegion(bm.RegionEU), bm.WithBaseURL("http://127.0.0.1")}},
		"bad region":    {"token", "agent", []bm.Option{bm.WithRegion("moon")}},
		"relative url":  {"token", "agent", []bm.Option{bm.WithBaseURL("/relative")}},
	}
	for name, item := range cases {
		t.Run(name, func(t *testing.T) {
			if _, err := bm.NewClient(item.token, item.agent, "en-us", item.options...); err == nil {
				t.Fatal("expected an error")
			}
		})
	}
}

func TestPrintingAClientDoesNotShowTheToken(t *testing.T) {
	client := server(t, func(http.ResponseWriter, *http.Request) {})
	for _, format := range []string{"%v", "%+v", "%#v"} {
		if shown := fmt.Sprintf(format, client); strings.Contains(shown, token) {
			t.Errorf("%s shows the token: %s", format, shown)
		}
	}
}

func TestSendsTheTokenVerbatimAndTheHeaders(t *testing.T) {
	client := server(t, func(w http.ResponseWriter, r *http.Request) {
		if got := r.Header.Get("Authorization"); got != "Basic "+token {
			t.Errorf("Authorization is %q", got)
		}
		if got := r.Header.Get("Accept-Language"); got != "en-us" {
			t.Errorf("Accept-Language is %q", got)
		}
		replyJSON(w, 200, `{"order_id": 1}`)
	})
	order, err := client.Orders.Get(context.Background(), 1)
	if err != nil {
		t.Fatal(err)
	}
	if order.OrderID == nil || *order.OrderID != 1 {
		t.Errorf("order is %+v", order)
	}
}

func TestDecodingKeepsWhatDoesNotFit(t *testing.T) {
	client := server(t, func(w http.ResponseWriter, _ *http.Request) {
		replyJSON(w, 200, `{"order_id": "not a number", "delivery_note": null, "tracking_number": "T1", "unknown": {"a": 1}}`)
	})
	order, err := client.Orders.Get(context.Background(), 1)
	if err != nil {
		t.Fatal(err)
	}
	if order.OrderID != nil {
		t.Errorf("OrderID is %d", *order.OrderID)
	}
	if got := string(order.Extra["order_id"]); got != `"not a number"` {
		t.Errorf("Extra[order_id] is %s", got)
	}
	if got := string(order.Extra["unknown"]); got != `{"a": 1}` {
		t.Errorf("Extra[unknown] is %s", got)
	}
	var wire map[string]any
	if err := json.Unmarshal([]byte(encode(t, order)), &wire); err != nil {
		t.Fatal(err)
	}
	if value, found := wire["delivery_note"]; !found || value != nil {
		t.Errorf("a null was not kept: %v", wire)
	}
	if wire["tracking_number"] != "T1" || wire["order_id"] != "not a number" {
		t.Errorf("round trip lost a value: %v", wire)
	}
}

func TestNumbersSurviveDecodingAndEncodingExactly(t *testing.T) {
	var listing bm.BuybackOrderListing
	if err := json.Unmarshal([]byte(`{"productId": 16777217}`), &listing); err != nil {
		t.Fatal(err)
	}
	if listing.ProductID == nil || *listing.ProductID != 16777217 {
		t.Errorf("ProductID is %v", listing.ProductID)
	}
	if got := encode(t, listing); got != `{"productId":16777217}` {
		t.Errorf("encoded %s", got)
	}

	var refund bm.PostRefundCreateRequest
	if err := json.Unmarshal([]byte(`{"amount": 262144.01}`), &refund); err != nil {
		t.Fatal(err)
	}
	if refund.Amount == nil || *refund.Amount != 262144.01 {
		t.Errorf("Amount is %v", refund.Amount)
	}
	if got := encode(t, refund); got != `{"amount":262144.01}` {
		t.Errorf("encoded %s", got)
	}
}

func TestAnOptionalReferenceIsTyped(t *testing.T) {
	var competitor bm.Competitor
	if err := json.Unmarshal([]byte(`{"min_price": {"amount": "1.00", "currency": "EUR"}, "market": "FR"}`), &competitor); err != nil {
		t.Fatal(err)
	}
	if competitor.MinPrice == nil || *competitor.MinPrice.Amount != "1.00" {
		t.Errorf("MinPrice is %v", competitor.MinPrice)
	}
	if competitor.Market == nil || *competitor.Market != bm.MarketCodeFr {
		t.Errorf("Market is %v", competitor.Market)
	}
}

func TestAFieldSetAfterDecodingWinsOverExtra(t *testing.T) {
	var order bm.Order
	if err := json.Unmarshal([]byte(`{"delivery_note": null}`), &order); err != nil {
		t.Fatal(err)
	}
	order.DeliveryNote = bm.Ptr("Set later")
	if got := encode(t, order); got != `{"delivery_note":"Set later"}` {
		t.Errorf("encoded %s", got)
	}
}

func TestRequestsSendOnlyTheFieldsThatAreSet(t *testing.T) {
	got := encode(t, bm.ListingUpdate{Quantity: 0, ShippingDelay1: bm.Ptr[int64](0)})
	if got != `{"quantity":0,"shipping_delay_1":0}` {
		t.Errorf("encoded %s", got)
	}
}

func TestAResponseOfTheWrongShapeIsADecodeError(t *testing.T) {
	client := server(t, func(w http.ResponseWriter, _ *http.Request) {
		replyJSON(w, 200, `["not an object"]`)
	})
	_, err := client.Orders.Get(context.Background(), 1)
	var failure *bm.APIError
	if !errors.Is(err, bm.ErrDecode) || !errors.As(err, &failure) {
		t.Fatalf("error is %v", err)
	}
	if failure.Status != 200 || failure.RawBody != `["not an object"]` {
		t.Errorf("failure is %+v", failure)
	}
}

func TestABodyThatCannotBeEncodedFailsBeforeSending(t *testing.T) {
	sent := false
	client := server(t, func(w http.ResponseWriter, _ *http.Request) {
		sent = true
		replyJSON(w, 200, `{}`)
	})
	_, err := client.Listings.Update(context.Background(), "1", &bm.ListingUpdate{Price: math.NaN()})
	var failure *bm.APIError
	var unsupported *json.UnsupportedValueError
	if errors.As(err, &failure) || !errors.As(err, &unsupported) {
		t.Errorf("error is %v", err)
	}
	if sent {
		t.Error("the request was sent")
	}
}

func TestErrorsMatchTheirSentinels(t *testing.T) {
	cases := []struct {
		name     string
		status   int
		cfRay    string
		body     string
		matches  error
		excludes error
	}{
		{"not found", 404, "", "", bm.ErrNotFound, bm.ErrPermission},
		{"waf", 403, "ray-1", "<html>", bm.ErrWAFBlocked, bm.ErrBotChallenge},
		{"waf is a permission error", 403, "ray-1", "<html>", bm.ErrPermission, bm.ErrNotFound},
		{"bot", 403, "", `{"errors":[{"code":"bot-need-challenge"}]}`, bm.ErrBotChallenge, bm.ErrWAFBlocked},
		{"bot is a permission error", 403, "", `{"errors":[{"code":"bot-need-challenge"}]}`, bm.ErrPermission, bm.ErrServer},
		{"unmapped", 418, "", "", bm.ErrAPI, bm.ErrServer},
	}
	for _, item := range cases {
		t.Run(item.name, func(t *testing.T) {
			client := server(t, func(w http.ResponseWriter, _ *http.Request) {
				if item.cfRay != "" {
					w.Header().Set("cf-ray", item.cfRay)
				}
				w.WriteHeader(item.status)
				fmt.Fprint(w, item.body)
			})
			_, err := client.Orders.Get(context.Background(), 1)
			if !errors.Is(err, item.matches) || errors.Is(err, item.excludes) {
				t.Errorf("error is %v", err)
			}
		})
	}
}

func TestANumericErrorCodeIsKept(t *testing.T) {
	client := server(t, func(w http.ResponseWriter, _ *http.Request) {
		replyJSON(w, 400, `{"error": {"code": 12345678901}}`)
	})
	_, err := client.Orders.Get(context.Background(), 1)
	var failure *bm.APIError
	if !errors.As(err, &failure) || failure.Code != "12345678901" {
		t.Errorf("error is %+v", err)
	}
}

func TestTheTokenIsRemovedFromErrorsAndLogs(t *testing.T) {
	var logs bytes.Buffer
	logger := slog.New(slog.NewTextHandler(&logs, &slog.HandlerOptions{Level: slog.LevelDebug}))
	client := server(t, func(w http.ResponseWriter, _ *http.Request) {
		w.WriteHeader(400)
		fmt.Fprint(w, "Rejected "+token)
	}, bm.WithLogger(logger))
	_, err := client.Buyback.GetOrder(context.Background(), token)
	var failure *bm.APIError
	if !errors.As(err, &failure) {
		t.Fatalf("error is %v", err)
	}
	if strings.Contains(failure.RawBody, token) || strings.Contains(failure.Error(), token) {
		t.Errorf("failure shows the token: %+v", failure)
	}
	if logs.Len() == 0 || strings.Contains(logs.String(), token) {
		t.Errorf("logs are %q", logs.String())
	}
}

func TestAConnectionFailureShowsItsCauseWithoutTheToken(t *testing.T) {
	closed := httptest.NewServer(http.NotFoundHandler())
	closed.Close()
	client := server(t, http.NotFound, bm.WithBaseURL(closed.URL), bm.WithMaxRetries(0))
	_, err := client.Buyback.GetOrder(context.Background(), token)
	var dial *net.OpError
	if !errors.Is(err, bm.ErrConnection) || !errors.As(err, &dial) {
		t.Fatalf("error is %v", err)
	}
	message := err.Error()
	if !strings.HasPrefix(message, "the connection failed: ") || !strings.Contains(message, dial.Error()) {
		t.Errorf("error shows %q", message)
	}
	if strings.Contains(message, token) {
		t.Errorf("error shows the token: %q", message)
	}
}

func TestARedirectIsAFailureNotFollowed(t *testing.T) {
	hits := 0
	foreign := httptest.NewServer(http.HandlerFunc(func(http.ResponseWriter, *http.Request) { hits++ }))
	defer foreign.Close()
	client := server(t, func(w http.ResponseWriter, r *http.Request) {
		http.Redirect(w, r, foreign.URL, http.StatusFound)
	})
	_, err := client.Orders.Get(context.Background(), 1)
	if !errors.Is(err, bm.ErrAPI) || hits != 0 {
		t.Errorf("error is %v after %d foreign hits", err, hits)
	}
}

func TestCancellingStopsARetryWaitAndReturnsTheContextError(t *testing.T) {
	requests := 0
	client := server(t, func(w http.ResponseWriter, _ *http.Request) {
		requests++
		w.Header().Set("Retry-After", "30")
		w.WriteHeader(429)
	})
	ctx, cancel := context.WithTimeout(context.Background(), 50*time.Millisecond)
	defer cancel()
	_, err := client.Orders.Get(ctx, 1)
	if !errors.Is(err, context.DeadlineExceeded) || requests != 1 {
		t.Errorf("error is %v after %d requests", err, requests)
	}
}

func TestACancelledContextDuringARequestIsNotRetried(t *testing.T) {
	requests := 0
	ctx, cancel := context.WithCancel(context.Background())
	release := make(chan struct{})
	defer close(release)
	client := server(t, func(http.ResponseWriter, *http.Request) {
		requests++
		cancel()
		<-release
	})
	_, err := client.Orders.Get(ctx, 1)
	if !errors.Is(err, context.Canceled) || requests != 1 {
		t.Errorf("error is %v after %d requests", err, requests)
	}
}

func TestARetryAfterAboveTheMaximumReturnsAtOnceWithTheHeader(t *testing.T) {
	for name, value := range map[string]string{
		"seconds":          "120",
		"too long for int": strings.Repeat("9", 400),
		"date":             time.Now().Add(time.Hour).UTC().Format(http.TimeFormat),
	} {
		t.Run(name, func(t *testing.T) {
			requests := 0
			client := server(t, func(w http.ResponseWriter, _ *http.Request) {
				requests++
				w.Header().Set("Retry-After", value)
				w.WriteHeader(429)
			}, bm.WithMaxRetryWait(time.Second))
			_, err := client.Orders.Get(context.Background(), 1)
			var failure *bm.APIError
			if !errors.Is(err, bm.ErrRateLimited) || !errors.As(err, &failure) {
				t.Fatalf("error is %v", err)
			}
			if failure.RetryAfter != value || requests != 1 {
				t.Errorf("RetryAfter is %q after %d requests", failure.RetryAfter, requests)
			}
		})
	}
}

func TestAFarFutureYearCountsAsAboveTheMaximum(t *testing.T) {
	requests := 0
	client := server(t, func(w http.ResponseWriter, _ *http.Request) {
		requests++
		w.Header().Set("Retry-After", "Fri, 31 Dec 9999 23:59:59 GMT")
		w.WriteHeader(429)
	})
	_, err := client.Orders.Get(context.Background(), 1)
	if !errors.Is(err, bm.ErrRateLimited) || requests != 1 {
		t.Errorf("error is %v after %d requests", err, requests)
	}
}

func TestTheMaximumDoesNotApplyToTheRateLimitWait(t *testing.T) {
	requests := 0
	client := server(t, func(w http.ResponseWriter, _ *http.Request) {
		requests++
		if requests == 1 {
			w.WriteHeader(429)
			return
		}
		replyJSON(w, 200, `{"order_id": 1}`)
	}, bm.WithRateLimitWait(20*time.Millisecond), bm.WithMaxRetryWait(time.Millisecond))
	if _, err := client.Orders.Get(context.Background(), 1); err != nil {
		t.Fatal(err)
	}
}

func TestACorruptCompressedBody(t *testing.T) {
	cases := []struct {
		name     string
		status   int
		matches  error
		requests int
	}{
		{"success is decode", 200, bm.ErrDecode, 1},
		{"failure keeps its status and retries", 502, bm.ErrServer, 2},
	}
	for _, item := range cases {
		t.Run(item.name, func(t *testing.T) {
			requests := 0
			client := server(t, func(w http.ResponseWriter, _ *http.Request) {
				requests++
				w.Header().Set("Content-Encoding", "gzip")
				w.WriteHeader(item.status)
				fmt.Fprint(w, "not gzip")
			}, bm.WithMaxRetries(1))
			_, err := client.Orders.Get(context.Background(), 1)
			if !errors.Is(err, item.matches) || requests != item.requests {
				t.Errorf("error is %v after %d requests", err, requests)
			}
		})
	}
}

func TestAGzippedBodyIsDecompressed(t *testing.T) {
	client := server(t, func(w http.ResponseWriter, _ *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		w.Header().Set("Content-Encoding", "gzip")
		compressed := gzip.NewWriter(w)
		fmt.Fprint(compressed, `{"order_id": 1}`)
		compressed.Close()
	})
	order, err := client.Orders.Get(context.Background(), 1)
	if err != nil {
		t.Fatal(err)
	}
	if *order.OrderID != 1 {
		t.Errorf("order is %+v", order)
	}
}

func TestTheTimeoutCoversABodyThatKeepsTrickling(t *testing.T) {
	release := make(chan struct{})
	defer close(release)
	client := server(t, func(w http.ResponseWriter, _ *http.Request) {
		w.Header().Set("Content-Type", "application/json")
		for range 100 {
			fmt.Fprint(w, " ")
			w.(http.Flusher).Flush()
			select {
			case <-release:
				return
			case <-time.After(20 * time.Millisecond):
			}
		}
	}, bm.WithTimeout(100*time.Millisecond), bm.WithMaxRetries(0))
	_, err := client.Orders.Get(context.Background(), 1)
	if !errors.Is(err, bm.ErrTimeout) {
		t.Errorf("error is %v", err)
	}
}

func TestIterationFollowsThePositionOnTheConfiguredServer(t *testing.T) {
	var queries []string
	client := server(t, func(w http.ResponseWriter, r *http.Request) {
		queries = append(queries, r.URL.RawQuery)
		if r.URL.Query().Get("page") == "" {
			replyJSON(w, 200, `{"next": "https://foreign.invalid/x?page=2", "results": [{"order_id": 1}]}`)
			return
		}
		replyJSON(w, 200, `{"next": null, "results": [{"order_id": 2}]}`)
	})
	var ids []int64
	for order, err := range client.Orders.Iter(context.Background(), &bm.OrdersListParams{PageSize: bm.Ptr[int64](1)}) {
		if err != nil {
			t.Fatal(err)
		}
		ids = append(ids, *order.OrderID)
	}
	if fmt.Sprint(ids) != "[1 2]" || fmt.Sprint(queries) != "[page-size=1 page=2&page-size=1]" {
		t.Errorf("ids %v, queries %v", ids, queries)
	}
}

func TestIterationStopsWhenTheCallerBreaks(t *testing.T) {
	requests := 0
	client := server(t, func(w http.ResponseWriter, _ *http.Request) {
		requests++
		replyJSON(w, 200, `{"next": "https://foreign.invalid/x?page=2", "results": [{"order_id": 1}, {"order_id": 2}]}`)
	})
	for _, err := range client.Orders.Iter(context.Background(), nil) {
		if err != nil {
			t.Fatal(err)
		}
		break
	}
	if requests != 1 {
		t.Errorf("sent %d requests", requests)
	}
}

func TestABadNextLinkIsADecodeError(t *testing.T) {
	for name, link := range map[string]string{
		"does not advance": `"https://foreign.invalid/x"`,
		"cannot be parsed": `"http://["`,
		"not a string":     `5`,
	} {
		t.Run(name, func(t *testing.T) {
			client := server(t, func(w http.ResponseWriter, _ *http.Request) {
				replyJSON(w, 200, `{"next": `+link+`, "results": []}`)
			})
			var last error
			for _, err := range client.Orders.Iter(context.Background(), nil) {
				last = err
			}
			if !errors.Is(last, bm.ErrDecode) {
				t.Errorf("error is %v", last)
			}
		})
	}
}

func TestIterationRejectsANextLinkThatIsNotAURL(t *testing.T) {
	client := server(t, func(w http.ResponseWriter, _ *http.Request) {
		replyJSON(w, 200, `{"next": "http://[", "results": [{"order_id": 1}]}`)
	})
	var ids []int64
	var last error
	for order, err := range client.Orders.Iter(context.Background(), nil) {
		if err != nil {
			last = err
			continue
		}
		ids = append(ids, *order.OrderID)
	}
	if fmt.Sprint(ids) != "[1]" || !errors.Is(last, bm.ErrDecode) {
		t.Errorf("ids %v, error %v", ids, last)
	}
}

func TestAPageThatIsNotAnObjectIsADecodeError(t *testing.T) {
	client := server(t, func(w http.ResponseWriter, _ *http.Request) { replyJSON(w, 200, `[]`) })
	var last error
	for _, err := range client.Orders.Iter(context.Background(), nil) {
		last = err
	}
	if !errors.Is(last, bm.ErrDecode) {
		t.Errorf("error is %v", last)
	}
}

func TestFormFieldsAndFilesAreMultipart(t *testing.T) {
	parts := map[string]string{}
	var filename string
	client := server(t, func(w http.ResponseWriter, r *http.Request) {
		_, params, err := mime.ParseMediaType(r.Header.Get("Content-Type"))
		if err != nil {
			t.Error(err)
		}
		reader := multipart.NewReader(r.Body, params["boundary"])
		for {
			part, err := reader.NextPart()
			if err == io.EOF {
				break
			}
			if err != nil {
				t.Fatal(err)
			}
			content, _ := io.ReadAll(part)
			parts[part.FormName()] = string(content)
			if part.FileName() != "" {
				filename = part.FileName()
			}
		}
		replyJSON(w, 201, `{"id": 1}`)
	})
	_, err := client.Care.SendMessage(context.Background(), 1, &bm.CareSendMessageParams{
		Message:    bm.Ptr("Synthetic message"),
		Attachment: []bm.File{{Name: "note.txt", Content: []byte("Synthetic file")}},
	})
	if err != nil {
		t.Fatal(err)
	}
	if parts["message"] != "Synthetic message" || parts["attachment"] != "Synthetic file" || filename != "note.txt" {
		t.Errorf("parts are %v, file name %q", parts, filename)
	}
}

func TestFormFloatsAreNotInScientificNotation(t *testing.T) {
	for price, want := range map[float64]string{1000000: "1000000", 1234.56: "1234.56", 0.1: "0.1"} {
		var got string
		client := server(t, func(w http.ResponseWriter, r *http.Request) {
			got = r.FormValue("price")
			replyJSON(w, 200, `{}`)
		})
		err := client.Buyback.CounterOffer(context.Background(), "1", &bm.BuybackCounterOfferParams{Price: &price})
		if err != nil {
			t.Fatal(err)
		}
		if got != want {
			t.Errorf("price %v was sent as %q", price, got)
		}
	}
}

func TestPathValuesAreEscaped(t *testing.T) {
	var path string
	client := server(t, func(w http.ResponseWriter, r *http.Request) {
		path = r.URL.EscapedPath()
		replyJSON(w, 200, `{}`)
	})
	if _, err := client.Buyback.GetOrder(context.Background(), "a/b c"); err != nil {
		t.Fatal(err)
	}
	if path != "/ws/buyback/v1/orders/a%2Fb%20c" {
		t.Errorf("path is %s", path)
	}
}
