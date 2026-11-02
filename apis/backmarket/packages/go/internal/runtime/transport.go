// Package runtime is the hand-written part of the client: everything an operation needs that the
// generator does badly. It holds nothing specific to any one API.
package runtime

import (
	"bytes"
	"compress/gzip"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"iter"
	"log/slog"
	"math"
	"net"
	"net/http"
	"net/url"
	"slices"
	"strconv"
	"strings"
	"time"
)

const redacted = "***"

// A backoff doubles per retry, and this keeps the shift in range for any retry count.
const maxBackoffDoublings = 20

var pageMarkers = []string{"page", "cursor"}

// Operation describes one API call.
type Operation struct {
	ID          string
	Method      string
	Path        string
	Resource    string
	Name        string
	Iterator    string
	PathParams  []string
	QueryParams []string
}

var operations = map[string]*Operation{}

// Register records a generated operation, so tools can find it by ID.
func Register(operation Operation) *Operation {
	operations[operation.ID] = &operation
	return &operation
}

// Lookup finds a registered operation.
func Lookup(id string) (*Operation, bool) {
	operation, found := operations[id]
	return operation, found
}

// Settings configures a Transport.
type Settings struct {
	BaseURL        string
	Secret         string
	Headers        http.Header
	ToError        func(ErrorContext) *Error
	Logger         *slog.Logger
	HTTPTransport  http.RoundTripper
	Timeout        time.Duration
	MaxRetries     int
	RetryBaseDelay time.Duration
	RateLimitWait  time.Duration
	MaxRetryWait   time.Duration
}

// Transport sends requests, applying the timeout, retry and redaction rules.
type Transport struct {
	settings Settings
	client   *http.Client
}

// NewTransport builds a Transport. It never follows a redirect: a redirect is reported as a failure,
// so the token cannot be sent anywhere but the configured server.
func NewTransport(settings Settings) *Transport {
	return &Transport{
		settings: settings,
		client: &http.Client{
			Transport: settings.HTTPTransport,
			CheckRedirect: func(*http.Request, []*http.Request) error {
				return http.ErrUseLastResponse
			},
		},
	}
}

type response struct {
	status int
	header http.Header
	body   []byte
}

func (t *Transport) redact(value string) string {
	return strings.ReplaceAll(value, t.settings.Secret, redacted)
}

func (t *Transport) log(ctx context.Context, level slog.Level, message string, attrs ...slog.Attr) {
	if t.settings.Logger == nil {
		return
	}
	for index, attr := range attrs {
		if attr.Value.Kind() == slog.KindString {
			attrs[index].Value = slog.StringValue(t.redact(attr.Value.String()))
		}
	}
	t.settings.Logger.LogAttrs(ctx, level, message, attrs...)
}

// decompress runs after the whole body has arrived, so that any failure here means a corrupt body
// and never a dropped connection. Go's own decompression cannot tell those two apart.
func decompress(header http.Header, body []byte) ([]byte, error) {
	if len(body) == 0 || !strings.EqualFold(header.Get("Content-Encoding"), "gzip") {
		return body, nil
	}
	reader, err := gzip.NewReader(bytes.NewReader(body))
	if err != nil {
		return nil, err
	}
	return io.ReadAll(reader)
}

func isTimeout(attempt context.Context, err error) bool {
	var network net.Error
	return attempt.Err() != nil || errors.Is(err, context.DeadlineExceeded) || (errors.As(err, &network) && network.Timeout())
}

// translate reports the caller's own context ending as it is, because that is not an API failure.
func translate(ctx, attempt context.Context, err error) error {
	switch {
	case ctx.Err() != nil:
		return ctx.Err()
	case isTimeout(attempt, err):
		return &Error{Kind: KindTimeout, Message: "the request timed out", Cause: err}
	default:
		return &Error{Kind: KindConnection, Message: "the connection failed", Cause: err}
	}
}

