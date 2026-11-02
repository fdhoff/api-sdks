# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Dict, Iterator, List, Mapping, Optional, Tuple, Union

from pydantic import Field, StrictFloat, StrictInt, StrictStr
from typing_extensions import Annotated

from datetime import datetime
from pydantic import StrictBool, StrictInt, field_validator
from typing import Optional
from backmarket_seller.models.delivery import Delivery
from backmarket_seller.models.delivery_page import DeliveryPage
from backmarket_seller.models.return_page import ReturnPage
from backmarket_seller.models.return_shipment import ReturnShipment
from backmarket_seller.models import Delivery
from backmarket_seller.models import ReturnShipment
from backmarket_seller._runtime import AsyncResource, FileInput, Operation, Param, Resource

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
    iterator="iter_deliveries",
    item=Delivery,
)
_get_delivery: Operation[Delivery] = Operation(
    id="GetDelivery",
    method="GET",
    path="/ws/shipping/v1/deliveries/{id}",
    resource="shipping",
    name="get_delivery",
    params=(Param("id", "id", "path"),),
    response=Delivery,
)
_get_return: Operation[ReturnShipment] = Operation(
    id="GetReturn",
    method="GET",
    path="/ws/shipping/v1/returns/{id}",
    resource="shipping",
    name="get_return",
    params=(Param("id", "id", "path"),),
    response=ReturnShipment,
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
    iterator="iter_returns",
    item=ReturnShipment,
)

OPERATIONS = (
    _get_deliveries,
    _get_delivery,
    _get_return,
    _get_returns,
)


class ShippingApi(Resource):
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
    ) -> Iterator[Delivery]:
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

    def get_delivery(
        self,
        id: StrictInt,
    ) -> Delivery:
        """Get one delivery."""
        return self._call(
            _get_delivery,
            id=id,
        )

    def get_return(
        self,
        id: StrictInt,
    ) -> ReturnShipment:
        """Get one return."""
        return self._call(
            _get_return,
            id=id,
        )

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
    ) -> Iterator[ReturnShipment]:
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
    ) -> AsyncIterator[Delivery]:
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

    async def get_delivery(
        self,
        id: StrictInt,
    ) -> Delivery:
        """Get one delivery."""
        return await self._call(
            _get_delivery,
            id=id,
        )

    async def get_return(
        self,
        id: StrictInt,
    ) -> ReturnShipment:
        """Get one return."""
        return await self._call(
            _get_return,
            id=id,
        )

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
    ) -> AsyncIterator[ReturnShipment]:
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
