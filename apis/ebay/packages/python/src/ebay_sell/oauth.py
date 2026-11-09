"""OAuth 2 as eBay implements it: application tokens from the client credentials grant, and user tokens
from the authorization code grant, both from one token endpoint with HTTP Basic client authentication."""

from __future__ import annotations

import asyncio
import base64
import inspect
import secrets
import threading
import time
from collections import deque
from collections.abc import Awaitable, Callable, Iterable, Mapping, Sequence
from dataclasses import dataclass, field, replace
from typing import Any
from urllib.parse import urlencode

from ._runtime import (
    AsyncTransport,
    AuthRequest,
    Credentials,
    DecodeError,
    MessageSigner,
    Operation,
    Param,
    SyncTransport,
)

API_SCOPE = "https://api.ebay.com/oauth/api_scope"
"""The scope of an application token, which the public operations accept."""

# The scopes eBay's client credentials grant gives. An operation that accepts any of them takes an
# application token, and every other operation a user token.
APP_SCOPES = frozenset({API_SCOPE, f"{API_SCOPE}/metadata.insights"})

AUTHORIZATION_URLS = {
    "production": "https://auth.ebay.com/oauth2/authorize",
    "sandbox": "https://auth.sandbox.ebay.com/oauth2/authorize",
}

# An application token this close to expiry is replaced before use.
_EXPIRY_MARGIN = 60.0
_REMEMBERED = 16

TOKEN_OPERATION: Operation[Any] = Operation(
    id="oauthToken",
    method="POST",
    path="/identity/v1/oauth2/token",
    resource="oauth",
    name="token",
    params=tuple(
        Param(name, name, "urlencoded") for name in ("grant_type", "code", "redirect_uri", "refresh_token", "scope")
    ),
    returns_json=True,
    host="api",
)


@dataclass(frozen=True)
class Token:
    """An access token, and for a user token the refresh token that replaces it. eBay's refresh returns a
    new access token only, so the refresh token carries over."""

    access_token: str = field(repr=False)
    expires_in: int | None = None
    refresh_token: str | None = field(default=None, repr=False)
    refresh_token_expires_in: int | None = None
    token_type: str = "Bearer"


@dataclass(frozen=True)
class AuthorizationRequest:
    """Send the user to `url`. Keep `state` until eBay redirects to your RuName's accept URL, check that the
    redirect's `state` matches, then pass its `code` to `exchange_code`."""

    url: str
    state: str


def authorization_url(
    client_id: str,
    ru_name: str,
    scopes: Sequence[str],
    *,
    state: str | None = None,
    prompt: str | None = None,
    environment: str = "production",
) -> AuthorizationRequest:
    """Build the URL that asks a user to grant your app `scopes`, with a fresh state unless you pass your own.
    `ru_name` is your app's redirect URL name, which eBay takes as `redirect_uri`. Pass `prompt="login"` to
    make the user sign in even if they already are."""
    if not scopes:
        raise ValueError("Request at least one scope")
    if environment not in AUTHORIZATION_URLS:
        raise ValueError(f"Unknown environment {environment!r}; expected one of: {', '.join(AUTHORIZATION_URLS)}")
    state = state if state is not None else secrets.token_urlsafe(32)
    query = {
        "client_id": client_id,
        "redirect_uri": ru_name,
        "response_type": "code",
        "scope": " ".join(scopes),
        "state": state,
    }
    if prompt is not None:
        query["prompt"] = prompt
    return AuthorizationRequest(f"{AUTHORIZATION_URLS[environment]}?{urlencode(query)}", state)


def takes_app_token(operation: Operation[Any]) -> bool:
    """eBay lists the scopes an operation accepts, any one of which is enough."""
    return any(
        scope in APP_SCOPES for requirement in operation.security for part in requirement for scope in part.scopes
    )


def _integer(value: Any) -> int | None:
    return value if isinstance(value, int) and not isinstance(value, bool) else None


