# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.notification import models as _models
from ebay_sell.notification.models.create_subscription_filter_request import CreateSubscriptionFilterRequest
from ebay_sell.notification.models.create_subscription_request import CreateSubscriptionRequest
from ebay_sell.notification.models.subscription import Subscription
from ebay_sell.notification.models.subscription_filter import SubscriptionFilter
from ebay_sell.notification.models.subscription_search_response import SubscriptionSearchResponse
from ebay_sell.notification.models.update_subscription_request import UpdateSubscriptionRequest

_create_subscription: Operation[object] = Operation(
    id="createSubscription",
    method="POST",
    path="/commerce/notification/v1/subscription",
    resource="subscriptions",
    name="create",
    params=(),
    response=object,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription",
                ),
            ),
        ),
    ),
    host="api",
)
_create_subscription_filter: Operation[object] = Operation(
    id="createSubscriptionFilter",
    method="POST",
    path="/commerce/notification/v1/subscription/{subscription_id}/filter",
    resource="subscriptions",
    name="create_filter",
    params=(Param("subscription_id", "subscription_id", "path"),),
    response=object,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription",
                ),
            ),
        ),
    ),
    host="api",
)
_delete_subscription: Operation[None] = Operation(
    id="deleteSubscription",
    method="DELETE",
    path="/commerce/notification/v1/subscription/{subscription_id}",
    resource="subscriptions",
    name="delete",
    params=(Param("subscription_id", "subscription_id", "path"),),
    response=None,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription",
                ),
            ),
        ),
    ),
    host="api",
)
_delete_subscription_filter: Operation[None] = Operation(
    id="deleteSubscriptionFilter",
    method="DELETE",
    path="/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}",
    resource="subscriptions",
    name="delete_filter",
    params=(
        Param("filter_id", "filter_id", "path"),
        Param("subscription_id", "subscription_id", "path"),
    ),
    response=None,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription",
                ),
            ),
        ),
    ),
    host="api",
)
_disable_subscription: Operation[None] = Operation(
    id="disableSubscription",
    method="POST",
    path="/commerce/notification/v1/subscription/{subscription_id}/disable",
    resource="subscriptions",
    name="disable",
    params=(Param("subscription_id", "subscription_id", "path"),),
    response=None,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription",
                ),
            ),
        ),
    ),
    host="api",
)
_enable_subscription: Operation[None] = Operation(
    id="enableSubscription",
    method="POST",
    path="/commerce/notification/v1/subscription/{subscription_id}/enable",
    resource="subscriptions",
    name="enable",
    params=(Param("subscription_id", "subscription_id", "path"),),
    response=None,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription",
                ),
            ),
        ),
    ),
    host="api",
)
_get_subscription: Operation[Subscription] = Operation(
    id="getSubscription",
    method="GET",
    path="/commerce/notification/v1/subscription/{subscription_id}",
    resource="subscriptions",
    name="get",
    params=(Param("subscription_id", "subscription_id", "path"),),
    response=Subscription,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription",
                ),
            ),
        ),
    ),
    host="api",
)
_get_subscription_filter: Operation[SubscriptionFilter] = Operation(
    id="getSubscriptionFilter",
    method="GET",
    path="/commerce/notification/v1/subscription/{subscription_id}/filter/{filter_id}",
    resource="subscriptions",
    name="get_filter",
    params=(
        Param("filter_id", "filter_id", "path"),
        Param("subscription_id", "subscription_id", "path"),
    ),
    response=SubscriptionFilter,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription",
                ),
            ),
        ),
    ),
    host="api",
)
_get_subscriptions: Operation[SubscriptionSearchResponse] = Operation(
    id="getSubscriptions",
    method="GET",
    path="/commerce/notification/v1/subscription",
    resource="subscriptions",
    name="list",
    params=(
        Param("continuation_token", "continuation_token", "query"),
        Param("limit", "limit", "query"),
    ),
    response=SubscriptionSearchResponse,
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
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription.readonly",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription",
                ),
            ),
        ),
    ),
    host="api",
)
_test_subscription: Operation[None] = Operation(
    id="testSubscription",
    method="POST",
    path="/commerce/notification/v1/subscription/{subscription_id}/test",
    resource="subscriptions",
    name="test",
    params=(Param("subscription_id", "subscription_id", "path"),),
    response=None,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription",
                ),
            ),
        ),
    ),
    host="api",
)
_update_subscription: Operation[None] = Operation(
    id="updateSubscription",
    method="PUT",
    path="/commerce/notification/v1/subscription/{subscription_id}",
    resource="subscriptions",
    name="update",
    params=(Param("subscription_id", "subscription_id", "path"),),
    response=None,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/commerce.notification.subscription",
                ),
            ),
        ),
    ),
    host="api",
)

OPERATIONS = (
    _create_subscription,
    _create_subscription_filter,
    _delete_subscription,
    _delete_subscription_filter,
    _disable_subscription,
    _enable_subscription,
    _get_subscription,
    _get_subscription_filter,
    _get_subscriptions,
    _test_subscription,
    _update_subscription,
)


class SubscriptionsApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[CreateSubscriptionRequest, Mapping[str, Any]]] = None,
    ) -> object:
        """Subscribe to a notification topic."""
        return self._call(
            _create_subscription,
            _body=body,
        )

    @checked
    def create_filter(
        self,
        subscription_id: StrictStr,
        body: Optional[Union[CreateSubscriptionFilterRequest, Mapping[str, Any]]] = None,
    ) -> object:
        """Add a filter to a subscription."""
        return self._call(
            _create_subscription_filter,
            subscription_id=subscription_id,
            _body=body,
        )

    @checked
    def delete(
        self,
        subscription_id: StrictStr,
    ) -> None:
        """Delete a subscription."""
        return self._call(
            _delete_subscription,
            subscription_id=subscription_id,
        )

    @checked
    def delete_filter(
        self,
        filter_id: StrictStr,
        subscription_id: StrictStr,
    ) -> None:
        """Delete a filter from a subscription."""
        return self._call(
            _delete_subscription_filter,
            filter_id=filter_id,
            subscription_id=subscription_id,
        )

    @checked
    def disable(
        self,
        subscription_id: StrictStr,
    ) -> None:
        """Stop sending a subscription's notifications."""
        return self._call(
            _disable_subscription,
            subscription_id=subscription_id,
        )

    @checked
    def enable(
        self,
        subscription_id: StrictStr,
    ) -> None:
        """Resume sending a subscription's notifications."""
        return self._call(
            _enable_subscription,
            subscription_id=subscription_id,
        )

    @checked
    def get(
        self,
        subscription_id: StrictStr,
    ) -> Subscription:
        """Get one subscription."""
        return self._call(
            _get_subscription,
            subscription_id=subscription_id,
        )

    @checked
    def get_filter(
        self,
        filter_id: StrictStr,
        subscription_id: StrictStr,
    ) -> SubscriptionFilter:
        """Get one filter of a subscription."""
        return self._call(
            _get_subscription_filter,
            filter_id=filter_id,
            subscription_id=subscription_id,
        )

    @checked
    def list(
        self,
        *,
        continuation_token: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
    ) -> SubscriptionSearchResponse:
        """List one page of the app's subscriptions."""
        return self._call(
            _get_subscriptions,
            continuation_token=continuation_token,
            limit=limit,
        )

    @checked
    def iter(
        self,
        *,
        continuation_token: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
    ) -> Iterator[_models.Subscription]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_subscriptions,
            continuation_token=continuation_token,
            limit=limit,
        )

    @checked
    def test(
        self,
        subscription_id: StrictStr,
    ) -> None:
        """Send a test notification to a subscription's destination."""
        return self._call(
            _test_subscription,
            subscription_id=subscription_id,
        )

    @checked
    def update(
        self,
        subscription_id: StrictStr,
        body: Optional[Union[UpdateSubscriptionRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Update a subscription."""
        return self._call(
            _update_subscription,
            subscription_id=subscription_id,
            _body=body,
        )


class AsyncSubscriptionsApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[CreateSubscriptionRequest, Mapping[str, Any]]] = None,
    ) -> object:
        """Subscribe to a notification topic."""
        return await self._call(
            _create_subscription,
            _body=body,
        )

    @checked
    async def create_filter(
        self,
        subscription_id: StrictStr,
        body: Optional[Union[CreateSubscriptionFilterRequest, Mapping[str, Any]]] = None,
    ) -> object:
        """Add a filter to a subscription."""
        return await self._call(
            _create_subscription_filter,
            subscription_id=subscription_id,
            _body=body,
        )

    @checked
    async def delete(
        self,
        subscription_id: StrictStr,
    ) -> None:
        """Delete a subscription."""
        return await self._call(
            _delete_subscription,
            subscription_id=subscription_id,
        )

    @checked
    async def delete_filter(
        self,
        filter_id: StrictStr,
        subscription_id: StrictStr,
    ) -> None:
        """Delete a filter from a subscription."""
        return await self._call(
            _delete_subscription_filter,
            filter_id=filter_id,
            subscription_id=subscription_id,
        )

    @checked
    async def disable(
        self,
        subscription_id: StrictStr,
    ) -> None:
        """Stop sending a subscription's notifications."""
        return await self._call(
            _disable_subscription,
            subscription_id=subscription_id,
        )

    @checked
    async def enable(
        self,
        subscription_id: StrictStr,
    ) -> None:
        """Resume sending a subscription's notifications."""
        return await self._call(
            _enable_subscription,
            subscription_id=subscription_id,
        )

    @checked
    async def get(
        self,
        subscription_id: StrictStr,
    ) -> Subscription:
        """Get one subscription."""
        return await self._call(
            _get_subscription,
            subscription_id=subscription_id,
        )

    @checked
    async def get_filter(
        self,
        filter_id: StrictStr,
        subscription_id: StrictStr,
    ) -> SubscriptionFilter:
        """Get one filter of a subscription."""
        return await self._call(
            _get_subscription_filter,
            filter_id=filter_id,
            subscription_id=subscription_id,
        )

    @checked
    async def list(
        self,
        *,
        continuation_token: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
    ) -> SubscriptionSearchResponse:
        """List one page of the app's subscriptions."""
        return await self._call(
            _get_subscriptions,
            continuation_token=continuation_token,
            limit=limit,
        )

    @checked
    def iter(
        self,
        *,
        continuation_token: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Subscription]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_subscriptions,
            continuation_token=continuation_token,
            limit=limit,
        )

    @checked
    async def test(
        self,
        subscription_id: StrictStr,
    ) -> None:
        """Send a test notification to a subscription's destination."""
        return await self._call(
            _test_subscription,
            subscription_id=subscription_id,
        )

    @checked
    async def update(
        self,
        subscription_id: StrictStr,
        body: Optional[Union[UpdateSubscriptionRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Update a subscription."""
        return await self._call(
            _update_subscription,
            subscription_id=subscription_id,
            _body=body,
        )
