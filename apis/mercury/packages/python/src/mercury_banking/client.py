from __future__ import annotations

import logging
from collections.abc import Mapping
from types import TracebackType

import httpx
from typing_extensions import Self

from ._resources import AsyncResources, Resources
from ._runtime import AsyncTransport, Settings, StaticCredentials, SyncTransport, select_hosts
from .errors import to_error

logger = logging.getLogger("mercury_banking")

ENVIRONMENTS: dict[str, dict[str, str]] = {
    "production": {"api": "https://api.mercury.com/api/v1", "vault": "https://vault-api.mercury.com/api/v1"},
    # Mercury documents no sandbox host for card details, so those calls go to the sandbox's own API host.
    "sandbox": {"api": "https://api-sandbox.mercury.com/api/v1", "vault": "https://api-sandbox.mercury.com/api/v1"},
}
"""The base URL of each host the API uses, by environment. `vault` serves only `cards.reveal`."""


def _settings(
    token: str,
    environment: str,
    hosts: Mapping[str, str] | None,
    user_agent: str | None,
    timeout: float,
    max_retries: int,
    retry_base_delay: float,
    rate_limit_wait: float,
    max_retry_wait: float,
) -> Settings:
    if not token:
        raise ValueError("token is required")
    urls = select_hosts(ENVIRONMENTS, environment, hosts)
    headers = {"Accept": "application/json"}
    if user_agent:
        headers["User-Agent"] = user_agent
    return Settings(
        base_url=urls["api"],
        credentials=StaticCredentials({"Authorization": f"Bearer {token}"}, secrets=[token]),
        headers=headers,
        to_error=to_error,
        logger=logger,
        timeout=timeout,
        max_retries=max_retries,
        retry_base_delay=retry_base_delay,
        rate_limit_wait=rate_limit_wait,
        max_retry_wait=max_retry_wait,
        hosts=urls,
    )


class MercuryClient(Resources):
    """Synchronous client.

    Args:
        token: Your API token, sent verbatim as a bearer token. The `secret-token:` prefix is part of it. It is
            never stored beyond this client or logged.
        environment: `production` or `sandbox`. A sandbox token works only in the sandbox.
        hosts: Your own base URL for each of `api` and `vault`, such as a mock's, instead of the environment's.
            The token is sent to them.
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
        token: str,
        *,
        environment: str = "production",
        hosts: Mapping[str, str] | None = None,
        user_agent: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_base_delay: float = 0.5,
        rate_limit_wait: float = 10.0,
        max_retry_wait: float = 60.0,
        http_transport: httpx.BaseTransport | None = None,
    ) -> None:
        settings = _settings(
            token,
            environment,
            hosts,
            user_agent,
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


class AsyncMercuryClient(AsyncResources):
    """Asynchronous client. Takes the same arguments as `MercuryClient`."""

    def __init__(
        self,
        token: str,
        *,
        environment: str = "production",
        hosts: Mapping[str, str] | None = None,
        user_agent: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_base_delay: float = 0.5,
        rate_limit_wait: float = 10.0,
        max_retry_wait: float = 60.0,
        http_transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        settings = _settings(
            token,
            environment,
            hosts,
            user_agent,
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
