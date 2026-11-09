from __future__ import annotations

import logging
from collections.abc import Callable, Mapping, Sequence
from types import TracebackType

import httpx
from typing_extensions import Self

from . import (
    account,
    account_v2,
    analytics,
    developer_analytics,
    feed,
    feedback,
    finances,
    fulfillment,
    identity,
    inventory,
    key_management,
    marketing,
    media,
    message,
    metadata,
    negotiation,
    notification,
    post_order,
    recommendation,
    stores,
    taxonomy,
)
from ._runtime import AsyncTransport, Settings, SyncTransport, select_hosts
from .errors import to_error
from .oauth import API_SCOPE, AsyncOAuth, EbayCredentials, OAuth, Token, _Config
from .signing import SigningKey

logger = logging.getLogger("ebay_sell")

ENVIRONMENTS: dict[str, dict[str, str]] = {
    "production": {"api": "https://api.ebay.com", "apiz": "https://apiz.ebay.com", "apim": "https://apim.ebay.com"},
    "sandbox": {
        "api": "https://api.sandbox.ebay.com",
        "apiz": "https://apiz.sandbox.ebay.com",
        "apim": "https://apim.sandbox.ebay.com",
    },
}
"""The base URL of each host the APIs use, by environment."""


def _header_defaults(marketplace_id: str | None, content_language: str | None) -> dict[str, str]:
    defaults = {"X-EBAY-C-MARKETPLACE-ID": marketplace_id, "Content-Language": content_language}
    return {name: value for name, value in defaults.items() if value}


def _settings(
    credentials: EbayCredentials,
    hosts: Mapping[str, str],
    header_defaults: Mapping[str, str],
    user_agent: str | None,
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
        base_url=hosts["api"],
        credentials=credentials,
        headers=headers,
        to_error=to_error,
        logger=logger,
        timeout=timeout,
        max_retries=max_retries,
        retry_base_delay=retry_base_delay,
        rate_limit_wait=rate_limit_wait,
        max_retry_wait=max_retry_wait,
        hosts=hosts,
        header_defaults=header_defaults,
    )


class _Options:
    """The arguments both clients share, checked once."""

    def __init__(
        self,
        client_id: str | None,
        client_secret: str | None,
        ru_name: str | None,
        app_token: str | None,
        user_token: str | None,
        refresh_token: str | None,
        on_token: Callable[[Token], object] | None,
        app_scopes: Sequence[str],
        user_scopes: Sequence[str] | None,
        environment: str,
        hosts: Mapping[str, str] | None,
        marketplace_id: str | None,
        content_language: str | None,
        signing_key: SigningKey | None,
        user_agent: str | None,
        timeout: float,
        max_retries: int,
        retry_base_delay: float,
        rate_limit_wait: float,
        max_retry_wait: float,
    ) -> None:
        if not any(scope.strip() for scope in app_scopes):
            raise ValueError("app_scopes needs at least one scope")
        signer = signing_key.signer() if signing_key is not None else None
        self.credentials = EbayCredentials(
            client_id,
            client_secret,
            app_token,
            user_token,
            refresh_token,
            on_token,
            signer,
            signing_key.jwe if signing_key is not None else None,
        )
        self.config = _Config(ru_name, tuple(app_scopes), tuple(user_scopes) if user_scopes else None, environment)
        self.settings = _settings(
            self.credentials,
            select_hosts(ENVIRONMENTS, environment, hosts),
            _header_defaults(marketplace_id, content_language),
            user_agent,
            timeout,
            max_retries,
            retry_base_delay,
            rate_limit_wait,
            max_retry_wait,
        )


