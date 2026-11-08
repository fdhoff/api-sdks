# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, NextLink, Operation, Param, Resource, Scheme, checked
from ebay_sell.finances import models as _models
from ebay_sell.finances.models.order_earning import OrderEarning
from ebay_sell.finances.models.order_earnings import OrderEarnings
from ebay_sell.finances.models.order_earnings_summary import OrderEarningsSummary

_get_order_earnings: Operation[OrderEarnings] = Operation(
    id="getOrderEarnings",
    method="GET",
    path="/sell/finances/v1/order_earnings",
    resource="order_earnings",
    name="list",
    params=(
        Param("filter", "filter", "query"),
        Param("limit", "limit", "query"),
        Param("offset", "offset", "query"),
        Param("sort", "sort", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=OrderEarnings,
    returns_json=True,
    iterator="iter",
    item=_models.OrderEarning,
    paging=NextLink(
        items="orders",
        link="next",
        params=(
            "offset",
            "limit",
            "continuation_token",
        ),
    ),
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances.earnings.read",)),),),
    host="apiz",
)
_get_order_earnings_by_id: Operation[OrderEarning] = Operation(
    id="getOrderEarningsById",
    method="GET",
    path="/sell/finances/v1/order_earnings/{order_id}",
    resource="order_earnings",
    name="get",
    params=(
        Param("order_id", "order_id", "path"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=OrderEarning,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances.earnings.read",)),),),
    host="apiz",
)
_get_order_earnings_summary: Operation[OrderEarningsSummary] = Operation(
    id="getOrderEarningsSummary",
    method="GET",
    path="/sell/finances/v1/order_earnings_summary",
    resource="order_earnings",
    name="get_summary",
    params=(
        Param("filter", "filter", "query"),
        Param("X-EBAY-C-MARKETPLACE-ID", "x_ebay_c_marketplace_id", "header"),
    ),
    response=OrderEarningsSummary,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.finances.earnings.read",)),),),
    host="apiz",
)

OPERATIONS = (
    _get_order_earnings,
    _get_order_earnings_by_id,
    _get_order_earnings_summary,
)


class OrderEarningsApi(Resource):
    @checked
    def list(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> OrderEarnings:
        """List one page of the seller's earnings by order."""
        return self._call(
            _get_order_earnings,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def iter(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.OrderEarning]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_order_earnings,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get(
        self,
        order_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> OrderEarning:
        """Get the seller's earnings from one order."""
        return self._call(
            _get_order_earnings_by_id,
            order_id=order_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def get_summary(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
    ) -> OrderEarningsSummary:
        """Sum the seller's earnings across orders."""
        return self._call(
            _get_order_earnings_summary,
            filter=filter,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )


class AsyncOrderEarningsApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> OrderEarnings:
        """List one page of the seller's earnings by order."""
        return await self._call(
            _get_order_earnings,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    def iter(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
        limit: Optional[StrictStr] = None,
        offset: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.OrderEarning]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_order_earnings,
            filter=filter,
            limit=limit,
            offset=offset,
            sort=sort,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get(
        self,
        order_id: StrictStr,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
    ) -> OrderEarning:
        """Get the seller's earnings from one order."""
        return await self._call(
            _get_order_earnings_by_id,
            order_id=order_id,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )

    @checked
    async def get_summary(
        self,
        *,
        x_ebay_c_marketplace_id: Optional[StrictStr] = None,
        filter: Optional[StrictStr] = None,
    ) -> OrderEarningsSummary:
        """Sum the seller's earnings across orders."""
        return await self._call(
            _get_order_earnings_summary,
            filter=filter,
            x_ebay_c_marketplace_id=x_ebay_c_marketplace_id,
        )
