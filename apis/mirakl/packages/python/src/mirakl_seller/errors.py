from __future__ import annotations

from ._runtime import ApiConnectionError, ApiError, ApiTimeoutError, DecodeError, ErrorContext, JobTimeoutError


class HttpError(ApiError):
    """A response with an error status. Mirakl documents no error body, so `raw_body` holds it as text, with your
    API key removed."""

    kind = "api"


class BadRequestError(HttpError):
    """HTTP 400."""

    kind = "bad_request"


class AuthenticationError(HttpError):
    """HTTP 401: the API key is missing, wrong or revoked."""

    kind = "authentication"


class PermissionDeniedError(HttpError):
    """HTTP 403: the key's role does not allow the call."""

    kind = "permission"


class NotFoundError(HttpError):
    """HTTP 404."""

    kind = "not_found"


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
    "DecodeError",
    "HttpError",
    "JobTimeoutError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitedError",
    "ServerError",
]
