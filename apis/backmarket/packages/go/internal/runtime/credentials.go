package runtime

import (
	"cmp"
	"context"
	"net/http"
	"net/url"
	"slices"
	"strings"
)

// Scheme is a security scheme an operation names, with the scopes it needs from it.
type Scheme struct {
	Name   string
	Scopes []string
}

// Requirement lists schemes that must all be satisfied. An operation lists alternatives: any one
// requirement will do.
type Requirement []Scheme

// AuthRequest is one attempt's request, as it will be sent. Header may be changed; the rest is
// read-only.
type AuthRequest struct {
	Method    string
	URL       string
	Header    http.Header
	Body      []byte
	Operation *Operation
}

// Credentials supplies each request's credentials. Apply runs before every attempt, retries
// included, so it can sign the final request. Secrets lists every value to keep out of logs and
// errors, and is called again each time, so it may change. Both may be called concurrently.
type Credentials interface {
	Apply(ctx context.Context, request *AuthRequest) error
	Secrets() []string
}

// Refresher is Credentials that can recover from a 401. Refresh runs at most once per call and once
// at a time per Transport, and reports whether to retry.
type Refresher interface {
	Refresh(ctx context.Context, request *AuthRequest) (bool, error)
}

// StaticCredentials sends the same headers on every request.
type StaticCredentials struct {
	Header http.Header
	Values []string
}

// Apply sets the headers.
func (c StaticCredentials) Apply(_ context.Context, request *AuthRequest) error {
	for name, values := range c.Header {
		request.Header[name] = slices.Clone(values)
	}
	return nil
}

// Secrets returns the values to redact.
func (c StaticCredentials) Secrets() []string { return c.Values }

// redactions lists each secret as written and as a path or query value escapes it, longest first so
// a secret that contains another is removed whole.
func redactions(credentials Credentials) []string {
	if credentials == nil {
		return nil
	}
	var forms []string
	for _, secret := range credentials.Secrets() {
		if secret != "" {
			forms = append(forms, secret, url.PathEscape(secret), url.QueryEscape(secret))
		}
	}
	slices.SortFunc(forms, func(a, b string) int { return cmp.Or(cmp.Compare(len(b), len(a)), strings.Compare(a, b)) })
	return slices.Compact(forms)
}

func redactWith(forms []string, value string) string {
	for _, form := range forms {
		value = strings.ReplaceAll(value, form, redacted)
	}
	return value
}
