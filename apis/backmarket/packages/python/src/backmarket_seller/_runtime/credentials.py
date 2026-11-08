from __future__ import annotations

from collections.abc import Awaitable, Iterable, Mapping, MutableMapping, Sequence
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from .transport import Operation

_REDACTED = "***"


@dataclass(frozen=True)
class Scheme:
    """A security scheme an operation names, with the scopes it needs from it."""

    name: str
    scopes: tuple[str, ...] = ()


Requirement = tuple[Scheme, ...]
"""Schemes that must all be satisfied. An operation lists alternatives: any one requirement will do."""


@dataclass
class AuthRequest:
    """One attempt's request, as it will be sent. `headers` may be changed, and its names are
    case-insensitive; the rest is read-only."""

    method: str
    url: str
    headers: MutableMapping[str, str] = field(repr=False)
    body: bytes = field(repr=False)
    operation: Operation[Any]


class Credentials:
    """Supplies each request's credentials.

    `apply` runs before every attempt, retries included, so it can sign the final request. `secrets`
    lists every value to keep out of logs and errors, and is read again each time, so it may change.
    `refresh` runs after a 401, at most once per call and once at a time per client, and returns whether
    to retry. Each method may be a coroutine function when the client is asynchronous.
    """

    def apply(self, request: AuthRequest) -> None | Awaitable[None]:
        raise NotImplementedError

    def secrets(self) -> Iterable[str]:
        return ()

    def refresh(self, request: AuthRequest) -> bool | Awaitable[bool]:
        return False


class StaticCredentials(Credentials):
    """The same headers on every request."""

    def __init__(self, headers: Mapping[str, str], secrets: Sequence[str]) -> None:
        self._headers = dict(headers)
        self._secrets = tuple(secrets)

    def __repr__(self) -> str:
        return "StaticCredentials(***)"

    def apply(self, request: AuthRequest) -> None:
        request.headers.update(self._headers)

    def secrets(self) -> Iterable[str]:
        return self._secrets


def redact(credentials: Credentials, text: str) -> str:
    """Longest first, so a secret that contains another is removed whole."""
    for secret in sorted({secret for secret in credentials.secrets() if secret}, key=len, reverse=True):
        text = text.replace(secret, _REDACTED)
    return text
