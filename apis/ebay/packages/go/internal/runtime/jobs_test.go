package runtime

import (
	"context"
	"errors"
	"io"
	"log/slog"
	"net/http"
	"slices"
	"strings"
	"sync"
	"testing"
	"time"
)

const (
	jobSecret = "synthetic-secret"
	jobBase   = "https://api.example.test"
	report    = "id;error\n1;none\n"
)

// A synthetic start and status pair. Only the status operation is polled.
var (
	startImport = &Operation{ID: "startImport", Method: "POST", Path: "/imports"}
	getImport   = &Operation{
		ID: "getImport", Method: "GET", Path: "/imports/{import_id}", PathParams: []string{"import_id"}, ReturnsJSON: true,
		Job: &Job{State: "progress.state", Done: []string{"COMPLETE"}, Failed: []string{"FAILED"}},
	}
)

type importStatus struct {
	ImportID int64 `json:"import_id"`
	Progress struct {
		State any `json:"state"`
	} `json:"progress"`
}

type roundTripFunc func(*http.Request) (*http.Response, error)

func (f roundTripFunc) RoundTrip(request *http.Request) (*http.Response, error) { return f(request) }

func reply(status int, header http.Header, body string) *http.Response {
	if header == nil {
		header = http.Header{}
	}
	return &http.Response{StatusCode: status, Header: header, Body: io.NopCloser(strings.NewReader(body))}
}

func jobStatus(state string) *http.Response {
	return reply(http.StatusOK, http.Header{"Content-Type": {"application/json"}}, `{"import_id":7,"progress":{"state":`+state+`}}`)
}

func csv(*http.Request) *http.Response {
	return reply(http.StatusOK, http.Header{"Content-Type": {"text/csv"}}, report)
}

func redirect(location string) *http.Response {
	return reply(http.StatusFound, http.Header{"Location": {location}}, "")
}

// jobTransport answers every request with handler, without a network, and records what was sent.
func jobTransport(t *testing.T, handler func(*http.Request) *http.Response) (*Transport, func() []*http.Request) {
	t.Helper()
	var lock sync.Mutex
	var sent []*http.Request
	transport := mustTransport(t, Settings{
		BaseURL:     jobBase,
		Credentials: StaticCredentials{Header: http.Header{"Authorization": {jobSecret}}, Values: []string{jobSecret}},
		Headers:     http.Header{"User-Agent": {"test"}},
		ToError: func(context ErrorContext) *Error {
			return &Error{Kind: KindAPI, Message: "failed", Status: context.Status, RetryAfter: context.Header.Get("Retry-After")}
		},
		HTTPTransport: roundTripFunc(func(request *http.Request) (*http.Response, error) {
			lock.Lock()
			sent = append(sent, request)
			lock.Unlock()
			return handler(request), nil
		}),
		Timeout:       time.Second,
		MaxRetries:    2,
		RateLimitWait: time.Millisecond,
		MaxRetryWait:  time.Second,
	})
	return transport, func() []*http.Request {
		lock.Lock()
		defer lock.Unlock()
		return slices.Clone(sent)
	}
}

func replies(responses ...*http.Response) func(*http.Request) *http.Response {
	var lock sync.Mutex
	return func(*http.Request) *http.Response {
		lock.Lock()
		defer lock.Unlock()
		next := responses[0]
		responses = responses[1:]
		return next
	}
}

var quick = &WaitOptions{Interval: time.Millisecond, Timeout: 5 * time.Second}

func wait(transport *Transport, operation *Operation, options *WaitOptions) (*importStatus, error) {
	return Wait[*importStatus](context.Background(), transport, operation, Input{Path: []any{int64(7)}}, options)
}

func TestWaitPollsUntilTheJobIsDoneAndReturnsItsLastStatus(t *testing.T) {
	transport, sent := jobTransport(t, replies(jobStatus(`"WAITING"`), jobStatus(`"RUNNING"`), jobStatus(`"COMPLETE"`)))
	result, err := wait(transport, getImport, quick)
	if err != nil || result.Progress.State != "COMPLETE" {
		t.Fatalf("result is %+v, %v", result, err)
	}
	requests := sent()
	if len(requests) != 3 {
		t.Fatalf("sent %d requests", len(requests))
	}
	for _, request := range requests {
		if got := request.URL.String(); got != jobBase+"/imports/7" {
			t.Errorf("polled %s", got)
		}
	}
}

func TestAFailedJobReturnsItsStatusRatherThanAnError(t *testing.T) {
	transport, sent := jobTransport(t, replies(jobStatus(`"RUNNING"`), jobStatus(`"FAILED"`)))
	result, err := wait(transport, getImport, quick)
	if err != nil || result.Progress.State != "FAILED" || len(sent()) != 2 {
		t.Fatalf("result is %+v, %v after %d requests", result, err, len(sent()))
	}
}

