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
	"sync/atomic"
	"time"
)

const redacted = "***"

// A backoff doubles per retry, and this keeps the shift in range for any retry count.
const maxBackoffDoublings = 20

// Paging is how an iterator walks pages: a [NextLink] or an [Offset].
type Paging interface{ itemsField() string }

// NextLink pages link to the next one. Only Params are read from the link: it is never fetched.
type NextLink struct {
	Items  string
	Link   string
	Params []string
}

// Offset pages are addressed by an offset, which advances by the number of items received. Iteration
// ends at an empty page or once the offset reaches the page's Total.
type Offset struct {
	Items  string
	Total  string
	Offset string
}

func (paging NextLink) itemsField() string { return paging.Items }
func (paging Offset) itemsField() string   { return paging.Items }

var defaultPaging = NextLink{Items: "results", Link: "next", Params: []string{"page", "cursor"}}

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
	// HeaderParams are the header arguments, each falling back to the client's default.
	HeaderParams []string
	// Host is the key of the host that serves the operation in [Settings.Hosts]. Empty means BaseURL.
	Host string
	// ReturnsJSON is set when the spec declares a JSON success body, so an empty one is an error.
	ReturnsJSON bool
	// Paging is how Iterator walks pages. Nil means the default [NextLink].
	Paging Paging
	// Security lists alternatives: any one requirement authorizes the call.
	Security []Requirement
}

func (o *Operation) paging() Paging {
	if o.Paging == nil {
		return defaultPaging
	}
	return o.Paging
}

func (o *Operation) items(page map[string]json.RawMessage) []json.RawMessage {
	var items []json.RawMessage
	if json.Unmarshal(page[o.paging().itemsField()], &items) != nil {
		return nil
	}
	return items
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
	BaseURL string
	// Hosts maps each host key to its base URL, for operations that name one.
	Hosts map[string]string
	// HeaderDefaults holds the value of a header argument that a call leaves unset, matched without
	// regard to case.
	HeaderDefaults map[string]string
	Credentials    Credentials
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
	settings   Settings
	client     *http.Client
	refreshing chan struct{}
	generation atomic.Uint64
}

