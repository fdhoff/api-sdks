from __future__ import annotations

import logging
from collections.abc import Callable
from types import TracebackType

import httpx
from typing_extensions import Self

from ._resources import AsyncResources, Resources
from ._runtime import AsyncTransport, Settings, SyncTransport
from .errors import to_error
from .oauth import AsyncOAuth, EtsyCredentials, OAuth, Token

logger = logging.getLogger("etsy_seller")

BASE_URL = "https://openapi.etsy.com"


def _settings(
    credentials: EtsyCredentials,
    user_agent: str | None,
    base_url: str,
    timeout: float,
    max_retries: int,
    retry_base_delay: float,
    rate_limit_wait: float,
    max_retry_wait: float,
) -> Settings:
    headers = {"Accept": "application/json"}
    if user_agent:
        headers["User-Agent"] = user_agent
    return Settings(
        base_url=base_url.rstrip("/"),
        credentials=credentials,
        headers=headers,
        to_error=to_error,
        logger=logger,
        timeout=timeout,
        max_retries=max_retries,
        retry_base_delay=retry_base_delay,
        rate_limit_wait=rate_limit_wait,
        max_retry_wait=max_retry_wait,
    )


class EtsyClient(Resources):
    """Synchronous client.

    Args:
        api_key: Your app's keystring.
        shared_secret: Your app's shared secret. Both are sent as `x-api-key` on every call.
        access_token: An OAuth access token, sent verbatim as a bearer token on calls that need one.
        refresh_token: Lets the client replace an expired access token by itself, once per call.
        on_token: Called with every new token pair, from `oauth.exchange_code` and every refresh, so you
            can store it. The old refresh token stops working.
        user_agent: Sent as `User-Agent`, when given.
        base_url: The server root. Point it at a mock in tests; your credentials are sent to it.
        timeout: Seconds allowed for each attempt, including reading the whole response.
        max_retries: Retries after the first attempt.
        retry_base_delay: Base in seconds of the exponential backoff.
        rate_limit_wait: Seconds to wait after a 429 with no usable `Retry-After`.
        max_retry_wait: The longest `Retry-After` to wait for, in seconds. A longer one raises
            `RateLimitedError` at once, with the header in `retry_after`.
        http_transport: An httpx transport to use instead of the network.
    """

    def __init__(
        self,
        api_key: str,
        shared_secret: str,
        *,
        access_token: str | None = None,
        refresh_token: str | None = None,
        on_token: Callable[[Token], object] | None = None,
        user_agent: str | None = None,
        base_url: str = BASE_URL,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_base_delay: float = 0.5,
        rate_limit_wait: float = 10.0,
        max_retry_wait: float = 60.0,
        http_transport: httpx.BaseTransport | None = None,
    ) -> None:
        credentials = EtsyCredentials(api_key, shared_secret, access_token, refresh_token, on_token)
        settings = _settings(
            credentials, user_agent, base_url, timeout, max_retries, retry_base_delay, rate_limit_wait, max_retry_wait
        )
        self._transport = SyncTransport(settings, http_transport)
        super().__init__(self._transport)
        self.oauth = OAuth(credentials, self._transport)
        credentials.refresher = self.oauth.refresh

    def close(self) -> None:
        self._transport.http.close()

    def __enter__(self) -> Self:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        self.close()


class AsyncEtsyClient(AsyncResources):
    """Asynchronous client. Takes the same arguments as `EtsyClient`."""

    def __init__(
        self,
        api_key: str,
        shared_secret: str,
        *,
        access_token: str | None = None,
        refresh_token: str | None = None,
        on_token: Callable[[Token], object] | None = None,
        user_agent: str | None = None,
        base_url: str = BASE_URL,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_base_delay: float = 0.5,
        rate_limit_wait: float = 10.0,
        max_retry_wait: float = 60.0,
        http_transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        credentials = EtsyCredentials(api_key, shared_secret, access_token, refresh_token, on_token)
        settings = _settings(
            credentials, user_agent, base_url, timeout, max_retries, retry_base_delay, rate_limit_wait, max_retry_wait
        )
        self._transport = AsyncTransport(settings, http_transport)
        super().__init__(self._transport)
        self.oauth = AsyncOAuth(credentials, self._transport)
        credentials.refresher = self.oauth.refresh

    async def aclose(self) -> None:
        await self._transport.http.aclose()

    async def __aenter__(self) -> Self:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        await self.aclose()
