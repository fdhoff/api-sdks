# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.account import models as _models
from ebay_sell.account.models.subscription_response import SubscriptionResponse

_get_subscription: Operation[SubscriptionResponse] = Operation(
    id="getSubscription",
    method="GET",
    path="/sell/account/v1/subscription",
    resource="subscriptions",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("continuation_token", "continuation_token", "query"),
    ),
    response=SubscriptionResponse,
    returns_json=True,
    iterator="iter",
    item=_models.Subscription,
    paging=NextLink(
        items="subscriptions",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.account",
                    "https://api.ebay.com/oauth/api_scope/sell.account.readonly",
                ),
            ),
        ),
    ),
    host="api",
)

OPERATIONS = (_get_subscription,)


class SubscriptionsApi(Resource):
    @checked
    def list(
        self,
        *,
        limit: Optional[StrictStr] = None,
        continuation_token: Optional[StrictStr] = None,
    ) -> SubscriptionResponse:
        """List one page of the seller's eBay subscriptions"""
        return self._call(
            _get_subscription,
            limit=limit,
            continuation_token=continuation_token,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[StrictStr] = None,
        continuation_token: Optional[StrictStr] = None,
    ) -> Iterator[_models.Subscription]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_subscription,
            limit=limit,
            continuation_token=continuation_token,
        )


class AsyncSubscriptionsApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        limit: Optional[StrictStr] = None,
        continuation_token: Optional[StrictStr] = None,
    ) -> SubscriptionResponse:
        """List one page of the seller's eBay subscriptions"""
        return await self._call(
            _get_subscription,
            limit=limit,
            continuation_token=continuation_token,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[StrictStr] = None,
        continuation_token: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Subscription]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_subscription,
            limit=limit,
            continuation_token=continuation_token,
        )
