from __future__ import annotations

import logging
from enum import Enum
from types import TracebackType

import httpx
from typing_extensions import Self

from ._resources import AsyncResources, Resources
from ._runtime import AsyncTransport, Settings, SyncTransport
from .errors import to_error

logger = logging.getLogger("backmarket_seller")


class Region(str, Enum):
    AP = "ap"
    EU = "eu"
    NA = "na"


class Environment(str, Enum):
    PRODUCTION = "production"
    PREPROD = "preprod"


_SERVERS: dict[tuple[Region, Environment], str] = {
    (Region.AP, Environment.PRODUCTION): "https://www.backmarket.co.jp",
    (Region.AP, Environment.PREPROD): "https://preprod.backmarket.co.jp",
    (Region.EU, Environment.PRODUCTION): "https://www.backmarket.fr",
    (Region.EU, Environment.PREPROD): "https://preprod.backmarket.fr",
    (Region.NA, Environment.PRODUCTION): "https://www.backmarket.com",
    (Region.NA, Environment.PREPROD): "https://preprod.backmarket.com",
}


def _settings(
    token: str,
    user_agent: str,
    locale: str,
    region: Region | None,
    environment: Environment,
    base_url: str | None,
    timeout: float,
    max_retries: int,
    retry_base_delay: float,
    rate_limit_wait: float,
    max_retry_wait: float,
) -> Settings:
    if not token:
        raise ValueError("token is required")
    if not user_agent:
        raise ValueError("user_agent is required; the API may refuse a request without it")
    if (region is None) == (base_url is None):
        raise ValueError("Pass exactly one of region and base_url")
    url = _SERVERS[Region(region), Environment(environment)] if base_url is None else base_url
    return Settings(
        base_url=url.rstrip("/"),
        secret=token,
        headers={
            "Authorization": f"Basic {token}",
            "User-Agent": user_agent,
            "Accept": "application/json",
            "Accept-Language": locale,
        },
        to_error=to_error,
        logger=logger,
        timeout=timeout,
        max_retries=max_retries,
        retry_base_delay=retry_base_delay,
        rate_limit_wait=rate_limit_wait,
        max_retry_wait=max_retry_wait,
    )


class BackMarketClient(Resources):
    """Synchronous client.

    Args:
        token: Your API token, sent verbatim. It is never stored beyond this client or logged.
        user_agent: Required, in the form `BM-{Company}-{Integration};contact@example.com`.
        locale: Sent as `Accept-Language` on every call, for example `fr-fr`.
        region: The marketplace region. Pass this or `base_url`.
        environment: Production or preprod.
        base_url: A server root, for tests against a mock. The token is sent to it.
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
        token: str,
        *,
        user_agent: str,
        locale: str,
        region: Region | None = None,
        environment: Environment = Environment.PRODUCTION,
        base_url: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_base_delay: float = 0.5,
        rate_limit_wait: float = 10.0,
        max_retry_wait: float = 60.0,
        http_transport: httpx.BaseTransport | None = None,
    ) -> None:
        settings = _settings(
            token,
            user_agent,
            locale,
            region,
            environment,
            base_url,
            timeout,
            max_retries,
            retry_base_delay,
            rate_limit_wait,
            max_retry_wait,
        )
        self._transport = SyncTransport(settings, http_transport)
        super().__init__(self._transport)

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


class AsyncBackMarketClient(AsyncResources):
    """Asynchronous client. Takes the same arguments as `BackMarketClient`."""

    def __init__(
        self,
        token: str,
        *,
        user_agent: str,
        locale: str,
        region: Region | None = None,
        environment: Environment = Environment.PRODUCTION,
        base_url: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_base_delay: float = 0.5,
        rate_limit_wait: float = 10.0,
        max_retry_wait: float = 60.0,
        http_transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        settings = _settings(
            token,
            user_agent,
            locale,
            region,
            environment,
            base_url,
            timeout,
            max_retries,
            retry_base_delay,
            rate_limit_wait,
            max_retry_wait,
        )
        self._transport = AsyncTransport(settings, http_transport)
        super().__init__(self._transport)

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
