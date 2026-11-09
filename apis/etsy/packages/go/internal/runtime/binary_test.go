package runtime

import (
	"bytes"
	"context"
	"errors"
	"io"
	"net/http"
	"net/http/httptest"
	"sync"
	"testing"
	"time"
)

var (
	downloadFile = &Operation{ID: "download-file", Method: "GET", Path: "/download", BinaryResponse: true}
	uploadFile   = &Operation{ID: "upload-file", Method: "POST", Path: "/upload", RawBody: "application/octet-stream"}
	getReport    = &Operation{ID: "get-report", Method: "GET", Path: "/report"}
	notUTF8      = []byte{0x25, 0x50, 0x44, 0x46, 0x00, 0xff, 0xfe, 0x80, 0x0a, 0xc3, 0x28}
)

type binaryRequest struct {
	header http.Header
	body   []byte
}

// binaryServer records every request and answers with handler. Status 429 and up map to their kind.
func binaryServer(t *testing.T, timeout time.Duration, handler func(w http.ResponseWriter, r *http.Request, count int)) (*Transport, func() []binaryRequest) {
	t.Helper()
	var lock sync.Mutex
	var seen []binaryRequest
	server := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		body, _ := io.ReadAll(r.Body)
		lock.Lock()
		seen = append(seen, binaryRequest{header: r.Header.Clone(), body: body})
		count := len(seen)
		lock.Unlock()
		handler(w, r, count)
	}))
	t.Cleanup(server.Close)
	transport := mustTransport(t, Settings{
		BaseURL: server.URL,
		ToError: func(context ErrorContext) *Error {
			kind := KindAPI
			switch context.Status {
			case http.StatusNotFound:
				kind = "not_found"
			case http.StatusTooManyRequests:
				kind = "rate_limited"
			}
			return &Error{Kind: kind, Message: "failed", Status: context.Status, RawBody: context.Text, RetryAfter: context.Header.Get("Retry-After")}
		},
		Timeout:       timeout,
		MaxRetries:    1,
		RateLimitWait: time.Millisecond,
		MaxRetryWait:  time.Second,
	})
	return transport, func() []binaryRequest {
		lock.Lock()
		defer lock.Unlock()
		return append([]binaryRequest(nil), seen...)
	}
}

func TestADownloadReturnsTheExactBytesAndContentType(t *testing.T) {
	transport, seen := binaryServer(t, time.Second, func(w http.ResponseWriter, r *http.Request, _ int) {
		w.Header().Set("Content-Type", "application/pdf")
		_, _ = w.Write(notUTF8)
	})
	download, err := CallDownload(context.Background(), transport, downloadFile, Input{})
	if err != nil {
		t.Fatal(err)
	}
	defer download.Body.Close()
	body, err := io.ReadAll(download.Body)
	if err != nil || !bytes.Equal(body, notUTF8) || download.ContentType != "application/pdf" {
		t.Fatalf("download is %q %x, %v", download.ContentType, body, err)
	}
	if got := seen()[0].header.Get("Accept-Encoding"); got != "identity" {
		t.Errorf("Accept-Encoding is %q", got)
	}
}

func TestADownloadStreamsBeforeTheBodyHasArrived(t *testing.T) {
	release := make(chan struct{})
	transport, _ := binaryServer(t, 5*time.Second, func(w http.ResponseWriter, r *http.Request, _ int) {
		_, _ = w.Write([]byte("first"))
		w.(http.Flusher).Flush()
		<-release
		_, _ = w.Write([]byte("second"))
	})
	download, err := CallDownload(context.Background(), transport, downloadFile, Input{})
	if err != nil {
		t.Fatal(err)
	}
	defer download.Body.Close()
	chunk := make([]byte, 5)
	if _, err := io.ReadFull(download.Body, chunk); err != nil || string(chunk) != "first" {
		t.Fatalf("first chunk is %q, %v", chunk, err)
	}
	close(release)
	rest, err := io.ReadAll(download.Body)
	if err != nil || string(rest) != "second" {
		t.Fatalf("rest is %q, %v", rest, err)
	}
}

func TestAnEmptyDownloadIsAnEmptyBody(t *testing.T) {
	transport, _ := binaryServer(t, time.Second, func(w http.ResponseWriter, r *http.Request, _ int) {
		w.WriteHeader(http.StatusOK)
	})
	download, err := CallDownload(context.Background(), transport, downloadFile, Input{})
	if err != nil {
		t.Fatal(err)
	}
	defer download.Body.Close()
	if body, err := io.ReadAll(download.Body); err != nil || len(body) != 0 || download.ContentType != "" {
		t.Fatalf("download is %q %q, %v", download.ContentType, body, err)
	}
}

func TestTheDeadlineKeepsRunningWhileADownloadIsRead(t *testing.T) {
	transport, _ := binaryServer(t, 100*time.Millisecond, func(w http.ResponseWriter, r *http.Request, _ int) {
		_, _ = w.Write([]byte("partial"))
		w.(http.Flusher).Flush()
		<-r.Context().Done()
	})
	download, err := CallDownload(context.Background(), transport, downloadFile, Input{})
	if err != nil {
		t.Fatal(err)
	}
	defer download.Body.Close()
	_, err = io.ReadAll(download.Body)
	var failure *Error
	if !errors.As(err, &failure) || failure.Kind != KindTimeout {
		t.Fatalf("error is %v", err)
	}
}