func TestAJobThatOutlastsTheDeadlineIsAJobTimeoutWithItsLastStatus(t *testing.T) {
	transport, sent := jobTransport(t, func(*http.Request) *http.Response { return jobStatus(`"RUNNING"`) })
	result, err := wait(transport, getImport, &WaitOptions{Interval: 20 * time.Millisecond, Timeout: 50 * time.Millisecond})
	var failure *Error
	if !errors.Is(err, &Error{Kind: KindJobTimeout}) || !errors.As(err, &failure) {
		t.Fatalf("error is %v", err)
	}
	last, ok := failure.Result.(*importStatus)
	if !ok || last.Progress.State != "RUNNING" || result != last {
		t.Fatalf("result is %+v and %+v", failure.Result, result)
	}
	if len(sent()) < 2 {
		t.Errorf("sent %d requests", len(sent()))
	}
}

func TestCancellingAWaitStopsItDuringTheInterval(t *testing.T) {
	transport, sent := jobTransport(t, func(*http.Request) *http.Response { return jobStatus(`"RUNNING"`) })
	ctx, cancel := context.WithCancel(context.Background())
	time.AfterFunc(20*time.Millisecond, cancel)
	started := time.Now()
	_, err := Wait[*importStatus](ctx, transport, getImport, Input{Path: []any{int64(7)}}, &WaitOptions{Interval: time.Minute, Timeout: time.Hour})
	if !errors.Is(err, context.Canceled) || time.Since(started) > 5*time.Second {
		t.Fatalf("error is %v after %s", err, time.Since(started))
	}
	if len(sent()) != 1 {
		t.Errorf("sent %d requests", len(sent()))
	}
}

func TestARateLimitWhilePollingIsRetried(t *testing.T) {
	limited := reply(http.StatusTooManyRequests, http.Header{"Retry-After": {"0"}}, "")
	transport, sent := jobTransport(t, replies(jobStatus(`"RUNNING"`), limited, jobStatus(`"COMPLETE"`)))
	result, err := wait(transport, getImport, quick)
	if err != nil || result.Progress.State != "COMPLETE" || len(sent()) != 3 {
		t.Fatalf("result is %+v, %v after %d requests", result, err, len(sent()))
	}
}

func TestAStateThatIsNotAStringIsADecodeError(t *testing.T) {
	transport, _ := jobTransport(t, func(*http.Request) *http.Response { return jobStatus("3") })
	_, err := wait(transport, getImport, quick)
	if !errors.Is(err, &Error{Kind: KindDecode}) || !strings.Contains(err.Error(), "progress.state") {
		t.Fatalf("error is %v", err)
	}
}

func TestWaitRefusesNegativeTimesAndAnOperationWithoutAJobBeforeSending(t *testing.T) {
	transport, sent := jobTransport(t, func(*http.Request) *http.Response { return jobStatus(`"COMPLETE"`) })
	for _, check := range []struct {
		operation *Operation
		options   *WaitOptions
		message   string
	}{
		{getImport, &WaitOptions{Interval: -time.Second}, "interval"},
		{getImport, &WaitOptions{Timeout: -time.Second}, "timeout"},
		{startImport, nil, "does not report a job"},
	} {
		_, err := wait(transport, check.operation, check.options)
		var failure *Error
		if err == nil || errors.As(err, &failure) || !strings.Contains(err.Error(), check.message) {
			t.Errorf("error is %v, want one naming %q", err, check.message)
		}
	}
	if len(sent()) != 0 {
		t.Errorf("sent %d requests", len(sent()))
	}
}

func readAll(t *testing.T, download *Download) string {
	t.Helper()
	defer download.Body.Close()
	body, err := io.ReadAll(download.Body)
	if err != nil {
		t.Fatal(err)
	}
	return string(body)
}

func authorizations(requests []*http.Request) []string {
	var sent []string
	for _, request := range requests {
		sent = append(sent, request.Header.Get("Authorization"))
	}
	return sent
}

func TestADownloadURLOnTheBaseOriginSendsCredentials(t *testing.T) {
	var logs strings.Builder
	transport, sent := jobTransport(t, csv)
	transport.settings.Logger = slog.New(slog.NewTextHandler(&logs, &slog.HandlerOptions{Level: slog.LevelDebug}))
	download, err := DownloadURL(context.Background(), transport, jobBase+"/files/report.csv?sig=synthetic-signature")
	if err != nil {
		t.Fatal(err)
	}
	if body := readAll(t, download); body != report || download.ContentType != "text/csv" {
		t.Fatalf("download is %q %q", download.ContentType, body)
	}
	request := sent()[0]
	if request.Header.Get("Authorization") != jobSecret || request.Header.Get("Accept-Encoding") != "identity" {
		t.Errorf("sent %v", request.Header)
	}
	if strings.Contains(logs.String(), "synthetic-signature") || !strings.Contains(logs.String(), jobBase+"/files/report.csv") {
		t.Errorf("logged %s", logs.String())
	}
}

