package backmarketseller

import (
	"fmt"
	"net/http"

	"github.com/fdhoff/api-sdks/apis/backmarket/packages/go/internal/runtime"
)

// APIError is the error every failed call returns, apart from the caller's own context ending and
// a request that cannot be encoded, such as a body holding NaN. That fails before anything is sent,
// with an error wrapping the encoder's own, so [errors.As] still finds it.
type APIError = runtime.Error

// Kind names a class of failure.
type Kind = runtime.Kind

// The kinds of failure.
const (
	KindAPI            = runtime.KindAPI
	KindTimeout        = runtime.KindTimeout
	KindConnection     = runtime.KindConnection
	KindDecode         = runtime.KindDecode
	KindBadRequest     = Kind("bad_request")
	KindAuthentication = Kind("authentication")
	KindPermission     = Kind("permission")
	KindWAFBlocked     = Kind("waf_blocked")
	KindBotChallenge   = Kind("bot_challenge")
	KindNotFound       = Kind("not_found")
	KindValidation     = Kind("validation")
	KindRateLimited    = Kind("rate_limited")
	KindServer         = Kind("server")
)

// Sentinels for [errors.Is]. ErrPermission also matches ErrWAFBlocked and ErrBotChallenge.
var (
	ErrAPI            = &APIError{Kind: KindAPI, Message: "API error"}
	ErrTimeout        = &APIError{Kind: KindTimeout, Message: "timeout"}
	ErrConnection     = &APIError{Kind: KindConnection, Message: "connection failed"}
	ErrDecode         = &APIError{Kind: KindDecode, Message: "response cannot be decoded"}
	ErrBadRequest     = &APIError{Kind: KindBadRequest, Message: "bad request"}
	ErrAuthentication = &APIError{Kind: KindAuthentication, Message: "authentication failed"}
	ErrPermission     = &APIError{Kind: KindPermission, Message: "permission denied"}
	ErrWAFBlocked     = &APIError{Kind: KindWAFBlocked, Message: "blocked by the firewall"}
	ErrBotChallenge   = &APIError{Kind: KindBotChallenge, Message: "stopped by bot management"}
	ErrNotFound       = &APIError{Kind: KindNotFound, Message: "not found"}
	ErrValidation     = &APIError{Kind: KindValidation, Message: "validation failed"}
	ErrRateLimited    = &APIError{Kind: KindRateLimited, Message: "rate limited"}
	ErrServer         = &APIError{Kind: KindServer, Message: "server error"}
)

const botChallengeCode = "bot-need-challenge"

var kindsByStatus = map[int]Kind{
	http.StatusBadRequest:          KindBadRequest,
	http.StatusUnauthorized:        KindAuthentication,
	http.StatusNotFound:            KindNotFound,
	http.StatusUnprocessableEntity: KindValidation,
	http.StatusTooManyRequests:     KindRateLimited,
}

func text(value any) string {
	if value == nil {
		return ""
	}
	return fmt.Sprint(value)
}

func object(value any) map[string]any {
	found, _ := value.(map[string]any)
	return found
}

func firstErrorCode(body any) string {
	errors, _ := object(body)["errors"].([]any)
	if len(errors) == 0 {
		return ""
	}
	return text(object(errors[0])["code"])
}

func errorCode(body any) string {
	if code, found := object(object(body)["error"])["code"]; found {
		return text(code)
	}
	return firstErrorCode(body)
}

func errorKind(context runtime.ErrorContext) (kind, parent Kind) {
	if context.Status == http.StatusForbidden {
		switch {
		case firstErrorCode(context.JSON) == botChallengeCode:
			return KindBotChallenge, KindPermission
		case context.Header.Get("cf-ray") != "" && context.JSON == nil:
			return KindWAFBlocked, KindPermission
		default:
			return KindPermission, ""
		}
	}
	if context.Status >= http.StatusInternalServerError {
		return KindServer, ""
	}
	if kind, found := kindsByStatus[context.Status]; found {
		return kind, ""
	}
	return KindAPI, ""
}

// toError maps on status first, then reads the body best-effort.
func toError(context runtime.ErrorContext) *APIError {
	kind, parent := errorKind(context)
	code := errorCode(context.JSON)
	message := fmt.Sprintf("HTTP %d (%s)", context.Status, kind)
	if code != "" {
		message += ": " + code
	}
	return &APIError{
		Kind:       kind,
		Parent:     parent,
		Message:    message,
		Status:     context.Status,
		RawBody:    context.Text,
		Code:       code,
		RequestID:  text(object(context.JSON)["requestId"]),
		RetryAfter: context.Header.Get("Retry-After"),
		CFRay:      context.Header.Get("cf-ray"),
	}
}