func TestADownloadThatFailsIsATypedErrorWithItsText(t *testing.T) {
	transport, _ := binaryServer(t, time.Second, func(w http.ResponseWriter, r *http.Request, _ int) {
		w.Header().Set("Content-Type", "application/json")
		w.WriteHeader(http.StatusNotFound)
		_, _ = w.Write([]byte(`{"message":"not found"}`))
	})
	_, err := CallDownload(context.Background(), transport, downloadFile, Input{})
	var failure *Error
	if !errors.As(err, &failure) || failure.Kind != "not_found" || failure.RawBody != `{"message":"not found"}` {
		t.Fatalf("error is %v", err)
	}
}

func rateLimitedOnce(w http.ResponseWriter, r *http.Request, count int) {
	if count == 1 {
		w.WriteHeader(http.StatusTooManyRequests)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	_, _ = w.Write([]byte(`{"id":1}`))
}

func TestARawBodyInMemoryIsSentUnchangedAndRetried(t *testing.T) {
	transport, seen := binaryServer(t, time.Second, rateLimitedOnce)
	result, err := Call[map[string]any](context.Background(), transport, uploadFile, Input{Raw: bytes.NewReader(notUTF8)})
	if err != nil || result["id"] != float64(1) {
		t.Fatalf("result is %v, %v", result, err)
	}
	requests := seen()
	if len(requests) != 2 {
		t.Fatalf("sent %d requests", len(requests))
	}
	for _, request := range requests {
		if !bytes.Equal(request.body, notUTF8) || request.header.Get("Content-Type") != "application/octet-stream" {
			t.Errorf("sent %q %x", request.header.Get("Content-Type"), request.body)
		}
	}
}

func TestARawBodyStreamIsSentOnceAndNeverResent(t *testing.T) {
	transport, seen := binaryServer(t, time.Second, rateLimitedOnce)
	stream := io.MultiReader(bytes.NewReader(notUTF8[:4]), bytes.NewReader(notUTF8[4:]))
	_, err := Call[map[string]any](context.Background(), transport, uploadFile, Input{Raw: stream})
	var failure *Error
	if !errors.As(err, &failure) || failure.Kind != "rate_limited" {
		t.Fatalf("error is %v", err)
	}
	requests := seen()
	if len(requests) != 1 || !bytes.Equal(requests[0].body, notUTF8) {
		t.Fatalf("sent %d requests: %x", len(requests), requests[0].body)
	}
}

type closeRecorder struct {
	io.Reader
	closed bool
}

func (c *closeRecorder) Close() error {
	c.closed = true
	return nil
}

func TestARawBodyStreamIsLeftOpenForTheCaller(t *testing.T) {
	transport, seen := binaryServer(t, time.Second, func(w http.ResponseWriter, r *http.Request, _ int) {
		w.Header().Set("Content-Type", "application/json")
		_, _ = w.Write([]byte(`{}`))
	})
	stream := &closeRecorder{Reader: bytes.NewReader(notUTF8)}
	if _, err := Call[map[string]any](context.Background(), transport, uploadFile, Input{Raw: stream}); err != nil {
		t.Fatal(err)
	}
	if stream.closed || !bytes.Equal(seen()[0].body, notUTF8) {
		t.Fatalf("closed is %v", stream.closed)
	}
}

func TestCredentialsSeeABodyInMemoryButNotAStream(t *testing.T) {
	var lock sync.Mutex
	var bodies [][]byte
	credentials := applyFunc(func(auth *AuthRequest) {
		lock.Lock()
		defer lock.Unlock()
		bodies = append(bodies, auth.Body)
	})
	transport, _ := binaryServer(t, time.Second, func(w http.ResponseWriter, r *http.Request, _ int) {
		w.Header().Set("Content-Type", "application/json")
		_, _ = w.Write([]byte(`{}`))
	})
	transport.settings.Credentials = credentials
	for _, raw := range []io.Reader{bytes.NewBuffer(notUTF8), io.LimitReader(bytes.NewReader(notUTF8), 64)} {
		if _, err := Call[map[string]any](context.Background(), transport, uploadFile, Input{Raw: raw}); err != nil {
			t.Fatal(err)
		}
	}
	if !bytes.Equal(bodies[0], notUTF8) || len(bodies[1]) != 0 {
		t.Fatalf("credentials saw %x and %x", bodies[0], bodies[1])
	}
}

type applyFunc func(*AuthRequest)

func (f applyFunc) Apply(_ context.Context, auth *AuthRequest) error {
	f(auth)
	return nil
}

func (f applyFunc) Secrets() []string { return nil }

func TestATextResponseThatIsNotJSONIsText(t *testing.T) {
	const report = "id\tname\n1\tsynthetic\n"
	transport, _ := binaryServer(t, time.Second, func(w http.ResponseWriter, r *http.Request, _ int) {
		w.Header().Set("Content-Type", "text/tab-separated-values")
		_, _ = w.Write([]byte(report))
	})
	result, err := Call[string](context.Background(), transport, getReport, Input{})
	if err != nil || result != report {
		t.Fatalf("result is %q, %v", result, err)
	}
}
