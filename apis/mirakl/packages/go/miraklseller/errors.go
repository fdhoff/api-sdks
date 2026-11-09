package miraklseller

import (
	"fmt"
	"net/http"

	"github.com/fdhoff/api-sdks/apis/mirakl/packages/go/internal/runtime"
)

// APIError is the error every failed call returns, apart from the caller's own context ending and
// a request that cannot be encoded, such as a body holding NaN. That fails before anything is sent,
// with an error wrapping the encoder's own, so [errors.As] still finds it. Mirakl declares no error
// body, so RawBody holds it as text, with your key removed.
type APIError = runtime.Error

// Kind names a class of failure.
type Kind = runtime.Kind

// The kinds of failure.
const (
	KindAPI            = runtime.KindAPI
	KindTimeout        = runtime.KindTimeout
	KindConnection     = runtime.KindConnection
	KindDecode         = runtime.KindDecode
	KindJobTimeout     = runtime.KindJobTimeout
	KindBadRequest     = Kind("bad_request")
	KindAuthentication = Kind("authentication")
	KindPermission     = Kind("permission")
	KindNotFound       = Kind("not_found")
	KindConflict       = Kind("conflict")
	KindValidation     = Kind("validation")
	KindRateLimited    = Kind("rate_limited")
	KindServer         = Kind("server")
)

// Sentinels for [errors.Is].
var (
	ErrAPI            = &APIError{Kind: KindAPI, Message: "API error"}
	ErrTimeout        = &APIError{Kind: KindTimeout, Message: "timeout"}
	ErrConnection     = &APIError{Kind: KindConnection, Message: "connection failed"}
	ErrDecode         = &APIError{Kind: KindDecode, Message: "response cannot be decoded"}
	ErrJobTimeout     = &APIError{Kind: KindJobTimeout, Message: "job did not end in time"}
	ErrBadRequest     = &APIError{Kind: KindBadRequest, Message: "bad request"}
	ErrAuthentication = &APIError{Kind: KindAuthentication, Message: "authentication failed"}
	ErrPermission     = &APIError{Kind: KindPermission, Message: "permission denied"}
	ErrNotFound       = &APIError{Kind: KindNotFound, Message: "not found"}
	ErrConflict       = &APIError{Kind: KindConflict, Message: "conflict"}
	ErrValidation     = &APIError{Kind: KindValidation, Message: "validation failed"}
	ErrRateLimited    = &APIError{Kind: KindRateLimited, Message: "rate limited"}
	ErrServer         = &APIError{Kind: KindServer, Message: "server error"}
)

// A 401 means the key is missing, wrong or revoked. A 403 means its user lacks a role the operation
// needs.
var kindsByStatus = map[int]Kind{
	http.StatusBadRequest:          KindBadRequest,
	http.StatusUnauthorized:        KindAuthentication,
	http.StatusForbidden:           KindPermission,
	http.StatusNotFound:            KindNotFound,
	http.StatusConflict:            KindConflict,
	http.StatusUnprocessableEntity: KindValidation,
	http.StatusTooManyRequests:     KindRateLimited,
}

func errorKind(status int) Kind {
	if kind, found := kindsByStatus[status]; found {
		return kind
	}
	if status >= http.StatusInternalServerError {
		return KindServer
	}
	return KindAPI
}

// toError maps on status alone.
func toError(context runtime.ErrorContext) *APIError {
	kind := errorKind(context.Status)
	return &APIError{
		Kind:       kind,
		Message:    fmt.Sprintf("HTTP %d (%s)", context.Status, kind),
		Status:     context.Status,
		RawBody:    context.Text,
		RetryAfter: context.Header.Get("Retry-After"),
	}
}
