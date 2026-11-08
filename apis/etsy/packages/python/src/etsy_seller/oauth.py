"""OAuth 2 authorization code flow with PKCE, as Etsy implements it."""

from __future__ import annotations

import asyncio
import base64
import hashlib
import inspect
import re
import secrets
import threading
from collections import deque
from collections.abc import Awaitable, Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any
from urllib.parse import urlencode

from ._runtime import AsyncTransport, AuthRequest, Credentials, DecodeError, Operation, Param, SyncTransport

AUTHORIZATION_URL = "https://www.etsy.com/oauth/connect"
_VERIFIER = re.compile(r"[A-Za-z0-9\-._~]{43,128}")
_REMEMBERED = 16

_TOKEN: Operation[Any] = Operation(
    id="oauthToken",
    method="POST",
    path="/v3/public/oauth/token",
    resource="oauth",
    name="token",
    params=tuple(
        Param(name, name, "urlencoded")
        for name in ("grant_type", "client_id", "redirect_uri", "code", "code_verifier", "refresh_token")
    ),
    returns_json=True,
)


@dataclass(frozen=True)
class Token:
    """An access token and the refresh token that replaces it. Etsy prefixes both with the user's ID."""

    access_token: str = field(repr=False)
    refresh_token: str = field(repr=False)
    expires_in: int | None = None
    token_type: str = "Bearer"

    @property
    def user_id(self) -> int | None:
        prefix = self.access_token.split(".", 1)[0]
        return int(prefix) if prefix.isdigit() else None


@dataclass(frozen=True)
class AuthorizationRequest:
    """Send the user to `url`. Keep `state` and `code_verifier` until Etsy redirects back, check that the
    redirect's `state` matches, then pass its `code` and this `code_verifier` to `exchange_code`."""

    url: str
    state: str
    code_verifier: str = field(repr=False)


def code_challenge(code_verifier: str) -> str:
    """The S256 challenge for a PKCE code verifier."""
    digest = hashlib.sha256(code_verifier.encode("ascii")).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")


def authorization_url(
    api_key: str,
    redirect_uri: str,
    scopes: Sequence[str],
    *,
    state: str | None = None,
    code_verifier: str | None = None,
) -> AuthorizationRequest:
    """Build the URL that asks a user to grant your app `scopes`, with a fresh state and PKCE verifier
    unless you pass your own."""
    if not scopes:
        raise ValueError("Request at least one scope")
    verifier = code_verifier if code_verifier is not None else secrets.token_urlsafe(64)
    if not _VERIFIER.fullmatch(verifier):
        raise ValueError("code_verifier must be 43 to 128 unreserved characters")
    state = state if state is not None else secrets.token_urlsafe(32)
    query = urlencode(
        {
            "response_type": "code",
            "client_id": api_key,
            "redirect_uri": redirect_uri,
            "scope": " ".join(scopes),
            "state": state,
            "code_challenge": code_challenge(verifier),
            "code_challenge_method": "S256",
        }
    )
    return AuthorizationRequest(f"{AUTHORIZATION_URL}?{query}", state, verifier)


def _token(data: Any, status: int) -> Token:
    fields = data if isinstance(data, Mapping) else {}
    access, refresh, expires = fields.get("access_token"), fields.get("refresh_token"), fields.get("expires_in")
    if not isinstance(access, str) or not isinstance(refresh, str) or not access or not refresh:
        raise DecodeError("The token response has no access and refresh token", status=status)
    expires_in = expires if isinstance(expires, int) and not isinstance(expires, bool) else None
    token_type = fields.get("token_type")
    return Token(access, refresh, expires_in, token_type if isinstance(token_type, str) else "Bearer")


def _needs(operation: Operation[Any], scheme: str) -> bool:
    return any(part.name == scheme for requirement in operation.security for part in requirement)


class EtsyCredentials(Credentials):
    """Sends `x-api-key` on every operation and the access token on those that need OAuth. After a 401
    on one of those, refreshes the access token once, when there is a refresh token."""

    def __init__(
        self,
        api_key: str,
        shared_secret: str,
        access_token: str | None,
        refresh_token: str | None,
        on_token: Callable[[Token], object] | None,
    ) -> None:
        if not api_key or not shared_secret:
            raise ValueError("api_key and shared_secret are required")
        self.api_key = api_key
        self._shared_secret = shared_secret
        self._access_token = access_token
        self._refresh_token = refresh_token
        self._token: Token | None = None
        self._on_token = on_token
        self._lock = threading.Lock()
        self._seen: deque[str] = deque((secret for secret in (access_token, refresh_token) if secret), _REMEMBERED)
        self.refresher: Callable[[], Token | Awaitable[Token]] | None = None

    def __repr__(self) -> str:
        return "EtsyCredentials(***)"

    @property
    def refresh_token(self) -> str | None:
        return self._refresh_token

    @property
    def token(self) -> Token | None:
        """The last token stored, if any."""
        return self._token

    def apply(self, request: AuthRequest) -> None:
        if _needs(request.operation, "api_key"):
            request.headers["x-api-key"] = f"{self.api_key}:{self._shared_secret}"
        access = self._access_token
        if access and _needs(request.operation, "oauth2"):
            request.headers["Authorization"] = f"Bearer {access}"

    def secrets(self) -> Iterable[str]:
        with self._lock:
            return [self.api_key, self._shared_secret, *self._seen]

    def remember(self, *values: str) -> None:
        """Keep values out of logs and errors from now on, such as a code about to be exchanged. Only the
        most recent values are kept, so a long-lived client does not grow."""
        with self._lock:
            self._seen.extend(value for value in values if value)

    def store(self, token: Token) -> Token:
        self.remember(token.access_token, token.refresh_token)
        self._access_token = token.access_token
        self._refresh_token = token.refresh_token
        self._token = token
        if self._on_token is not None:
            self._on_token(token)
        return token

    def refresh(self, request: AuthRequest) -> bool | Awaitable[bool]:
        if self.refresher is None or not self._refresh_token or not _needs(request.operation, "oauth2"):
            return False
        result = self.refresher()
        return _refreshed(result) if inspect.isawaitable(result) else True


