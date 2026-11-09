from __future__ import annotations

from ._runtime import ApiConnectionError, ApiError, ApiTimeoutError, DecodeError, ErrorContext


class HttpError(ApiError):
    """A response with an error status. Mercury declares no error body, so `raw_body` holds it as text, with your
    token removed."""

    kind = "api"


class BadRequestError(HttpError):
    """HTTP 400."""

    kind = "bad_request"


class AuthenticationError(HttpError):
    """HTTP 401: the token is missing, wrong or revoked."""

    kind = "authentication"


class PermissionDeniedError(HttpError):
    """HTTP 403: the token lacks the scope, or the request did not come from an allowed IP address."""

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
    error_type = _BY_STATUS.get(context.status) or (ServerError if context.status >= 500 else HttpError)
    return error_type(
        f"HTTP {context.status} ({error_type.kind})",
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