// NewTransport builds a Transport. It never follows a redirect: a redirect is reported as a failure,
// so the token cannot be sent anywhere but the configured server.
func NewTransport(settings Settings) *Transport {
	return &Transport{
		settings:   settings,
		refreshing: make(chan struct{}, 1),
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

// redact removes every secret as written and as a path or query value escapes it.
func (t *Transport) redact(value string) string {
	return redactWith(redactions(t.settings.Credentials), value)
}

// redactedError prints its cause with the token removed, and still unwraps to it.
type redactedError struct {
	cause error
	text  string
}

func (e *redactedError) Error() string { return e.text }

func (e *redactedError) Unwrap() error { return e.cause }

// hide keeps the token out of a cause's message, such as a URL holding it as a path value.
func (t *Transport) hide(err error) error {
	if err == nil {
		return nil
	}
	text := t.redact(err.Error())
	if text == err.Error() {
		return err
	}
	return &redactedError{cause: err, text: text}
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
func (t *Transport) translate(ctx, attempt context.Context, err error) error {
	switch {
	case ctx.Err() != nil:
		return ctx.Err()
	case isTimeout(attempt, err):
		return &Error{Kind: KindTimeout, Message: "the request timed out", Cause: t.hide(err)}
	default:
		return &Error{Kind: KindConnection, Message: "the connection failed", Cause: t.hide(err)}
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

// baseURL is the root of the operation's host. A host missing from the settings is an error, so
// nothing is ever sent outside them.
func (t *Transport) baseURL(operation *Operation) (string, error) {
	if operation.Host == "" {
		return t.settings.BaseURL, nil
	}
	base, found := t.settings.Hosts[operation.Host]
	if !found {
		return "", fmt.Errorf("no base URL for host %q", operation.Host)
	}
	return base, nil
}

func (t *Transport) headerDefault(name string) (string, bool) {
	for key, value := range t.settings.HeaderDefaults {
		if strings.EqualFold(key, name) {
			return value, true
		}
	}
	return "", false
}

// addHeaderParams sets each header argument the call passed, or else the client's default for it.
func (t *Transport) addHeaderParams(header http.Header, built *request) {
	for _, name := range built.operation.HeaderParams {
		if values, passed := built.headers[name]; passed {
			header.Del(name)
			for _, value := range values {
				header.Add(name, value)
			}
		} else if value, found := t.headerDefault(name); found {
			header.Set(name, value)
		}
	}
}

// authorize builds one attempt's request and lets the credentials sign it.
func (t *Transport) authorize(ctx context.Context, built *request, base string) (*AuthRequest, error) {
	header := http.Header{}
	for name, values := range t.settings.Headers {
		header[name] = slices.Clone(values)
	}
	header.Set("Accept-Encoding", "gzip")
	if built.contentType != "" {
		header.Set("Content-Type", built.contentType)
	}
	t.addHeaderParams(header, built)
	auth := &AuthRequest{Method: built.method, URL: built.url(base), Header: header, Body: built.body, Operation: built.operation}
	if t.settings.Credentials == nil {
		return auth, nil
	}
	if err := t.settings.Credentials.Apply(ctx, auth); err != nil {
		return nil, t.hide(err)
	}
	return auth, nil
}

// refresh lets calls waiting on a refresh share it, and a call whose credentials were refreshed
// since it sent them retry without another.
func (t *Transport) refresh(ctx context.Context, auth *AuthRequest, generation uint64) (bool, error) {
	refresher, ok := t.settings.Credentials.(Refresher)
	if !ok {
		return false, nil
	}
	select {
	case t.refreshing <- struct{}{}:
	case <-ctx.Done():
		return false, ctx.Err()
	}
	defer func() { <-t.refreshing }()
	if t.generation.Load() != generation {
		return true, nil
	}
	refreshed, err := refresher.Refresh(ctx, auth)
	if err != nil {
		return false, t.hide(err)
	}
	if refreshed {
		t.generation.Add(1)
	}
	return refreshed, nil
}

func (t *Transport) attempt(ctx context.Context, auth *AuthRequest) (*response, error) {
	attempt, cancel := context.WithTimeout(ctx, t.settings.Timeout)
	defer cancel()
	outgoing, err := http.NewRequestWithContext(attempt, auth.Method, auth.URL, bytes.NewReader(auth.Body))
	if err != nil {
		return nil, &Error{Kind: KindConnection, Message: "the request could not be built", Cause: t.hide(err)}
	}
	outgoing.Header = auth.Header
	incoming, err := t.client.Do(outgoing)
	if err != nil {
		return nil, t.translate(ctx, attempt, err)
	}
	defer incoming.Body.Close()
	success := incoming.StatusCode >= 200 && incoming.StatusCode < 300
	body, err := io.ReadAll(incoming.Body)
	if err != nil {
		return nil, t.translate(ctx, attempt, err)
	}
	body, err = decompress(incoming.Header, body)
	if err != nil && success {
		return nil, &Error{Kind: KindDecode, Message: "the response body cannot be decompressed", Status: incoming.StatusCode, Cause: t.hide(err)}
	}
	t.log(ctx, slog.LevelDebug, "response", slog.String("method", auth.Method), slog.Int("status", incoming.StatusCode), slog.Int("bytes", len(body)))
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
	base, err := t.baseURL(built.operation)
	if err != nil {
		return nil, err
	}
	refreshed := false
	for tries := 0; ; tries++ {
		t.log(ctx, slog.LevelDebug, "request", slog.String("method", built.method), slog.String("url", built.url(base)))
		generation := t.generation.Load()
		auth, err := t.authorize(ctx, built, base)
		if err != nil {
			return nil, err
		}
		answer, err := t.attempt(ctx, auth)
		var failure *Error
		if err == nil || !errors.As(err, &failure) {
			return answer, err
		}
		// Never for an operation that sends no credentials, such as a token request made during a refresh.
		if failure.Status == http.StatusUnauthorized && !refreshed && len(built.operation.Security) > 0 {
			refreshed = true
			retry, err := t.refresh(ctx, auth, generation)
			if err != nil {
				return nil, err
			}
			if retry {
				t.log(ctx, slog.LevelInfo, "retrying after refreshing credentials")
				tries--
				continue
			}
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
	return &Error{Kind: KindDecode, Message: message, Status: answer.status, RawBody: t.redact(string(answer.body)), Cause: t.hide(cause)}
}

func decode[T any](t *Transport, operation *Operation, answer *response) (T, error) {
	var result, empty T
	if len(answer.body) == 0 {
		if operation.ReturnsJSON {
			return empty, t.decodeError("the response body is empty", answer, nil)
		}
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
	return decode[T](t, operation, answer)
}

// nextLink reads the position out of a page's link and applies it to our own request. The link is
// never fetched: it could send the token to another host. A nil result means the last page.
func (t *Transport) nextLink(operation *Operation, paging NextLink, query url.Values, page map[string]json.RawMessage, answer *response) (url.Values, error) {
	var link any
	if err := json.Unmarshal(page[paging.Link], &link); page[paging.Link] != nil && err != nil {
		return nil, t.decodeError(fmt.Sprintf("the %s link is not valid JSON", paging.Link), answer, err)
	}
	if link == nil || link == "" {
		return nil, nil
	}
	text, isText := link.(string)
	if !isText {
		return nil, t.decodeError(fmt.Sprintf("the %s link is not a string", paging.Link), answer, nil)
	}
	parsed, err := url.Parse(text)
	if err != nil {
		return nil, t.decodeError(fmt.Sprintf("the %s link cannot be parsed", paging.Link), answer, err)
	}
	position := parsed.Query()
	updated := url.Values{}
	for name, values := range query {
		updated[name] = values
	}
	advanced := false
	for _, marker := range paging.Params {
		value := position.Get(marker)
		if value == "" || !slices.Contains(operation.QueryParams, marker) {
			continue
		}
		advanced = advanced || value != query.Get(marker)
		updated.Set(marker, value)
	}
	if !advanced {
		return nil, t.decodeError(fmt.Sprintf("the %s link does not advance the iteration", paging.Link), answer, nil)
	}
	return updated, nil
}

// nextOffset moves the offset past the items received. A nil result means the last page.
func (t *Transport) nextOffset(paging Offset, query url.Values, page map[string]json.RawMessage, answer *response, received int) (url.Values, error) {
	var items []json.RawMessage
	if err := json.Unmarshal(page[paging.Items], &items); err != nil || items == nil {
		return nil, t.decodeError(fmt.Sprintf("the %s field of a page is not a list", paging.Items), answer, err)
	}
	if received == 0 {
		return nil, nil
	}
	start := 0
	if current := query.Get(paging.Offset); current != "" {
		parsed, err := strconv.Atoi(current)
		if err != nil {
			return nil, t.decodeError(fmt.Sprintf("the %s parameter is not an integer", paging.Offset), answer, err)
		}
		start = parsed
	}
	position := start + received
	var total *float64
	if json.Unmarshal(page[paging.Total], &total) == nil && total != nil && float64(position) >= *total {
		return nil, nil
	}
	updated := url.Values{}
	for name, values := range query {
		updated[name] = values
	}
	updated.Set(paging.Offset, strconv.Itoa(position))
	return updated, nil
}

// nextQuery is the query of the page after this one. A nil result means the last page.
func (t *Transport) nextQuery(operation *Operation, query url.Values, page map[string]json.RawMessage, answer *response, received int) (url.Values, error) {
	switch paging := operation.paging().(type) {
	case Offset:
		return t.nextOffset(paging, query, page, answer, received)
	case NextLink:
		return t.nextLink(operation, paging, query, page, answer)
	default:
		return nil, t.decodeError(fmt.Sprintf("unknown paging %T", paging), answer, nil)
	}
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
			items := operation.items(page)
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
			query, err := t.nextQuery(operation, built.query, page, answer, len(items))
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
