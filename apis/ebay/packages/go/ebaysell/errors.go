package ebaysell

import (
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"strconv"

	"github.com/fdhoff/api-sdks/apis/ebay/packages/go/internal/runtime"
)

// APIError is the error every failed call returns, apart from the caller's own context ending, a
// call that has no token to send, and a request that cannot be encoded, such as a body holding NaN.
// That fails before anything is sent, with an error wrapping the encoder's own. For an error
// response, Code and Detail are the errorId and message of the first entry in the body's errors
// list, when it has one; [ErrorDetails] reads the whole list.
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

// ErrorParameter is one entry of an error's parameters list.
type ErrorParameter struct {
	Name  string `json:"name"`
	Value string `json:"value"`
}

// ErrorDetail is one entry of an eBay error response's errors list. ErrorID is 0 when the entry has
// none.
type ErrorDetail struct {
	ErrorID     int64            `json:"errorId"`
	Domain      string           `json:"domain"`
	Subdomain   string           `json:"subdomain"`
	Category    string           `json:"category"`
	Message     string           `json:"message"`
	LongMessage string           `json:"longMessage"`
	Parameters  []ErrorParameter `json:"parameters"`
}

// ErrorDetails reads the errors list of a failed call's response body, best-effort: an entry or
// field of the wrong type is skipped. It returns nil for an error without such a body.
func ErrorDetails(err error) []ErrorDetail {
	var failure *APIError
	if !errors.As(err, &failure) || failure.RawBody == "" {
		return nil
	}
	var body struct {
		Errors []json.RawMessage `json:"errors"`
	}
	if json.Unmarshal([]byte(failure.RawBody), &body) != nil {
		return nil
	}
	details := make([]ErrorDetail, 0, len(body.Errors))
	for _, raw := range body.Errors {
		if detail, ok := errorDetail(raw); ok {
			details = append(details, detail)
		}
	}
	return details
}

// errorDetail reads each field on its own, so one of the wrong type does not lose the rest.
func errorDetail(raw json.RawMessage) (ErrorDetail, bool) {
	var fields map[string]json.RawMessage
	if json.Unmarshal(raw, &fields) != nil || fields == nil {
		return ErrorDetail{}, false
	}
	var detail ErrorDetail
	targets := map[string]any{
		"errorId": &detail.ErrorID, "domain": &detail.Domain, "subdomain": &detail.Subdomain, "category": &detail.Category,
		"message": &detail.Message, "longMessage": &detail.LongMessage,
	}
	for name, target := range targets {
		_ = json.Unmarshal(fields[name], target)
	}
	var parameters []json.RawMessage
	_ = json.Unmarshal(fields["parameters"], &parameters)
	for _, item := range parameters {
		var parameter ErrorParameter
		var values map[string]json.RawMessage
		if json.Unmarshal(item, &values) != nil || values == nil {
			continue
		}
		_ = json.Unmarshal(values["name"], &parameter.Name)
		_ = json.Unmarshal(values["value"], &parameter.Value)
		detail.Parameters = append(detail.Parameters, parameter)
	}
	return detail, true
}

// firstError is the errorId and message of the first entry of the body's errors list.
func firstError(body any) (string, string) {
	fields, _ := body.(map[string]any)
	list, _ := fields["errors"].([]any)
	if len(list) == 0 {
		return "", ""
	}
	first, _ := list[0].(map[string]any)
	message, _ := first["message"].(string)
	code := ""
	if number, ok := first["errorId"].(json.Number); ok {
		if id, err := strconv.ParseInt(number.String(), 10, 64); err == nil {
			code = strconv.FormatInt(id, 10)
		}
	}
	return code, message
}

// toError maps on status first, then reads the body best-effort.
func toError(context runtime.ErrorContext) *APIError {
	kind := errorKind(context.Status)
	code, detail := firstError(context.JSON)
	message := fmt.Sprintf("HTTP %d (%s)", context.Status, kind)
	if detail != "" {
		message += ": " + detail
	}
	return &APIError{
		Kind:       kind,
		Message:    message,
		Status:     context.Status,
		RawBody:    context.Text,
		Code:       code,
		Detail:     detail,
		RetryAfter: context.Header.Get("Retry-After"),
	}
}