def _token(data: Any, status: int) -> Token:
    fields = data if isinstance(data, Mapping) else {}
    access = fields.get("access_token")
    if not isinstance(access, str) or not access:
        raise DecodeError("The token response has no access token", status=status)
    refresh = fields.get("refresh_token")
    token_type = fields.get("token_type")
    return Token(
        access,
        _integer(fields.get("expires_in")),
        refresh if isinstance(refresh, str) and refresh else None,
        _integer(fields.get("refresh_token_expires_in")),
        token_type if isinstance(token_type, str) else "Bearer",
    )


class EbayCredentials(Credentials):
    """Sends an application token on operations that accept one and a user token on the rest, then signs the
    request when there is a signer. Mints an application token when there is none or it is about to expire.
    After a 401, mints a new application token, or refreshes the user token once when there is a refresh
    token."""

    def __init__(
        self,
        client_id: str | None,
        client_secret: str | None,
        app_token: str | None,
        user_token: str | None,
        refresh_token: str | None,
        on_token: Callable[[Token], object] | None,
        signer: MessageSigner | None = None,
        signature_key: str | None = None,
        clock: Callable[[], float] = time.monotonic,
    ) -> None:
        if bool(client_id) != bool(client_secret):
            raise ValueError("Pass client_id and client_secret together")
        if not (client_id or app_token or user_token or refresh_token):
            raise ValueError("Pass client_id and client_secret, or a token")
        self.client_id = client_id
        self._client_secret = client_secret
        self._basic = (
            base64.b64encode(f"{client_id}:{client_secret}".encode()).decode() if client_id and client_secret else None
        )
        self._app_token = app_token
        self._app_expires_at: float | None = None
        self._user_token = user_token
        self._refresh_token = refresh_token
        self._on_token = on_token
        self._signer = signer
        self._signature_key = signature_key
        self._clock = clock
        self._lock = threading.Lock()
        self._seen: deque[str] = deque((), _REMEMBERED)
        self.minter: Callable[[], Token | Awaitable[Token]] | None = None
        self.refresher: Callable[[], Token | Awaitable[Token]] | None = None

    def __repr__(self) -> str:
        return "EbayCredentials(***)"

    @property
    def can_mint(self) -> bool:
        return self._basic is not None

    @property
    def refresh_token(self) -> str | None:
        return self._refresh_token

    @property
    def user_token(self) -> str | None:
        return self._user_token

    def fresh_app_token(self) -> str | None:
        """The application token, unless it is about to expire. A token passed in has no known expiry."""
        expires = self._app_expires_at
        if self._app_token and (expires is None or self._clock() < expires - _EXPIRY_MARGIN):
            return self._app_token
        return None

    def basic_header(self) -> str:
        if self._basic is None:
            raise ValueError("A token request needs client_id and client_secret")
        return f"Basic {self._basic}"

    def apply(self, request: AuthRequest) -> None | Awaitable[None]:
        if request.operation is TOKEN_OPERATION:
            request.headers["Authorization"] = self.basic_header()
            return None
        if takes_app_token(request.operation):
            token = self.fresh_app_token()
            if token is None and self.can_mint and self.minter is not None:
                minted = self.minter()
                if inspect.isawaitable(minted):
                    return self._apply_later(request, minted)
                token = minted.access_token
            token = token or self._user_token
            if token is None:
                raise ValueError(
                    f"{request.operation.id} needs an application token: pass client_id and client_secret, or app_token"
                )
        else:
            token = self._user_token
            if token is None:
                raise ValueError(
                    f"{request.operation.id} needs a user token: pass user_token, or call oauth.exchange_code first"
                )
        self._finish(request, token)
        return None

    async def _apply_later(self, request: AuthRequest, minted: Awaitable[Token]) -> None:
        self._finish(request, (await minted).access_token)

    def _finish(self, request: AuthRequest, token: str) -> None:
        request.headers["Authorization"] = f"Bearer {token}"
        if self._signer is not None and self._signature_key is not None:
            request.headers["x-ebay-signature-key"] = self._signature_key
            self._signer.sign(request)

    def secrets(self) -> Iterable[str]:
        with self._lock:
            current = [self._client_secret, self._basic, self._app_token, self._user_token, self._refresh_token]
            signer = self._signer.secrets() if self._signer is not None else ()
            return [secret for secret in (*current, *signer, *self._seen) if secret]

    def remember(self, *values: str) -> None:
        """Keep values out of logs and errors from now on, such as a code about to be exchanged. Only the
        most recent values are kept, so a long-lived client does not grow."""
        with self._lock:
            self._seen.extend(value for value in values if value)

    def store_app(self, token: Token) -> Token:
        self.remember(*(value for value in (self._app_token,) if value))
        self._app_token = token.access_token
        self._app_expires_at = self._clock() + token.expires_in if token.expires_in is not None else None
        return token

    def store_user(self, token: Token) -> Token:
        """Keeps the refresh token when the response has none, as eBay's refresh does not return one."""
        kept = token if token.refresh_token else replace(token, refresh_token=self._refresh_token)
        self.remember(*(value for value in (self._user_token, self._refresh_token) if value))
        self._user_token = kept.access_token
        self._refresh_token = kept.refresh_token
        if self._on_token is not None:
            self._on_token(kept)
        return kept

    def _refreshes_app(self, operation: Operation[Any]) -> bool:
        """Whether a 401 on `operation` replaces the application token rather than the user token."""
        return takes_app_token(operation) and (self.can_mint or self._app_token is not None)

    def refresh_group(self, operation: Operation[Any]) -> str:
        """An application token and a user token refresh separately, so a 401 on one never waits out a
        refresh of the other."""
        return "app" if self._refreshes_app(operation) else "user"

    def refresh(self, request: AuthRequest) -> bool | Awaitable[bool]:
        if self._refreshes_app(request.operation):
            if not self.can_mint or self.minter is None:
                return False
            self._app_expires_at = float("-inf")
            result = self.minter()
        elif self._refresh_token and self.refresher is not None:
            result = self.refresher()
        else:
            return False
        return _refreshed(result) if inspect.isawaitable(result) else True


