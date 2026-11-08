from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from ._runtime import ApiConnectionError, ApiError, ApiTimeoutError, DecodeError, ErrorContext


class HttpError(ApiError):
    """A response with an error status. `message` is the `error` text of its body, when it has one."""

    kind = "api"

    def __init__(self, text: str, *, message: str | None = None, **fields: Any) -> None:
        super().__init__(text, **fields)
        self.message = message


class BadRequestError(HttpError):
    """HTTP 400."""

    kind = "bad_request"


class AuthenticationError(HttpError):
    """HTTP 401, after any refresh of the access token."""

    kind = "authentication"


class PermissionDeniedError(HttpError):
    """HTTP 403."""

    kind = "permission"


class NotFoundError(HttpError):
    """HTTP 404."""

    kind = "not_found"


class ConflictError(HttpError):
    """HTTP 409."""

    kind = "conflict"


class UnprocessableError(HttpError):
    """HTTP 422."""

    kind = "validation"


class RateLimitedError(HttpError):
    """HTTP 429, after retries."""

    kind = "rate_limited"


class ServerError(HttpError):
    """HTTP 5xx, after retries."""

    kind = "server"


_BY_STATUS: dict[int, type[HttpError]] = {
    400: BadRequestError,
    401: AuthenticationError,
    403: PermissionDeniedError,
    404: NotFoundError,
    409: ConflictError,
    422: UnprocessableError,
    429: RateLimitedError,
}


def to_error(context: ErrorContext) -> ApiError:
    """Map on status first, then read the body best-effort."""
    error_type = _BY_STATUS.get(context.status) or (ServerError if context.status >= 500 else HttpError)
    body = context.json
    message = body.get("error") if isinstance(body, Mapping) else None
    message = message if isinstance(message, str) else None
    return error_type(
        f"HTTP {context.status} ({error_type.kind})" + (f": {message}" if message else ""),
        message=message,
        status=context.status,
        raw_body=context.text,
        retry_after=context.headers.get("retry-after"),
    )


__all__ = [
    "ApiConnectionError",
    "ApiError",
    "ApiTimeoutError",
    "AuthenticationError",
    "BadRequestError",
    "ConflictError",
    "DecodeError",
    "HttpError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitedError",
    "ServerError",
    "UnprocessableError",
]