class EbayClient:
    """Synchronous client for every API in this package, one attribute per API.

    Args:
        client_id: Your keyset's App ID. With `client_secret`, the client mints application tokens itself
            and can exchange and refresh user tokens.
        client_secret: Your keyset's Cert ID.
        ru_name: Your app's redirect URL name, for the authorization code grant.
        app_token: An application token to use instead of minting one.
        user_token: A user access token, sent on operations that need a seller's consent.
        refresh_token: Lets the client replace an expired user token by itself, once per call.
        on_token: Called with every new user token, from `oauth.exchange_code` and every refresh, so you can
            store it. It runs while the client holds its token locks, so it must not call `oauth` or make
            calls with this client, which would deadlock.
        app_scopes: The scopes of minted application tokens, at least one.
        user_scopes: The scopes to ask for when refreshing a user token. eBay keeps the original grant's when
            this is not given.
        environment: `production` or `sandbox`.
        hosts: Your own base URL for each of `api`, `apiz` and `apim`, such as a mock's, instead of the
            environment's. Your credentials are sent to them.
        marketplace_id: Sent as `X-EBAY-C-MARKETPLACE-ID` on operations that take it, unless a call passes
            its own.
        content_language: Sent as `Content-Language` on operations that take it, unless a call passes its own.
        signing_key: Signs every request, as eBay requires of EU and UK sellers on some calls.
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
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        ru_name: str | None = None,
        app_token: str | None = None,
        user_token: str | None = None,
        refresh_token: str | None = None,
        on_token: Callable[[Token], object] | None = None,
        app_scopes: Sequence[str] = (API_SCOPE,),
        user_scopes: Sequence[str] | None = None,
        environment: str = "production",
        hosts: Mapping[str, str] | None = None,
        marketplace_id: str | None = None,
        content_language: str | None = None,
        signing_key: SigningKey | None = None,
        user_agent: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_base_delay: float = 0.5,
        rate_limit_wait: float = 10.0,
        max_retry_wait: float = 60.0,
        http_transport: httpx.BaseTransport | None = None,
    ) -> None:
        options = _Options(
            client_id,
            client_secret,
            ru_name,
            app_token,
            user_token,
            refresh_token,
            on_token,
            app_scopes,
            user_scopes,
            environment,
            hosts,
            marketplace_id,
            content_language,
            signing_key,
            user_agent,
            timeout,
            max_retries,
            retry_base_delay,
            rate_limit_wait,
            max_retry_wait,
        )
        transport = self._transport = SyncTransport(options.settings, http_transport)
        self.account = account.Resources(transport)
        self.account_v2 = account_v2.Resources(transport)
        self.analytics = analytics.Resources(transport)
        self.feed = feed.Resources(transport)
        self.finances = finances.Resources(transport)
        self.fulfillment = fulfillment.Resources(transport)
        self.inventory = inventory.Resources(transport)
        self.marketing = marketing.Resources(transport)
        self.metadata = metadata.Resources(transport)
        self.negotiation = negotiation.Resources(transport)
        self.recommendation = recommendation.Resources(transport)
        self.stores = stores.Resources(transport)
        self.post_order = post_order.Resources(transport)
        self.feedback = feedback.Resources(transport)
        self.identity = identity.Resources(transport)
        self.media = media.Resources(transport)
        self.message = message.Resources(transport)
        self.notification = notification.Resources(transport)
        self.taxonomy = taxonomy.Resources(transport)
        self.developer_analytics = developer_analytics.Resources(transport)
        self.key_management = key_management.Resources(transport)
        self.oauth = OAuth(options.credentials, transport, options.config)
        options.credentials.minter = self.oauth.app_token
        options.credentials.refresher = self.oauth.refresh

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


class AsyncEbayClient:
    """Asynchronous client. Takes the same arguments as `EbayClient`."""

    def __init__(
        self,
        *,
        client_id: str | None = None,
        client_secret: str | None = None,
        ru_name: str | None = None,
        app_token: str | None = None,
        user_token: str | None = None,
        refresh_token: str | None = None,
        on_token: Callable[[Token], object] | None = None,
        app_scopes: Sequence[str] = (API_SCOPE,),
        user_scopes: Sequence[str] | None = None,
        environment: str = "production",
        hosts: Mapping[str, str] | None = None,
        marketplace_id: str | None = None,
        content_language: str | None = None,
        signing_key: SigningKey | None = None,
        user_agent: str | None = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        retry_base_delay: float = 0.5,
        rate_limit_wait: float = 10.0,
        max_retry_wait: float = 60.0,
        http_transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        options = _Options(
            client_id,
            client_secret,
            ru_name,
            app_token,
            user_token,
            refresh_token,
            on_token,
            app_scopes,
            user_scopes,
            environment,
            hosts,
            marketplace_id,
            content_language,
            signing_key,
            user_agent,
            timeout,
            max_retries,
            retry_base_delay,
            rate_limit_wait,
            max_retry_wait,
        )
        transport = self._transport = AsyncTransport(options.settings, http_transport)
        self.account = account.AsyncResources(transport)
        self.account_v2 = account_v2.AsyncResources(transport)
        self.analytics = analytics.AsyncResources(transport)
        self.feed = feed.AsyncResources(transport)
        self.finances = finances.AsyncResources(transport)
        self.fulfillment = fulfillment.AsyncResources(transport)
        self.inventory = inventory.AsyncResources(transport)
        self.marketing = marketing.AsyncResources(transport)
        self.metadata = metadata.AsyncResources(transport)
        self.negotiation = negotiation.AsyncResources(transport)
        self.recommendation = recommendation.AsyncResources(transport)
        self.stores = stores.AsyncResources(transport)
        self.post_order = post_order.AsyncResources(transport)
        self.feedback = feedback.AsyncResources(transport)
        self.identity = identity.AsyncResources(transport)
        self.media = media.AsyncResources(transport)
        self.message = message.AsyncResources(transport)
        self.notification = notification.AsyncResources(transport)
        self.taxonomy = taxonomy.AsyncResources(transport)
        self.developer_analytics = developer_analytics.AsyncResources(transport)
        self.key_management = key_management.AsyncResources(transport)
        self.oauth = AsyncOAuth(options.credentials, transport, options.config)
        options.credentials.minter = self.oauth.app_token
        options.credentials.refresher = self.oauth.refresh

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
