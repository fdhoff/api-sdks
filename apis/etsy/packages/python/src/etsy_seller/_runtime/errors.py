from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, ClassVar


class ApiError(Exception):
    """Base class for every error the client raises."""

    kind: ClassVar[str] = "api"

    def __init__(
        self,
        message: str,
        *,
        status: int | None = None,
        raw_body: str | None = None,
        code: Any = None,
        request_id: str | None = None,
        retry_after: str | None = None,
        cf_ray: str | None = None,
    ) -> None:
        super().__init__(message)
        self.status = status
        self.raw_body = raw_body
        self.code = code
        self.request_id = request_id
        self.retry_after = retry_after
        self.cf_ray = cf_ray


class ApiTimeoutError(ApiError):
    """No response arrived in time, after retries."""

    kind = "timeout"


class ApiConnectionError(ApiError):
    """The connection failed or dropped before a full response, after retries."""

    kind = "connection"


class DecodeError(ApiError):
    """A success response could not be read as the API declares it."""

    kind = "decode"


@dataclass(frozen=True)
class ErrorContext:
    """A failed response, with the credential already removed from `text` and `json`."""

    status: int
    headers: Mapping[str, str]
    text: str
    json: Any
