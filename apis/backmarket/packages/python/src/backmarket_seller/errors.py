from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ._runtime import ApiConnectionError, ApiError, ApiTimeoutError, DecodeError, ErrorContext

BOT_CHALLENGE_CODE = "bot-need-challenge"


class BadRequestError(ApiError):
    """HTTP 400."""

    kind = "bad_request"


class AuthenticationError(ApiError):
    """HTTP 401."""

    kind = "authentication"


class PermissionDeniedError(ApiError):
    """HTTP 403 that is neither of the two below."""

    kind = "permission"


class WafBlockedError(PermissionDeniedError):
    """HTTP 403 HTML block from the firewall. Give `cf_ray` to your seller contact."""

    kind = "waf_blocked"


class BotChallengeError(PermissionDeniedError):
    """HTTP 403 from bot management."""

    kind = "bot_challenge"


class NotFoundError(ApiError):
    """HTTP 404."""

    kind = "not_found"


class UnprocessableError(ApiError):
    """HTTP 422."""

    kind = "validation"


class RateLimitedError(ApiError):
    """HTTP 429, after retries."""

    kind = "rate_limited"


class ServerError(ApiError):
    """HTTP 5xx, after retries."""

    kind = "server"


_BY_STATUS: dict[int, type[ApiError]] = {
    400: BadRequestError,
    401: AuthenticationError,
    404: NotFoundError,
    422: UnprocessableError,
    429: RateLimitedError,
}


def _first_error_code(body: Any) -> Any:
    errors = body.get("errors") if isinstance(body, Mapping) else None
    first = errors[0] if isinstance(errors, list) and errors else None
    return first.get("code") if isinstance(first, Mapping) else None


def _code(body: Any) -> Any:
    error = body.get("error") if isinstance(body, Mapping) else None
    code = error.get("code") if isinstance(error, Mapping) else None
    return _first_error_code(body) if code is None else code


def _error_type(context: ErrorContext) -> type[ApiError]:
    if context.status == 403:
        if _first_error_code(context.json) == BOT_CHALLENGE_CODE:
            return BotChallengeError
        if context.headers.get("cf-ray") and context.json is None:
            return WafBlockedError
        return PermissionDeniedError
    if context.status >= 500:
        return ServerError
    return _BY_STATUS.get(context.status, ApiError)


def to_error(context: ErrorContext) -> ApiError:
    """Map on status first, then read the body best-effort."""
    error_type = _error_type(context)
    body = context.json
    code = _code(body)
    request_id: str | None = body.get("requestId") if isinstance(body, Mapping) else None
    return error_type(
        f"HTTP {context.status} ({error_type.kind})" + (f": {code}" if code is not None else ""),
        status=context.status,
        raw_body=context.text,
        code=code,
        request_id=request_id,
        retry_after=context.headers.get("retry-after"),
        cf_ray=context.headers.get("cf-ray"),
    )


__all__ = [
    "ApiConnectionError",
    "ApiError",
    "ApiTimeoutError",
    "AuthenticationError",
    "BadRequestError",
    "BotChallengeError",
    "DecodeError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitedError",
    "ServerError",
    "UnprocessableError",
    "WafBlockedError",
]