func TestADownloadURLOnAnotherSchemeHostOrPortSendsNoCredentials(t *testing.T) {
	for _, address := range []string{
		"https://files.example.test/report.csv",
		"http://api.example.test/report.csv",
		"https://api.example.test:8443/report.csv",
	} {
		transport, sent := jobTransport(t, csv)
		download, err := DownloadURL(context.Background(), transport, address)
		if err != nil {
			t.Fatal(err)
		}
		if body := readAll(t, download); body != report {
			t.Errorf("%s: body is %q", address, body)
		}
		if got := sent()[0].Header.Values("Authorization"); len(got) != 0 {
			t.Errorf("%s: sent Authorization %q", address, got)
		}
	}
}

func TestTheBaseOriginMatchesTheDefaultPortAndAnyCase(t *testing.T) {
	transport, sent := jobTransport(t, csv)
	download, err := DownloadURL(context.Background(), transport, "https://API.example.test:443/report.csv")
	if err != nil {
		t.Fatal(err)
	}
	readAll(t, download)
	if got := sent()[0].Header.Get("Authorization"); got != jobSecret {
		t.Errorf("sent Authorization %q", got)
	}
}

func TestARedirectToAnotherOriginDropsCredentialsForTheRestOfTheChain(t *testing.T) {
	transport, sent := jobTransport(t, func(request *http.Request) *http.Response {
		switch {
		case request.URL.Host == "api.example.test" && request.URL.Path == "/files/1":
			return redirect("https://files.example.test/signed/1")
		case request.URL.Host == "files.example.test":
			return redirect(jobBase + "/files/final")
		default:
			return csv(request)
		}
	})
	download, err := DownloadURL(context.Background(), transport, jobBase+"/files/1")
	if err != nil {
		t.Fatal(err)
	}
	if body := readAll(t, download); body != report {
		t.Fatalf("body is %q", body)
	}
	var urls []string
	for _, request := range sent() {
		urls = append(urls, request.URL.String())
	}
	if want := []string{jobBase + "/files/1", "https://files.example.test/signed/1", jobBase + "/files/final"}; !slices.Equal(urls, want) {
		t.Errorf("sent %q", urls)
	}
	if got := authorizations(sent()); !slices.Equal(got, []string{jobSecret, "", ""}) {
		t.Errorf("sent Authorization %q", got)
	}
}

func TestARelativeRedirectOnTheBaseOriginKeepsCredentials(t *testing.T) {
	transport, sent := jobTransport(t, func(request *http.Request) *http.Response {
		if request.URL.Path == "/files/1" {
			return redirect("/files/2")
		}
		return csv(request)
	})
	download, err := DownloadURL(context.Background(), transport, jobBase+"/files/1")
	if err != nil {
		t.Fatal(err)
	}
	readAll(t, download)
	if got := authorizations(sent()); !slices.Equal(got, []string{jobSecret, jobSecret}) || sent()[1].URL.String() != jobBase+"/files/2" {
		t.Errorf("sent Authorization %q to %v", got, sent()[1].URL)
	}
}

func TestADownloadURLRefusesARelativeOrNonHTTPURLBeforeSending(t *testing.T) {
	transport, sent := jobTransport(t, csv)
	for _, address := range []string{"/files/1", "ftp://api.example.test/files/1", "https:///files/1"} {
		_, err := DownloadURL(context.Background(), transport, address)
		var failure *Error
		if err == nil || errors.As(err, &failure) || !strings.Contains(err.Error(), "absolute") {
			t.Errorf("%s: error is %v", address, err)
		}
	}
	if len(sent()) != 0 {
		t.Errorf("sent %d requests", len(sent()))
	}
}

func TestADownloadURLStopsAfterFiveRedirects(t *testing.T) {
	transport, sent := jobTransport(t, func(request *http.Request) *http.Response { return redirect(request.URL.String()) })
	_, err := DownloadURL(context.Background(), transport, jobBase+"/files/1")
	if !errors.Is(err, &Error{Kind: KindDecode}) || !strings.Contains(err.Error(), "redirects") {
		t.Fatalf("error is %v", err)
	}
	if len(sent()) != 6 {
		t.Errorf("sent %d requests", len(sent()))
	}
}

func TestARedirectWithoutAUsableLocationIsADecodeError(t *testing.T) {
	for _, location := range []string{"", "ftp://files.example.test/1"} {
		transport, _ := jobTransport(t, func(*http.Request) *http.Response { return redirect(location) })
		_, err := DownloadURL(context.Background(), transport, jobBase+"/files/1")
		if !errors.Is(err, &Error{Kind: KindDecode}) {
			t.Errorf("%q: error is %v", location, err)
		}
	}
}