func (t *Transport) failure(status int, header http.Header, body []byte) *Error {
	text := t.redact(string(body))
	decoder := json.NewDecoder(strings.NewReader(text))
	decoder.UseNumber()
	var parsed any
	if decoder.Decode(&parsed) != nil {
		parsed = nil
	}
	return t.settings.ToError(ErrorContext{Status: status, Header: header, Text: text, JSON: parsed})
}

func (t *Transport) attempt(ctx context.Context, built *request) (*response, error) {
	attempt, cancel := context.WithTimeout(ctx, t.settings.Timeout)
	defer cancel()
	outgoing, err := http.NewRequestWithContext(attempt, built.method, built.url(t.settings.BaseURL), bytes.NewReader(built.body))
	if err != nil {
		return nil, &Error{Kind: KindConnection, Message: "the request could not be built", Cause: err}
	}
	for name, values := range t.settings.Headers {
		outgoing.Header[name] = values
	}
	outgoing.Header.Set("Accept-Encoding", "gzip")
	if built.contentType != "" {
		outgoing.Header.Set("Content-Type", built.contentType)
	}
	incoming, err := t.client.Do(outgoing)
	if err != nil {
		return nil, translate(ctx, attempt, err)
	}
	defer incoming.Body.Close()
	success := incoming.StatusCode >= 200 && incoming.StatusCode < 300
	body, err := io.ReadAll(incoming.Body)
	if err != nil {
		return nil, translate(ctx, attempt, err)
	}
	body, err = decompress(incoming.Header, body)
	if err != nil && success {
		return nil, &Error{Kind: KindDecode, Message: "the response body cannot be decompressed", Status: incoming.StatusCode, Cause: err}
	}
	t.log(ctx, slog.LevelDebug, "response", slog.String("method", built.method), slog.Int("status", incoming.StatusCode), slog.Int("bytes", len(body)))
	if !success {
		return nil, t.failure(incoming.StatusCode, incoming.Header, body)
	}
	return &response{status: incoming.StatusCode, header: incoming.Header, body: body}, nil
}

// retryAfter reads the header, reporting false when it is unusable or in the past. A number too
// large for a Duration comes back as the longest Duration, which then exceeds any maximum wait.
func retryAfter(value string, now time.Time) (time.Duration, bool) {
	value = strings.TrimSpace(value)
	if value == "" {
		return 0, false
	}
	if strings.Trim(value, "0123456789") == "" {
		seconds, err := strconv.ParseInt(value, 10, 64)
		if err != nil || seconds > math.MaxInt64/int64(time.Second) {
			return math.MaxInt64, true
		}
		return time.Duration(seconds) * time.Second, true
	}
	when, err := http.ParseTime(value)
	if err != nil {
		return 0, false
	}
	wait := when.Sub(now)
	return wait, wait > 0
}

func (t *Transport) retryDelay(failure *Error, method string, tries int) (time.Duration, bool) {
	settings := t.settings
	if tries >= settings.MaxRetries {
		return 0, false
	}
	if failure.Status == http.StatusTooManyRequests {
		wait, usable := retryAfter(failure.RetryAfter, time.Now())
		if !usable {
			return settings.RateLimitWait, true
		}
		return wait, wait <= settings.MaxRetryWait
	}
	failed := failure.Kind == KindTimeout || failure.Kind == KindConnection || failure.Status >= 500
	if method == http.MethodGet && failed {
		return settings.RetryBaseDelay << min(tries, maxBackoffDoublings), true
	}
	return 0, false
}

func sleep(ctx context.Context, delay time.Duration) error {
	timer := time.NewTimer(delay)
	defer timer.Stop()
	select {
	case <-timer.C:
		return nil
	case <-ctx.Done():
		return ctx.Err()
	}
}

func (t *Transport) fetch(ctx context.Context, built *request) (*response, error) {
	for tries := 0; ; tries++ {
		t.log(ctx, slog.LevelDebug, "request", slog.String("method", built.method), slog.String("url", built.url(t.settings.BaseURL)))
		answer, err := t.attempt(ctx, built)
		var failure *Error
		if err == nil || !errors.As(err, &failure) {
			return answer, err
		}
		delay, retry := t.retryDelay(failure, built.method, tries)
		if !retry {
			return nil, err
		}
		t.log(ctx, slog.LevelInfo, "retrying", slog.Duration("delay", delay), slog.String("kind", string(failure.Kind)))
		if err := sleep(ctx, delay); err != nil {
			return nil, err
		}
	}
}

