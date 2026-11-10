from __future__ import annotations

from typing import Any

from ._runtime import ApiConnectionError, ApiError, ApiTimeoutError, DecodeError, ErrorContext


class HttpError(ApiError):
    """A response with an error status. `message` is the `message` of Gitea's JSON error body, when it has one,
    and `raw_body` the body as text. Both have every credential removed."""

    kind = "api"

    def __init__(self, text: str, *, message: str | None = None, **fields: Any) -> None:
        super().__init__(text, **fields)
        self.message = message


class BadRequestError(HttpError):
    """HTTP 400."""

    kind = "bad_request"


class AuthenticationError(HttpError):
    """HTTP 401: the credentials are missing or wrong, or a one-time password is needed."""

    kind = "authentication"


class PermissionDeniedError(HttpError):
    """HTTP 403: the credentials do not allow the call."""

    kind = "permission"


class NotFoundError(HttpError):
    """HTTP 404. Gitea also answers 404 for a private repository the credentials cannot see."""

    kind = "not_found"


class ConflictError(HttpError):
    """HTTP 409, such as for a repository or branch that already exists."""

    kind = "conflict"


class UnprocessableError(HttpError):
    """HTTP 422: Gitea refused the request's fields."""

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
    body = context.json
    message = body.get("message") if isinstance(body, dict) else None
    message = message if isinstance(message, str) else None
    summary = f"HTTP {context.status} ({error_type.kind})"
    return error_type(
        f"{summary}: {message}" if message else summary,
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