async def _refreshed(result: Awaitable[Token]) -> bool:
    await result
    return True


def _app_params(scopes: Sequence[str]) -> dict[str, str]:
    return {"grant_type": "client_credentials", "scope": " ".join(scopes)}


def _exchange_params(code: str, ru_name: str) -> dict[str, str]:
    return {"grant_type": "authorization_code", "code": code, "redirect_uri": ru_name}


def _refresh_params(credentials: EbayCredentials, scopes: Sequence[str] | None) -> dict[str, str]:
    refresh_token = credentials.refresh_token
    if not refresh_token:
        raise ValueError("There is no refresh token: pass refresh_token, or exchange a code first")
    params = {"grant_type": "refresh_token", "refresh_token": refresh_token}
    if scopes:
        params["scope"] = " ".join(scopes)
    return params


def _replaced_user(credentials: EbayCredentials, before: str | None) -> bool:
    """Another refresh replaced the user token while this one waited."""
    return credentials.user_token is not None and credentials.user_token != before


@dataclass
class _Config:
    ru_name: str | None
    app_scopes: Sequence[str]
    user_scopes: Sequence[str] | None
    environment: str


def _ru_name(config: _Config) -> str:
    if not config.ru_name:
        raise ValueError("Pass ru_name to the client to use the authorization code grant")
    return config.ru_name


def _client_id(credentials: EbayCredentials) -> str:
    if not credentials.client_id:
        raise ValueError("Pass client_id and client_secret to the client to use the authorization code grant")
    return credentials.client_id


