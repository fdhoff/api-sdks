# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
from typing import AsyncIterator, Iterator, Optional

from pydantic import StrictBool, StrictInt

from backmarket_seller import models as _models
from backmarket_seller._runtime import AsyncResource, Operation, Param, Resource, checked
from backmarket_seller.models.delivery import Delivery
from backmarket_seller.models.delivery_page import DeliveryPage
from backmarket_seller.models.return_page import ReturnPage
from backmarket_seller.models.return_shipment import ReturnShipment

_get_deliveries: Operation[DeliveryPage] = Operation(
    id="GetDeliveries",
    method="GET",
    path="/ws/shipping/v1/deliveries",
    resource="shipping",
    name="list_deliveries",
    params=(
        Param("page", "page", "query"),
        Param("order_id", "order_id", "query"),
        Param("start_date", "start_date", "query"),
        Param("end_date", "end_date", "query"),
        Param("pickup_start_date", "pickup_start_date", "query"),
        Param("pickup_end_date", "pickup_end_date", "query"),
        Param("order_state", "order_state", "query"),
        Param("hub_scanned", "hub_scanned", "query"),
    ),
    response=DeliveryPage,
    returns_json=True,
    iterator="iter_deliveries",
    item=_models.Delivery,
)
_get_delivery: Operation[Delivery] = Operation(
    id="GetDelivery",
    method="GET",
    path="/ws/shipping/v1/deliveries/{id}",
    resource="shipping",
    name="get_delivery",
    params=(Param("id", "id", "path"),),
    response=Delivery,
    returns_json=True,
)
_get_return: Operation[ReturnShipment] = Operation(
    id="GetReturn",
    method="GET",
    path="/ws/shipping/v1/returns/{id}",
    resource="shipping",
    name="get_return",
    params=(Param("id", "id", "path"),),
    response=ReturnShipment,
    returns_json=True,
)
_get_returns: Operation[ReturnPage] = Operation(
    id="GetReturns",
    method="GET",
    path="/ws/shipping/v1/returns",
    resource="shipping",
    name="list_returns",
    params=(
        Param("page", "page", "query"),
        Param("order_id", "order_id", "query"),
        Param("start_date", "start_date", "query"),
        Param("end_date", "end_date", "query"),
        Param("pickup_start_date", "pickup_start_date", "query"),
        Param("pickup_end_date", "pickup_end_date", "query"),
        Param("order_state", "order_state", "query"),
        Param("hub_scanned", "hub_scanned", "query"),
    ),
    response=ReturnPage,
    returns_json=True,
    iterator="iter_returns",
    item=_models.ReturnShipment,
)

OPERATIONS = (
    _get_deliveries,
    _get_delivery,
    _get_return,
    _get_returns,
)


class ShippingApi(Resource):
    @checked
    def list_deliveries(
        self,
        *,
        page: Optional[StrictInt] = None,
        order_id: Optional[StrictInt] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        pickup_start_date: Optional[datetime] = None,
        pickup_end_date: Optional[datetime] = None,
        order_state: Optional[StrictInt] = None,
        hub_scanned: Optional[StrictBool] = None,
    ) -> DeliveryPage:
        """List one page of deliveries."""
        return self._call(
            _get_deliveries,
            page=page,
            order_id=order_id,
            start_date=start_date,
            end_date=end_date,
            pickup_start_date=pickup_start_date,
            pickup_end_date=pickup_end_date,
            order_state=order_state,
            hub_scanned=hub_scanned,
        )

    @checked
    def iter_deliveries(
        self,
        *,
        page: Optional[StrictInt] = None,
        order_id: Optional[StrictInt] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        pickup_start_date: Optional[datetime] = None,
        pickup_end_date: Optional[datetime] = None,
        order_state: Optional[StrictInt] = None,
        hub_scanned: Optional[StrictBool] = None,
    ) -> Iterator[_models.Delivery]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_deliveries,
            page=page,
            order_id=order_id,
            start_date=start_date,
            end_date=end_date,
            pickup_start_date=pickup_start_date,
            pickup_end_date=pickup_end_date,
            order_state=order_state,
            hub_scanned=hub_scanned,
        )

    @checked
    def get_delivery(
        self,
        id: StrictInt,
    ) -> Delivery:
        """Get one delivery."""
        return self._call(
            _get_delivery,
            id=id,
        )

    @checked
    def get_return(
        self,
        id: StrictInt,
    ) -> ReturnShipment:
        """Get one return."""
        return self._call(
            _get_return,
            id=id,
        )

    @checked
    def list_returns(
        self,
        *,
        page: Optional[StrictInt] = None,
        order_id: Optional[StrictInt] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        pickup_start_date: Optional[datetime] = None,
        pickup_end_date: Optional[datetime] = None,
        order_state: Optional[StrictInt] = None,
        hub_scanned: Optional[StrictBool] = None,
    ) -> ReturnPage:
        """List one page of returns."""
        return self._call(
            _get_returns,
            page=page,
            order_id=order_id,
            start_date=start_date,
            end_date=end_date,
            pickup_start_date=pickup_start_date,
            pickup_end_date=pickup_end_date,
            order_state=order_state,
            hub_scanned=hub_scanned,
        )

    @checked
    def iter_returns(
        self,
        *,
        page: Optional[StrictInt] = None,
        order_id: Optional[StrictInt] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        pickup_start_date: Optional[datetime] = None,
        pickup_end_date: Optional[datetime] = None,
        order_state: Optional[StrictInt] = None,
        hub_scanned: Optional[StrictBool] = None,
    ) -> Iterator[_models.ReturnShipment]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_returns,
            page=page,
            order_id=order_id,
            start_date=start_date,
            end_date=end_date,
            pickup_start_date=pickup_start_date,
            pickup_end_date=pickup_end_date,
            order_state=order_state,
            hub_scanned=hub_scanned,
        )


