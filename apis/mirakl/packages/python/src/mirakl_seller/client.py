from __future__ import annotations

import logging
from types import TracebackType
from urllib.parse import urlsplit

import httpx
from typing_extensions import Self

from ._resources import AsyncResources, Resources
from ._runtime import (
    AsyncDownload,
    AsyncTransport,
    Credentials,
    Download,
    Requirement,
    Scheme,
    Settings,
    StaticCredentials,
    SyncTransport,
)
from .errors import to_error

logger = logging.getLogger("mirakl_seller")

# What a custom credentials provider sees as a URL download's requirements: the shop API key, as on every operation.
_DOWNLOAD_SECURITY: tuple[Requirement, ...] = ((Scheme("Shop-API-Key"),),)


def _settings(
    api_key: str | None,
    credentials: Credentials | None,
    base_url: str,
    shop_id: int | None,
    user_agent: str | None,
    timeout: float,
    max_retries: int,
    retry_base_delay: float,
    rate_limit_wait: float,
    max_retry_wait: float,
) -> Settings:
    if (api_key is None) == (credentials is None):
        raise ValueError("Pass exactly one of api_key and credentials")
    if api_key == "":
        raise ValueError("api_key must not be empty")
    url = urlsplit(base_url)
    if url.scheme not in ("http", "https") or not url.hostname:
        raise ValueError("base_url must be your operator's Mirakl URL, such as https://marketplace.example.com")
    if shop_id is not None and (isinstance(shop_id, bool) or not isinstance(shop_id, int)):
        raise ValueError("shop_id must be an integer")
    headers = {"Accept": "application/json"}
    if user_agent:
        headers["User-Agent"] = user_agent
    return Settings(
        base_url=base_url.rstrip("/"),
        # The key is the whole Authorization header, with no scheme in front.
        credentials=credentials or StaticCredentials({"Authorization": str(api_key)}, secrets=[str(api_key)]),
        headers=headers,
        to_error=to_error,
        logger=logger,
        timeout=timeout,
        max_retries=max_retries,
        retry_base_delay=retry_base_delay,
        rate_limit_wait=rate_limit_wait,
        max_retry_wait=max_retry_wait,
        query_defaults={} if shop_id is None else {"shop_id": str(shop_id)},
    )


class MiraklClient(Resources):
    """Synchronous client.

    Args:
        api_key: Your shop API key, from your operator's seller back office. It is sent as the whole
            `Authorization` header, never stored beyond this client, and never logged. Pass this or `credentials`.
        base_url: Your operator's Mirakl URL, without `/api`, such as `https://marketplace.example.com`. Every
            operator runs its own instance, so there is no default. The key is sent to it.
        shop_id: The shop to act for, when your key covers several. Every call sends it unless the call passes
            its own `shop_id`.
        credentials: A provider that sets each request's credentials, instead of `api_key`.
        user_agent: Sent as `User-Agent`, when given.
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
        api_key: str | None = None,
        *,
        base_url: str,
        shop_id: int | None = None,
        credentials: Credentials | None = None,
        user_agent: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_base_delay: float = 0.5,
        rate_limit_wait: float = 10.0,
        max_retry_wait: float = 60.0,
        http_transport: httpx.BaseTransport | None = None,
    ) -> None:
        settings = _settings(
            api_key,
            credentials,
            base_url,
            shop_id,
            user_agent,
            timeout,
            max_retries,
            retry_base_delay,
            rate_limit_wait,
            max_retry_wait,
        )
        self._transport = SyncTransport(settings, http_transport)
        super().__init__(self._transport)

    def download_url(self, url: str) -> Download:
        """Download a file URL that a response returned, such as an export's, following redirects. Your key goes
        only to `base_url`'s scheme, host and port, and never again once a redirect leaves them. Logs leave out
        the URL's query. Close the download, or read it in a `with` block."""
        return self._transport.download_url(url, _DOWNLOAD_SECURITY)

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


class AsyncMiraklClient(AsyncResources):
    """Asynchronous client. Takes the same arguments as `MiraklClient`."""

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str,
        shop_id: int | None = None,
        credentials: Credentials | None = None,
        user_agent: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_base_delay: float = 0.5,
        rate_limit_wait: float = 10.0,
        max_retry_wait: float = 60.0,
        http_transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        settings = _settings(
            api_key,
            credentials,
            base_url,
            shop_id,
            user_agent,
            timeout,
            max_retries,
            retry_base_delay,
            rate_limit_wait,
            max_retry_wait,
        )
        self._transport = AsyncTransport(settings, http_transport)
        super().__init__(self._transport)

    async def download_url(self, url: str) -> AsyncDownload:
        """Download a file URL that a response returned, as `MiraklClient.download_url` does. Close the download,
        or read it in an `async with` block."""
        return await self._transport.download_url(url, _DOWNLOAD_SECURITY)

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
