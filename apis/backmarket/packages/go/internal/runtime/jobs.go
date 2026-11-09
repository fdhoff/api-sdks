package runtime

import (
	"bytes"
	"cmp"
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"slices"
	"strings"
	"time"
)

const (
	defaultWaitInterval = time.Minute
	defaultWaitTimeout  = time.Hour
	maxRedirects        = 5
)

var redirects = []int{http.StatusMovedPermanently, http.StatusFound, http.StatusSeeOther, http.StatusTemporaryRedirect, http.StatusPermanentRedirect}

// Job is how an operation reports an asynchronous job's progress. The job has ended once the string
// at the dotted State path of its response is one of Done or Failed.
type Job struct {
	State  string
	Done   []string
	Failed []string
}

// WaitOptions sets how often a wait polls and for how long. A zero field takes its default.
type WaitOptions struct {
	// Interval is the pause between polls. The default is a minute.
	Interval time.Duration
	// Timeout is how long to poll before giving up. The default is an hour.
	Timeout time.Duration
}

func waitTimes(operation *Operation, options *WaitOptions) (interval, timeout time.Duration, err error) {
	if operation.Job == nil {
		return 0, 0, fmt.Errorf("%s does not report a job", operation.ID)
	}
	if options == nil {
		options = &WaitOptions{}
	}
	if options.Interval < 0 {
		return 0, 0, errors.New("the wait interval must not be negative")
	}
	if options.Timeout < 0 {
		return 0, 0, errors.New("the wait timeout must not be negative")
	}
	return cmp.Or(options.Interval, defaultWaitInterval), cmp.Or(options.Timeout, defaultWaitTimeout), nil
}

// jobEnded reads the job's state from the raw response, so it does not depend on the status model.
func (t *Transport) jobEnded(job *Job, answer *response) (bool, error) {
	var value any
	if json.Unmarshal(answer.body, &value) != nil {
		value = nil
	}
	for _, key := range strings.Split(job.State, ".") {
		object, _ := value.(map[string]any)
		value = object[key]
	}
	state, isText := value.(string)
	if !isText {
		return false, t.decodeError(fmt.Sprintf("the %s state of a job is not a string", job.State), answer, nil)
	}
	return slices.Contains(job.Done, state) || slices.Contains(job.Failed, state), nil
}

// Wait polls a job's status operation until the job ends, and returns its last status, done or
// failed. Each poll is an ordinary call, retried as any call is. Once the timeout has passed it
// returns the last status with a [KindJobTimeout] error that also holds it as Result. Cancelling ctx
// stops it at once, even between polls.
func Wait[T any](ctx context.Context, t *Transport, operation *Operation, input Input, options *WaitOptions) (T, error) {
	var empty T
	interval, timeout, err := waitTimes(operation, options)
	if err != nil {
		return empty, err
	}
	built, err := newRequest(operation, input)
	if err != nil {
		return empty, err
	}
	deadline := time.Now().Add(timeout)
	for {
		answer, err := t.fetch(ctx, built)
		if err != nil {
			return empty, err
		}
		result, err := decode[T](t, operation, answer)
		if err != nil {
			return empty, err
		}
		ended, err := t.jobEnded(operation.Job, answer)
		if err != nil {
			return empty, err
		}
		if ended {
			return result, nil
		}
		remaining := time.Until(deadline)
		if remaining <= 0 {
			return result, &Error{Kind: KindJobTimeout, Message: fmt.Sprintf("the job did not end within %s", timeout), Result: result}
		}
		if err := sleep(ctx, min(interval, remaining)); err != nil {
			return empty, err
		}
	}
}

func isAbsolute(address *url.URL) bool {
	_, known := defaultPorts[address.Scheme]
	return known && address.Hostname() != ""
}

// origin is a URL's scheme, lowercase host and port, with the scheme's default port filled in.
func origin(address *url.URL) string {
	port := defaultPorts[address.Scheme]
	if address.Port() != "" {
		port = ":" + address.Port()
	}
	return address.Scheme + "://" + strings.ToLower(address.Hostname()) + port
}

// redirected is where a redirect points, resolved against the URL that returned it.
func redirected(current *url.URL, answer *response) (*url.URL, error) {
	location := answer.header.Get("Location")
	if location == "" {
		return nil, &Error{Kind: KindDecode, Message: "a redirect has no Location", Status: answer.status}
	}
	next, err := current.Parse(location)
	if err != nil || !isAbsolute(next) {
		return nil, &Error{Kind: KindDecode, Message: "a redirect's Location is not an http or https URL", Status: answer.status}
	}
	return next, nil
}

// DownloadURL GETs an absolute URL that a response returned, as a [Download], following up to five
// redirects. Credentials are applied only while every request so far has gone to the base URL's
// scheme, host and port, and never again once a redirect leaves it. security is what the
// credentials see as the operation's requirements. The URL is logged without its query.
func DownloadURL(ctx context.Context, t *Transport, address string, security ...Requirement) (*Download, error) {
	target, err := url.Parse(address)
	if err != nil || !isAbsolute(target) {
		return nil, errors.New("the URL is not an absolute http or https URL")
	}
	base, err := url.Parse(t.settings.BaseURL)
	signed := err == nil
	operation := &Operation{ID: "downloadUrl", Method: http.MethodGet, Name: "DownloadURL", BinaryResponse: true, Security: security}
	for range maxRedirects + 1 {
		signed = signed && origin(target) == origin(base)
		built := &request{operation: operation, method: http.MethodGet, query: url.Values{}, headers: url.Values{}, target: target, unsigned: !signed}
		answer, err := t.fetch(ctx, built)
		if err != nil {
			return nil, err
		}
		if !slices.Contains(redirects, answer.status) {
			body := answer.stream
			if body == nil {
				body = io.NopCloser(bytes.NewReader(answer.body))
			}
			return &Download{ContentType: answer.header.Get("Content-Type"), Body: body}, nil
		}
		if target, err = redirected(target, answer); err != nil {
			return nil, err
		}
	}
	return nil, &Error{Kind: KindDecode, Message: fmt.Sprintf("more than %d redirects", maxRedirects)}
}
