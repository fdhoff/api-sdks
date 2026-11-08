# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.fulfillment import models as _models
from ebay_sell.fulfillment.models.issue_refund_request import IssueRefundRequest
from ebay_sell.fulfillment.models.order import Order
from ebay_sell.fulfillment.models.order_search_paged_collection import OrderSearchPagedCollection
from ebay_sell.fulfillment.models.refund import Refund

_get_order: Operation[Order] = Operation(
    id="getOrder",
    method="GET",
    path="/sell/fulfillment/v1/order/{orderId}",
    resource="orders",
    name="get",
    params=(
        Param("orderId", "order_id", "path"),
        Param("fieldGroups", "field_groups", "query"),
    ),
    response=Order,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_get_orders: Operation[OrderSearchPagedCollection] = Operation(
    id="getOrders",
    method="GET",
    path="/sell/fulfillment/v1/order",
    resource="orders",
    name="list",
    params=(
        Param("fieldGroups", "field_groups", "query"),
        Param("filter", "filter", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("orderIds", "order_ids", "query"),
    ),
    response=OrderSearchPagedCollection,
    returns_json=True,
    iterator="iter",
    item=_models.Order,
    paging=NextLink(
        items="orders",
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
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment",
                    "https://api.ebay.com/oauth/api_scope/sell.fulfillment.readonly",
                ),
            ),
        ),
    ),
    host="api",
)
_issue_refund: Operation[Refund] = Operation(
    id="issueRefund",
    method="POST",
    path="/sell/fulfillment/v1/order/{order_id}/issue_refund",
    resource="orders",
    name="issue_refund",
    params=(Param("order_id", "order_id", "path"),),
    response=Refund,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances",)),),),
    host="api",
)

OPERATIONS = (
    _get_order,
    _get_orders,
    _issue_refund,
)


class OrdersApi(Resource):
    @checked
    def get(
        self,
        order_id: StrictStr,
        *,
        field_groups: Optional[StrictStr] = None,
    ) -> Order:
        """Get one order."""
        return self._call(
            _get_order,
            order_id=order_id,
            field_groups=field_groups,
        )

    @checked
    def list(
        self,
        *,
        field_groups: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        order_ids: Optional[StrictStr] = None,
    ) -> OrderSearchPagedCollection:
        """List one page of the seller's orders."""
        return self._call(
            _get_orders,
            field_groups=field_groups,
            filter=filter,
            limit=limit,
            offset=offset,
            order_ids=order_ids,
        )

    @checked
    def iter(
        self,
        *,
        field_groups: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        order_ids: Optional[StrictStr] = None,
    ) -> Iterator[_models.Order]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_orders,
            field_groups=field_groups,
            filter=filter,
            limit=limit,
            offset=offset,
            order_ids=order_ids,
        )

    @checked
    def issue_refund(
        self,
        order_id: StrictStr,
        body: Optional[Union[IssueRefundRequest, Mapping[str, Any]]] = None,
    ) -> Refund:
        """Refund all or part of an order."""
        return self._call(
            _issue_refund,
            order_id=order_id,
            _body=body,
        )


class AsyncOrdersApi(AsyncResource):
    @checked
    async def get(
        self,
        order_id: StrictStr,
        *,
        field_groups: Optional[StrictStr] = None,
    ) -> Order:
        """Get one order."""
        return await self._call(
            _get_order,
            order_id=order_id,
            field_groups=field_groups,
        )

    @checked
    async def list(
        self,
        *,
        field_groups: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        order_ids: Optional[StrictStr] = None,
    ) -> OrderSearchPagedCollection:
        """List one page of the seller's orders."""
        return await self._call(
            _get_orders,
            field_groups=field_groups,
            filter=filter,
            limit=limit,
            offset=offset,
            order_ids=order_ids,
        )

    @checked
    def iter(
        self,
        *,
        field_groups: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        order_ids: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Order]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_orders,
            field_groups=field_groups,
            filter=filter,
            limit=limit,
            offset=offset,
            order_ids=order_ids,
        )

    @checked
    async def issue_refund(
        self,
        order_id: StrictStr,
        body: Optional[Union[IssueRefundRequest, Mapping[str, Any]]] = None,
    ) -> Refund:
        """Refund all or part of an order."""
        return await self._call(
            _issue_refund,
            order_id=order_id,
            _body=body,
        )
