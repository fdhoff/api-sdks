# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import Field, StrictInt
from typing_extensions import Annotated

from backmarket_seller import models as _models
from backmarket_seller._runtime import AsyncResource, FileInput, Operation, Param, Resource, checked
from backmarket_seller.models.country_code import CountryCode
from backmarket_seller.models.order import Order
from backmarket_seller.models.order_line_update import OrderLineUpdate
from backmarket_seller.models.order_page import OrderPage
from backmarket_seller.models.order_state import OrderState
from backmarket_seller.models.update_order import UpdateOrder
from backmarket_seller.models.updated_order_line import UpdatedOrderLine

_get_ws_list_order: Operation[OrderPage] = Operation(
    id="get-ws-list-order",
    method="GET",
    path="/ws/orders",
    resource="orders",
    name="list",
    params=(
        Param("date_creation", "date_creation", "query"),
        Param("date_modification", "date_modification", "query"),
        Param("country_code", "country_code", "query"),
        Param("state", "state", "query"),
        Param("page", "page", "query"),
        Param("page-size", "page_size", "query"),
    ),
    response=OrderPage,
    iterator="iter",
    item=_models.Order,
)
_get_ws_specific_order: Operation[Order] = Operation(
    id="get-ws-specific-order",
    method="GET",
    path="/ws/orders/{order_id}",
    resource="orders",
    name="get",
    params=(Param("order_id", "order_id", "path"),),
    response=Order,
)
_post_ws_specific_order_invoice: Operation[None] = Operation(
    id="post-ws-specific-order-invoice",
    method="POST",
    path="/ws/orders/{order_id}/invoice",
    resource="orders",
    name="upload_invoice",
    params=(
        Param("order_id", "order_id", "path"),
        Param("invoice", "invoice", "form"),
    ),
    response=None,
)
_update_ws_specific_order: Operation[Order] = Operation(
    id="update-ws-specific-order",
    method="POST",
    path="/ws/orders/{order_id}",
    resource="orders",
    name="update",
    params=(Param("order_id", "order_id", "path"),),
    response=Order,
)
_update_ws_specific_orderline: Operation[UpdatedOrderLine] = Operation(
    id="update-ws-specific-orderline",
    method="PATCH",
    path="/ws/orderlines/{orderline_id}",
    resource="orders",
    name="update_line",
    params=(Param("orderline_id", "orderline_id", "path"),),
    response=UpdatedOrderLine,
)

OPERATIONS = (
    _get_ws_list_order,
    _get_ws_specific_order,
    _post_ws_specific_order_invoice,
    _update_ws_specific_order,
    _update_ws_specific_orderline,
)


class OrdersApi(Resource):
    @checked
    def list(
        self,
        *,
        date_creation: Optional[datetime] = None,
        date_modification: Optional[datetime] = None,
        country_code: Optional[CountryCode] = None,
        state: Optional[OrderState] = None,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> OrderPage:
        """List one page of orders."""
        return self._call(
            _get_ws_list_order,
            date_creation=date_creation,
            date_modification=date_modification,
            country_code=country_code,
            state=state,
            page=page,
            page_size=page_size,
        )

    @checked
    def iter(
        self,
        *,
        date_creation: Optional[datetime] = None,
        date_modification: Optional[datetime] = None,
        country_code: Optional[CountryCode] = None,
        state: Optional[OrderState] = None,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> Iterator[_models.Order]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_list_order,
            date_creation=date_creation,
            date_modification=date_modification,
            country_code=country_code,
            state=state,
            page=page,
            page_size=page_size,
        )

    @checked
    def get(
        self,
        order_id: StrictInt,
    ) -> Order:
        """Get one order."""
        return self._call(
            _get_ws_specific_order,
            order_id=order_id,
        )

    @checked
    def upload_invoice(
        self,
        order_id: StrictInt,
        *,
        invoice: Optional[List[FileInput]] = None,
    ) -> None:
        """Upload invoices for an order."""
        return self._call(
            _post_ws_specific_order_invoice,
            order_id=order_id,
            invoice=invoice,
        )

    @checked
    def update(
        self,
        order_id: StrictInt,
        body: Optional[Union[UpdateOrder, Mapping[str, Any]]] = None,
    ) -> Order:
        """Update one order."""
        return self._call(
            _update_ws_specific_order,
            order_id=order_id,
            _body=body,
        )

    @checked
    def update_line(
        self,
        orderline_id: StrictInt,
        body: Optional[Union[OrderLineUpdate, Mapping[str, Any]]] = None,
    ) -> UpdatedOrderLine:
        """Update one order line."""
        return self._call(
            _update_ws_specific_orderline,
            orderline_id=orderline_id,
            _body=body,
        )


class AsyncOrdersApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        date_creation: Optional[datetime] = None,
        date_modification: Optional[datetime] = None,
        country_code: Optional[CountryCode] = None,
        state: Optional[OrderState] = None,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> OrderPage:
        """List one page of orders."""
        return await self._call(
            _get_ws_list_order,
            date_creation=date_creation,
            date_modification=date_modification,
            country_code=country_code,
            state=state,
            page=page,
            page_size=page_size,
        )

    @checked
    def iter(
        self,
        *,
        date_creation: Optional[datetime] = None,
        date_modification: Optional[datetime] = None,
        country_code: Optional[CountryCode] = None,
        state: Optional[OrderState] = None,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> AsyncIterator[_models.Order]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_list_order,
            date_creation=date_creation,
            date_modification=date_modification,
            country_code=country_code,
            state=state,
            page=page,
            page_size=page_size,
        )

    @checked
    async def get(
        self,
        order_id: StrictInt,
    ) -> Order:
        """Get one order."""
        return await self._call(
            _get_ws_specific_order,
            order_id=order_id,
        )

    @checked
    async def upload_invoice(
        self,
        order_id: StrictInt,
        *,
        invoice: Optional[List[FileInput]] = None,
    ) -> None:
        """Upload invoices for an order."""
        return await self._call(
            _post_ws_specific_order_invoice,
            order_id=order_id,
            invoice=invoice,
        )

    @checked
    async def update(
        self,
        order_id: StrictInt,
        body: Optional[Union[UpdateOrder, Mapping[str, Any]]] = None,
    ) -> Order:
        """Update one order."""
        return await self._call(
            _update_ws_specific_order,
            order_id=order_id,
            _body=body,
        )

    @checked
    async def update_line(
        self,
        orderline_id: StrictInt,
        body: Optional[Union[OrderLineUpdate, Mapping[str, Any]]] = None,
    ) -> UpdatedOrderLine:
        """Update one order line."""
        return await self._call(
            _update_ws_specific_orderline,
            orderline_id=orderline_id,
            _body=body,
        )
