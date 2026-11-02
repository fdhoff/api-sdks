package runtime

import "net/http"

// Kind names a class of failure.
type Kind string

// Kinds the runtime raises itself. The API's status table adds the rest.
const (
	KindAPI        Kind = "api"
	KindTimeout    Kind = "timeout"
	KindConnection Kind = "connection"
	KindDecode     Kind = "decode"
)

// Error is the failure every call returns, apart from the caller's own context ending.
// Use [errors.Is] with a sentinel to test the kind, and [errors.As] to read the fields.
type Error struct {
	Kind       Kind
	Parent     Kind // A broader kind this one also matches, if any.
	Message    string
	Status     int
	RawBody    string // The response body, with the token removed.
	Code       string
	RequestID  string
	RetryAfter string
	CFRay      string
	Cause      error
}

func (e *Error) Error() string { return e.Message }

func (e *Error) Unwrap() error { return e.Cause }

// Is matches a sentinel: an Error that sets only Kind.
func (e *Error) Is(target error) bool {
	sentinel, ok := target.(*Error)
	return ok && sentinel.Status == 0 && (sentinel.Kind == e.Kind || sentinel.Kind == e.Parent)
}

// ErrorContext is a failed response, with the token already removed from Text and JSON.
type ErrorContext struct {
	Status int
	Header http.Header
	Text   string
	JSON   any
}