class AsyncShippingApi(AsyncResource):
    @checked
    async def list_deliveries(
        self,
        *,
        page: Optional[StrictInt] = None,
        order_id: Optional[StrictInt] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        pickup_start_date: Optional[datetime] = None,
        pickup_end_date: Optional[datetime] = None,
        order_state: Optional[StrictInt] = None,
        hub_scanned: Optional[StrictBool] = None,
    ) -> DeliveryPage:
        """List one page of deliveries."""
        return await self._call(
            _get_deliveries,
            page=page,
            order_id=order_id,
            start_date=start_date,
            end_date=end_date,
            pickup_start_date=pickup_start_date,
            pickup_end_date=pickup_end_date,
            order_state=order_state,
            hub_scanned=hub_scanned,
        )

    @checked
    def iter_deliveries(
        self,
        *,
        page: Optional[StrictInt] = None,
        order_id: Optional[StrictInt] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        pickup_start_date: Optional[datetime] = None,
        pickup_end_date: Optional[datetime] = None,
        order_state: Optional[StrictInt] = None,
        hub_scanned: Optional[StrictBool] = None,
    ) -> AsyncIterator[_models.Delivery]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_deliveries,
            page=page,
            order_id=order_id,
            start_date=start_date,
            end_date=end_date,
            pickup_start_date=pickup_start_date,
            pickup_end_date=pickup_end_date,
            order_state=order_state,
            hub_scanned=hub_scanned,
        )

    @checked
    async def get_delivery(
        self,
        id: StrictInt,
    ) -> Delivery:
        """Get one delivery."""
        return await self._call(
            _get_delivery,
            id=id,
        )

    @checked
    async def get_return(
        self,
        id: StrictInt,
    ) -> ReturnShipment:
        """Get one return."""
        return await self._call(
            _get_return,
            id=id,
        )

    @checked
    async def list_returns(
        self,
        *,
        page: Optional[StrictInt] = None,
        order_id: Optional[StrictInt] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        pickup_start_date: Optional[datetime] = None,
        pickup_end_date: Optional[datetime] = None,
        order_state: Optional[StrictInt] = None,
        hub_scanned: Optional[StrictBool] = None,
    ) -> ReturnPage:
        """List one page of returns."""
        return await self._call(
            _get_returns,
            page=page,
            order_id=order_id,
            start_date=start_date,
            end_date=end_date,
            pickup_start_date=pickup_start_date,
            pickup_end_date=pickup_end_date,
            order_state=order_state,
            hub_scanned=hub_scanned,
        )

    @checked
    def iter_returns(
        self,
        *,
        page: Optional[StrictInt] = None,
        order_id: Optional[StrictInt] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        pickup_start_date: Optional[datetime] = None,
        pickup_end_date: Optional[datetime] = None,
        order_state: Optional[StrictInt] = None,
        hub_scanned: Optional[StrictBool] = None,
    ) -> AsyncIterator[_models.ReturnShipment]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_returns,
            page=page,
            order_id=order_id,
            start_date=start_date,
            end_date=end_date,
            pickup_start_date=pickup_start_date,
            pickup_end_date=pickup_end_date,
            order_state=order_state,
            hub_scanned=hub_scanned,
        )