async def _refreshed(result: Awaitable[Token]) -> bool:
    await result
    return True


def _exchange_params(api_key: str, code: str, code_verifier: str, redirect_uri: str) -> dict[str, str]:
    return {
        "grant_type": "authorization_code",
        "client_id": api_key,
        "redirect_uri": redirect_uri,
        "code": code,
        "code_verifier": code_verifier,
    }


def _refresh_params(credentials: EtsyCredentials) -> dict[str, str]:
    refresh_token = credentials.refresh_token
    if not refresh_token:
        raise ValueError("There is no refresh token: pass refresh_token, or exchange a code first")
    return {"grant_type": "refresh_token", "client_id": credentials.api_key, "refresh_token": refresh_token}


def _replaced(credentials: EtsyCredentials, refresh_token: str | None) -> Token | None:
    """The token another refresh stored while this one waited, since each refresh token works only once."""
    token = credentials.token
    return token if token is not None and credentials.refresh_token != refresh_token else None


class OAuth:
    """OAuth 2 for a synchronous client. A token it obtains is used for the client's later calls, and is
    passed to the client's `on_token` callback for you to store."""

    def __init__(self, credentials: EtsyCredentials, transport: SyncTransport) -> None:
        self._credentials = credentials
        self._transport = transport
        self._refreshing = threading.Lock()

    def authorization_url(
        self, redirect_uri: str, scopes: Sequence[str], *, state: str | None = None
    ) -> AuthorizationRequest:
        """Build the URL that asks a user to grant your app `scopes`. See `AuthorizationRequest`."""
        return authorization_url(self._credentials.api_key, redirect_uri, scopes, state=state)

    def exchange_code(self, code: str, *, code_verifier: str, redirect_uri: str) -> Token:
        """Trade the code from Etsy's redirect for a token. `redirect_uri` must match the authorization URL's."""
        self._credentials.remember(code, code_verifier)
        params = _exchange_params(self._credentials.api_key, code, code_verifier, redirect_uri)
        return self._request(params)

    def refresh(self) -> Token:
        """Replace the access token now. The client also does this itself after a 401. A refresh asked for
        while another is under way waits for it and returns its token."""
        refresh_token = self._credentials.refresh_token
        with self._refreshing:
            replaced = _replaced(self._credentials, refresh_token)
            return replaced or self._request(_refresh_params(self._credentials))

    def _request(self, params: Mapping[str, str]) -> Token:
        reply = self._transport.fetch(_TOKEN, None, params)
        return self._credentials.store(_token(reply.data, reply.status))


class AsyncOAuth:
    """OAuth 2 for an asynchronous client, with the same methods as `OAuth`."""

    def __init__(self, credentials: EtsyCredentials, transport: AsyncTransport) -> None:
        self._credentials = credentials
        self._transport = transport
        self._refreshing = asyncio.Lock()

    def authorization_url(
        self, redirect_uri: str, scopes: Sequence[str], *, state: str | None = None
    ) -> AuthorizationRequest:
        """Build the URL that asks a user to grant your app `scopes`. See `AuthorizationRequest`."""
        return authorization_url(self._credentials.api_key, redirect_uri, scopes, state=state)

    async def exchange_code(self, code: str, *, code_verifier: str, redirect_uri: str) -> Token:
        """Trade the code from Etsy's redirect for a token. `redirect_uri` must match the authorization URL's."""
        self._credentials.remember(code, code_verifier)
        params = _exchange_params(self._credentials.api_key, code, code_verifier, redirect_uri)
        return await self._request(params)

    async def refresh(self) -> Token:
        """Replace the access token now. The client also does this itself after a 401. A refresh asked for
        while another is under way waits for it and returns its token."""
        refresh_token = self._credentials.refresh_token
        async with self._refreshing:
            replaced = _replaced(self._credentials, refresh_token)
            return replaced or await self._request(_refresh_params(self._credentials))

    async def _request(self, params: Mapping[str, str]) -> Token:
        reply = await self._transport.fetch(_TOKEN, None, params)
        return self._credentials.store(_token(reply.data, reply.status))


__all__ = ["AsyncOAuth", "AuthorizationRequest", "OAuth", "Token", "authorization_url", "code_challenge"]