class OAuth:
    """OAuth 2 for a synchronous client. Tokens it obtains are used for the client's later calls, and each
    new user token is passed to the client's `on_token` callback for you to store. That callback runs while
    the token locks are held, so it must not call these methods."""

    def __init__(self, credentials: EbayCredentials, transport: SyncTransport, config: _Config) -> None:
        self._credentials = credentials
        self._transport = transport
        self._config = config
        self._minting = threading.Lock()
        self._refreshing = threading.Lock()

    def authorization_url(
        self, scopes: Sequence[str], *, state: str | None = None, prompt: str | None = None
    ) -> AuthorizationRequest:
        """Build the URL that asks a user to grant your app `scopes`. See `AuthorizationRequest`."""
        client_id, ru_name = _client_id(self._credentials), _ru_name(self._config)
        return authorization_url(
            client_id, ru_name, scopes, state=state, prompt=prompt, environment=self._config.environment
        )

    def exchange_code(self, code: str) -> Token:
        """Trade the code from eBay's redirect for a user token and its refresh token."""
        self._credentials.remember(code)
        reply = self._transport.fetch(TOKEN_OPERATION, None, _exchange_params(code, _ru_name(self._config)))
        return self._credentials.store_user(_token(reply.data, reply.status))

    def refresh(self, scopes: Sequence[str] | None = None) -> Token:
        """Replace the user token now. The client also does this itself after a 401. `scopes` must be the
        original grant's or fewer, and default to the client's `user_scopes`. A refresh asked for while another
        is under way waits for it and returns without another."""
        before = self._credentials.user_token
        with self._refreshing:
            if _replaced_user(self._credentials, before):
                return Token(self._credentials.user_token or "", refresh_token=self._credentials.refresh_token)
            params = _refresh_params(self._credentials, scopes or self._config.user_scopes)
            reply = self._transport.fetch(TOKEN_OPERATION, None, params)
            return self._credentials.store_user(_token(reply.data, reply.status))

    def app_token(self, *, force: bool = False) -> Token:
        """Mint an application token with the client's `app_scopes`, unless the current one is still fresh
        and `force` is false."""
        with self._minting:
            current = self._credentials.fresh_app_token()
            if current is not None and not force:
                return Token(current)
            reply = self._transport.fetch(TOKEN_OPERATION, None, _app_params(self._config.app_scopes))
            return self._credentials.store_app(_token(reply.data, reply.status))


class AsyncOAuth:
    """OAuth 2 for an asynchronous client, with the same methods as `OAuth`."""

    def __init__(self, credentials: EbayCredentials, transport: AsyncTransport, config: _Config) -> None:
        self._credentials = credentials
        self._transport = transport
        self._config = config
        self._minting = asyncio.Lock()
        self._refreshing = asyncio.Lock()

    def authorization_url(
        self, scopes: Sequence[str], *, state: str | None = None, prompt: str | None = None
    ) -> AuthorizationRequest:
        """Build the URL that asks a user to grant your app `scopes`. See `AuthorizationRequest`."""
        client_id, ru_name = _client_id(self._credentials), _ru_name(self._config)
        return authorization_url(
            client_id, ru_name, scopes, state=state, prompt=prompt, environment=self._config.environment
        )

    async def exchange_code(self, code: str) -> Token:
        """Trade the code from eBay's redirect for a user token and its refresh token."""
        self._credentials.remember(code)
        reply = await self._transport.fetch(TOKEN_OPERATION, None, _exchange_params(code, _ru_name(self._config)))
        return self._credentials.store_user(_token(reply.data, reply.status))

    async def refresh(self, scopes: Sequence[str] | None = None) -> Token:
        """Replace the user token now. See `OAuth.refresh`."""
        before = self._credentials.user_token
        async with self._refreshing:
            if _replaced_user(self._credentials, before):
                return Token(self._credentials.user_token or "", refresh_token=self._credentials.refresh_token)
            params = _refresh_params(self._credentials, scopes or self._config.user_scopes)
            reply = await self._transport.fetch(TOKEN_OPERATION, None, params)
            return self._credentials.store_user(_token(reply.data, reply.status))

    async def app_token(self, *, force: bool = False) -> Token:
        """Mint an application token with the client's `app_scopes`, unless the current one is still fresh."""
        async with self._minting:
            current = self._credentials.fresh_app_token()
            if current is not None and not force:
                return Token(current)
            reply = await self._transport.fetch(TOKEN_OPERATION, None, _app_params(self._config.app_scopes))
            return self._credentials.store_app(_token(reply.data, reply.status))


__all__ = [
    "API_SCOPE",
    "APP_SCOPES",
    "AsyncOAuth",
    "AuthorizationRequest",
    "OAuth",
    "Token",
    "authorization_url",
    "takes_app_token",
]
