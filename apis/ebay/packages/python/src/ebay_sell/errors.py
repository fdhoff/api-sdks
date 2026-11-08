from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass
from typing import Any

from ._runtime import ApiConnectionError, ApiError, ApiTimeoutError, DecodeError, ErrorContext


@dataclass(frozen=True)
class ErrorParameter:
    name: str | None
    value: str | None


@dataclass(frozen=True)
class ErrorDetail:
    """One entry of an eBay error response's `errors` list."""

    error_id: int | None
    domain: str | None
    subdomain: str | None
    category: str | None
    message: str | None
    long_message: str | None
    parameters: tuple[ErrorParameter, ...]


class HttpError(ApiError):
    """A response with an error status. `errors` holds the body's `errors` list, and `message` and `code` are
    the first entry's `message` and `errorId`, when the body has them."""

    kind = "api"

    def __init__(
        self, text: str, *, message: str | None = None, errors: Sequence[ErrorDetail] = (), **fields: Any
    ) -> None:
        super().__init__(text, **fields)
        self.message = message
        self.errors = tuple(errors)


class BadRequestError(HttpError):
    """HTTP 400."""

    kind = "bad_request"


class AuthenticationError(HttpError):
    """HTTP 401, after any new token."""

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


def _string(value: Any) -> str | None:
    return value if isinstance(value, str) else None


def _parameters(value: Any) -> tuple[ErrorParameter, ...]:
    items = value if isinstance(value, list) else []
    return tuple(
        ErrorParameter(_string(item.get("name")), _string(item.get("value")))
        for item in items
        if isinstance(item, Mapping)
    )


def error_details(body: Any) -> tuple[ErrorDetail, ...]:
    """The `errors` list of a body, best-effort: fields of the wrong type read as None."""
    items = body.get("errors") if isinstance(body, Mapping) else None
    return tuple(
        ErrorDetail(
            error_id=item["errorId"]
            if isinstance(item.get("errorId"), int) and not isinstance(item.get("errorId"), bool)
            else None,
            domain=_string(item.get("domain")),
            subdomain=_string(item.get("subdomain")),
            category=_string(item.get("category")),
            message=_string(item.get("message")),
            long_message=_string(item.get("longMessage")),
            parameters=_parameters(item.get("parameters")),
        )
        for item in (items if isinstance(items, list) else [])
        if isinstance(item, Mapping)
    )


def to_error(context: ErrorContext) -> ApiError:
    """Map on status first, then read the body best-effort."""
    error_type = _BY_STATUS.get(context.status) or (ServerError if context.status >= 500 else HttpError)
    errors = error_details(context.json)
    first = errors[0] if errors else None
    message = first.message if first else None
    return error_type(
        f"HTTP {context.status} ({error_type.kind})" + (f": {message}" if message else ""),
        message=message,
        errors=errors,
        status=context.status,
        raw_body=context.text,
        code=first.error_id if first else None,
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
    "ErrorDetail",
    "ErrorParameter",
    "HttpError",
    "NotFoundError",
    "PermissionDeniedError",
    "RateLimitedError",
    "ServerError",
    "UnprocessableError",
]