func (t *Transport) decodeError(message string, answer *response, cause error) *Error {
	return &Error{Kind: KindDecode, Message: message, Status: answer.status, RawBody: t.redact(string(answer.body)), Cause: cause}
}

func decode[T any](t *Transport, answer *response) (T, error) {
	var result, empty T
	if len(answer.body) == 0 {
		return result, nil
	}
	if !strings.Contains(strings.ToLower(answer.header.Get("Content-Type")), "json") {
		switch target := any(&result).(type) {
		case *string:
			*target = string(answer.body)
		case *any:
			*target = string(answer.body)
		default:
			return empty, t.decodeError("the response body is not JSON", answer, nil)
		}
		return result, nil
	}
	if err := json.Unmarshal(answer.body, &result); err != nil {
		return empty, t.decodeError("the response body does not fit its type", answer, err)
	}
	return result, nil
}

// Call sends one operation and decodes its response.
func Call[T any](ctx context.Context, t *Transport, operation *Operation, input Input) (T, error) {
	var empty T
	built, err := newRequest(operation, input)
	if err != nil {
		return empty, err
	}
	answer, err := t.fetch(ctx, built)
	if err != nil {
		return empty, err
	}
	return decode[T](t, answer)
}

// nextQuery reads the position out of a page's `next` link and applies it to our own request.
// `next` is never fetched: it could send the token to another host. A nil result means the last page.
func (t *Transport) nextQuery(operation *Operation, query url.Values, page map[string]json.RawMessage, answer *response) (url.Values, error) {
	var link any
	if err := json.Unmarshal(page["next"], &link); page["next"] != nil && err != nil {
		return nil, t.decodeError("the next link is not valid JSON", answer, err)
	}
	if link == nil || link == "" {
		return nil, nil
	}
	text, isText := link.(string)
	if !isText {
		return nil, t.decodeError("the next link is not a string", answer, nil)
	}
	parsed, err := url.Parse(text)
	if err != nil {
		return nil, t.decodeError("the next link cannot be parsed", answer, err)
	}
	position := parsed.Query()
	updated := url.Values{}
	for name, values := range query {
		updated[name] = values
	}
	advanced := false
	for _, marker := range pageMarkers {
		value := position.Get(marker)
		if value == "" || !slices.Contains(operation.QueryParams, marker) {
			continue
		}
		advanced = advanced || value != query.Get(marker)
		updated.Set(marker, value)
	}
	if !advanced {
		return nil, t.decodeError("the next link does not advance the iteration", answer, nil)
	}
	return updated, nil
}

// Paginate walks every page of an operation, yielding each item. It stops after yielding an error.
func Paginate[T any](ctx context.Context, t *Transport, operation *Operation, input Input) iter.Seq2[T, error] {
	return func(yield func(T, error) bool) {
		var empty T
		built, err := newRequest(operation, input)
		if err != nil {
			yield(empty, err)
			return
		}
		for {
			answer, err := t.fetch(ctx, built)
			if err != nil {
				yield(empty, err)
				return
			}
			var page map[string]json.RawMessage
			if err := json.Unmarshal(answer.body, &page); err != nil || page == nil {
				yield(empty, t.decodeError("a page is not a JSON object", answer, err))
				return
			}
			var items []json.RawMessage
			if json.Unmarshal(page["results"], &items) != nil {
				items = nil
			}
			for _, raw := range items {
				var item T
				if err := json.Unmarshal(raw, &item); err != nil {
					yield(empty, t.decodeError(fmt.Sprintf("an item does not fit %T", item), answer, err))
					return
				}
				if !yield(item, nil) {
					return
				}
			}
			query, err := t.nextQuery(operation, built.query, page, answer)
			if err != nil {
				yield(empty, err)
				return
			}
			if query == nil {
				return
			}
			next := *built
			next.query = query
			built = &next
		}
	}
}
