# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union

from pydantic import Field, StrictInt, StrictStr
from typing_extensions import Annotated

from mirakl_seller import models as _models
from mirakl_seller._runtime import (
    AsyncResource,
    Cursor,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from mirakl_seller.models.st01_request import ST01Request
from mirakl_seller.models.st01_response201 import ST01Response201
from mirakl_seller.models.st06_request import ST06Request
from mirakl_seller.models.st06_response200 import ST06Response200
from mirakl_seller.models.st07_request import ST07Request
from mirakl_seller.models.st07_response200 import ST07Response200
from mirakl_seller.models.st11_response200 import ST11Response200
from mirakl_seller.models.st12_response200 import ST12Response200
from mirakl_seller.models.st23_request import ST23Request
from mirakl_seller.models.st23_response200 import ST23Response200
from mirakl_seller.models.st24_request import ST24Request
from mirakl_seller.models.st24_response200 import ST24Response200
from mirakl_seller.models.st26_request import ST26Request
from mirakl_seller.models.st26_response200 import ST26Response200
from mirakl_seller.models.st31_request import ST31Request
from mirakl_seller.models.st31_response200 import ST31Response200
from mirakl_seller.models.st41_request import ST41Request
from mirakl_seller.models.st41_response200 import ST41Response200
from mirakl_seller.models.st42_response200 import ST42Response200
from mirakl_seller.models.st51_request import ST51Request
from mirakl_seller.models.st51_response200 import ST51Response200
from mirakl_seller.models.st52_response200 import ST52Response200

_s_t01: Operation[ST01Response201] = Operation(
    id="ST01",
    method="POST",
    path="/api/shipments",
    resource="shipments",
    name="create",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=ST01Response201,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SHIP",
                ),
            ),
        ),
    ),
)
_s_t06: Operation[ST06Response200] = Operation(
    id="ST06",
    method="PUT",
    path="/api/shipments/delete",
    resource="shipments",
    name="delete",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=ST06Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SHIPMENT_DELETE",
                ),
            ),
        ),
    ),
)
_s_t07: Operation[ST07Response200] = Operation(
    id="ST07",
    method="PUT",
    path="/api/shipments",
    resource="shipments",
    name="update_shipping_origin",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=ST07Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SHIPMENT_WRITE",
                ),
            ),
        ),
    ),
)
_s_t11: Operation[ST11Response200] = Operation(
    id="ST11",
    method="GET",
    path="/api/shipments",
    resource="shipments",
    name="list",
    params=(
        Param("order_id", "order_id", "query"),
        Param("shipment_state_code", "shipment_state_code", "query"),
        Param("shipment_customer_debit_state_code", "shipment_customer_debit_state_code", "query"),
        Param("last_updated_from", "last_updated_from", "query"),
        Param("last_updated_to", "last_updated_to", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
        Param("sort", "sort", "query"),
    ),
    response=ST11Response200,
    returns_json=True,
    iterator="iter",
    item=_models.ST11Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_READ",
                ),
            ),
        ),
    ),
)
_s_t12: Operation[ST12Response200] = Operation(
    id="ST12",
    method="GET",
    path="/api/shipments/items_to_ship",
    resource="shipments",
    name="list_items_to_ship",
    params=(
        Param("order_id", "order_id", "query"),
        Param("fulfillment_center_code", "fulfillment_center_code", "query"),
        Param("shipping_date_from", "shipping_date_from", "query"),
        Param("shipping_date_to", "shipping_date_to", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
        Param("sort", "sort", "query"),
    ),
    response=ST12Response200,
    returns_json=True,
    iterator="iter_items_to_ship",
    item=_models.ST12Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_READ",
                    "ROLE_PARTNER_ORDER_SHIPMENT_READ",
                ),
            ),
        ),
    ),
)
_s_t23: Operation[ST23Response200] = Operation(
    id="ST23",
    method="POST",
    path="/api/shipments/tracking",
    resource="shipments",
    name="update_tracking",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=ST23Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_TRACKING_WRITE",
                ),
            ),
        ),
    ),
)
_s_t24: Operation[ST24Response200] = Operation(
    id="ST24",
    method="PUT",
    path="/api/shipments/ship",
    resource="shipments",
    name="ship",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=ST24Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SHIP",
                ),
            ),
        ),
    ),
)
_s_t26: Operation[ST26Response200] = Operation(
    id="ST26",
    method="PUT",
    path="/api/shipments/ready_for_pick_up",
    resource="shipments",
    name="mark_ready_for_pick_up",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=ST26Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_PARTNER_ORDER_SHIPMENT_PICK_UP",
                    "ROLE_SHOP_ADMIN",
                ),
            ),
        ),
    ),
)
_s_t31: Operation[ST31Response200] = Operation(
    id="ST31",
    method="PUT",
    path="/api/shipments/additional_information",
    resource="shipments",
    name="update_additional_information",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=ST31Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SHIP",
                ),
            ),
        ),
    ),
)
_s_t41: Operation[ST41Response200] = Operation(
    id="ST41",
    method="POST",
    path="/api/shipments/shipping-labels/rates",
    resource="shipments",
    name="calculate_label_rates",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=ST41Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SHIPMENT_WRITE",
                ),
            ),
        ),
    ),
)
_s_t42: Operation[ST42Response200] = Operation(
    id="ST42",
    method="GET",
    path="/api/shipments/shipping-labels/rates",
    resource="shipments",
    name="list_label_rates",
    params=(
        Param("shipment_id", "shipment_id", "query"),
        Param("label_rate_state", "label_rate_state", "query"),
        Param("date_created_from", "date_created_from", "query"),
        Param("date_created_to", "date_created_to", "query"),
        Param("last_updated_from", "last_updated_from", "query"),
        Param("last_updated_to", "last_updated_to", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
        Param("sort", "sort", "query"),
    ),
    response=ST42Response200,
    returns_json=True,
    iterator="iter_label_rates",
    item=_models.ST42Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SHIPMENT_READ",
                ),
            ),
        ),
    ),
)
_s_t51: Operation[ST51Response200] = Operation(
    id="ST51",
    method="POST",
    path="/api/shipments/shipping-labels",
    resource="shipments",
    name="create_labels",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=ST51Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SHIPMENT_WRITE",
                ),
            ),
        ),
    ),
)
_s_t52: Operation[ST52Response200] = Operation(
    id="ST52",
    method="GET",
    path="/api/shipments/shipping-labels",
    resource="shipments",
    name="list_labels",
    params=(
        Param("shipment_id", "shipment_id", "query"),
        Param("label_state", "label_state", "query"),
        Param("date_created_from", "date_created_from", "query"),
        Param("date_created_to", "date_created_to", "query"),
        Param("last_updated_from", "last_updated_from", "query"),
        Param("last_updated_to", "last_updated_to", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
        Param("sort", "sort", "query"),
    ),
    response=ST52Response200,
    returns_json=True,
    iterator="iter_labels",
    item=_models.ST52Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_SHIPMENT_READ",
                ),
            ),
        ),
    ),
)

OPERATIONS = (
    _s_t01,
    _s_t06,
    _s_t07,
    _s_t11,
    _s_t12,
    _s_t23,
    _s_t24,
    _s_t26,
    _s_t31,
    _s_t41,
    _s_t42,
    _s_t51,
    _s_t52,
)


class ShipmentsApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[ST01Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST01Response201:
        """Create shipments (ST01)."""
        return self._call(
            _s_t01,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def delete(
        self,
        body: Optional[Union[ST06Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST06Response200:
        """Delete shipments (ST06)."""
        return self._call(
            _s_t06,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def update_shipping_origin(
        self,
        body: Optional[Union[ST07Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST07Response200:
        """Update the shipping origin of shipments (ST07)."""
        return self._call(
            _s_t07,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def list(
        self,
        *,
        order_id: Optional[List[StrictStr]] = None,
        shipment_state_code: Optional[List[StrictStr]] = None,
        shipment_customer_debit_state_code: Optional[List[StrictStr]] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> ST11Response200:
        """List one page of shipments (ST11)."""
        return self._call(
            _s_t11,
            order_id=order_id,
            shipment_state_code=shipment_state_code,
            shipment_customer_debit_state_code=shipment_customer_debit_state_code,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter(
        self,
        *,
        order_id: Optional[List[StrictStr]] = None,
        shipment_state_code: Optional[List[StrictStr]] = None,
        shipment_customer_debit_state_code: Optional[List[StrictStr]] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.ST11Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _s_t11,
            order_id=order_id,
            shipment_state_code=shipment_state_code,
            shipment_customer_debit_state_code=shipment_customer_debit_state_code,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def list_items_to_ship(
        self,
        *,
        order_id: Optional[List[StrictStr]] = None,
        fulfillment_center_code: Optional[List[StrictStr]] = None,
        shipping_date_from: Optional[datetime] = None,
        shipping_date_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> ST12Response200:
        """List one page of items to ship (ST12)."""
        return self._call(
            _s_t12,
            order_id=order_id,
            fulfillment_center_code=fulfillment_center_code,
            shipping_date_from=shipping_date_from,
            shipping_date_to=shipping_date_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_items_to_ship(
        self,
        *,
        order_id: Optional[List[StrictStr]] = None,
        fulfillment_center_code: Optional[List[StrictStr]] = None,
        shipping_date_from: Optional[datetime] = None,
        shipping_date_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.ST12Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _s_t12,
            order_id=order_id,
            fulfillment_center_code=fulfillment_center_code,
            shipping_date_from=shipping_date_from,
            shipping_date_to=shipping_date_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def update_tracking(
        self,
        body: Optional[Union[ST23Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST23Response200:
        """Update the carrier tracking of shipments (ST23)."""
        return self._call(
            _s_t23,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def ship(
        self,
        body: Optional[Union[ST24Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST24Response200:
        """Confirm that shipments have shipped (ST24)."""
        return self._call(
            _s_t24,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def mark_ready_for_pick_up(
        self,
        body: Optional[Union[ST26Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST26Response200:
        """Mark shipments as ready to pick up (ST26)."""
        return self._call(
            _s_t26,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def update_additional_information(
        self,
        body: Optional[Union[ST31Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST31Response200:
        """Update the additional information of shipments (ST31)."""
        return self._call(
            _s_t31,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def calculate_label_rates(
        self,
        body: Optional[Union[ST41Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST41Response200:
        """Calculate shipping label rates (ST41)."""
        return self._call(
            _s_t41,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def list_label_rates(
        self,
        *,
        shipment_id: Optional[List[StrictStr]] = None,
        label_rate_state: Optional[List[StrictStr]] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> ST42Response200:
        """List one page of shipping label rates (ST42)."""
        return self._call(
            _s_t42,
            shipment_id=shipment_id,
            label_rate_state=label_rate_state,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_label_rates(
        self,
        *,
        shipment_id: Optional[List[StrictStr]] = None,
        label_rate_state: Optional[List[StrictStr]] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.ST42Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _s_t42,
            shipment_id=shipment_id,
            label_rate_state=label_rate_state,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def create_labels(
        self,
        body: Optional[Union[ST51Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST51Response200:
        """Create shipping labels (ST51)."""
        return self._call(
            _s_t51,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def list_labels(
        self,
        *,
        shipment_id: Optional[List[StrictStr]] = None,
        label_state: Optional[List[StrictStr]] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> ST52Response200:
        """List one page of shipping labels (ST52)."""
        return self._call(
            _s_t52,
            shipment_id=shipment_id,
            label_state=label_state,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_labels(
        self,
        *,
        shipment_id: Optional[List[StrictStr]] = None,
        label_state: Optional[List[StrictStr]] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.ST52Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _s_t52,
            shipment_id=shipment_id,
            label_state=label_state,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )


class AsyncShipmentsApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[ST01Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST01Response201:
        """Create shipments (ST01)."""
        return await self._call(
            _s_t01,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def delete(
        self,
        body: Optional[Union[ST06Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST06Response200:
        """Delete shipments (ST06)."""
        return await self._call(
            _s_t06,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def update_shipping_origin(
        self,
        body: Optional[Union[ST07Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST07Response200:
        """Update the shipping origin of shipments (ST07)."""
        return await self._call(
            _s_t07,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def list(
        self,
        *,
        order_id: Optional[List[StrictStr]] = None,
        shipment_state_code: Optional[List[StrictStr]] = None,
        shipment_customer_debit_state_code: Optional[List[StrictStr]] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> ST11Response200:
        """List one page of shipments (ST11)."""
        return await self._call(
            _s_t11,
            order_id=order_id,
            shipment_state_code=shipment_state_code,
            shipment_customer_debit_state_code=shipment_customer_debit_state_code,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter(
        self,
        *,
        order_id: Optional[List[StrictStr]] = None,
        shipment_state_code: Optional[List[StrictStr]] = None,
        shipment_customer_debit_state_code: Optional[List[StrictStr]] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ST11Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _s_t11,
            order_id=order_id,
            shipment_state_code=shipment_state_code,
            shipment_customer_debit_state_code=shipment_customer_debit_state_code,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    async def list_items_to_ship(
        self,
        *,
        order_id: Optional[List[StrictStr]] = None,
        fulfillment_center_code: Optional[List[StrictStr]] = None,
        shipping_date_from: Optional[datetime] = None,
        shipping_date_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> ST12Response200:
        """List one page of items to ship (ST12)."""
        return await self._call(
            _s_t12,
            order_id=order_id,
            fulfillment_center_code=fulfillment_center_code,
            shipping_date_from=shipping_date_from,
            shipping_date_to=shipping_date_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_items_to_ship(
        self,
        *,
        order_id: Optional[List[StrictStr]] = None,
        fulfillment_center_code: Optional[List[StrictStr]] = None,
        shipping_date_from: Optional[datetime] = None,
        shipping_date_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ST12Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _s_t12,
            order_id=order_id,
            fulfillment_center_code=fulfillment_center_code,
            shipping_date_from=shipping_date_from,
            shipping_date_to=shipping_date_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    async def update_tracking(
        self,
        body: Optional[Union[ST23Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST23Response200:
        """Update the carrier tracking of shipments (ST23)."""
        return await self._call(
            _s_t23,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def ship(
        self,
        body: Optional[Union[ST24Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST24Response200:
        """Confirm that shipments have shipped (ST24)."""
        return await self._call(
            _s_t24,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def mark_ready_for_pick_up(
        self,
        body: Optional[Union[ST26Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST26Response200:
        """Mark shipments as ready to pick up (ST26)."""
        return await self._call(
            _s_t26,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def update_additional_information(
        self,
        body: Optional[Union[ST31Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST31Response200:
        """Update the additional information of shipments (ST31)."""
        return await self._call(
            _s_t31,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def calculate_label_rates(
        self,
        body: Optional[Union[ST41Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST41Response200:
        """Calculate shipping label rates (ST41)."""
        return await self._call(
            _s_t41,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def list_label_rates(
        self,
        *,
        shipment_id: Optional[List[StrictStr]] = None,
        label_rate_state: Optional[List[StrictStr]] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> ST42Response200:
        """List one page of shipping label rates (ST42)."""
        return await self._call(
            _s_t42,
            shipment_id=shipment_id,
            label_rate_state=label_rate_state,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_label_rates(
        self,
        *,
        shipment_id: Optional[List[StrictStr]] = None,
        label_rate_state: Optional[List[StrictStr]] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ST42Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _s_t42,
            shipment_id=shipment_id,
            label_rate_state=label_rate_state,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    async def create_labels(
        self,
        body: Optional[Union[ST51Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> ST51Response200:
        """Create shipping labels (ST51)."""
        return await self._call(
            _s_t51,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def list_labels(
        self,
        *,
        shipment_id: Optional[List[StrictStr]] = None,
        label_state: Optional[List[StrictStr]] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> ST52Response200:
        """List one page of shipping labels (ST52)."""
        return await self._call(
            _s_t52,
            shipment_id=shipment_id,
            label_state=label_state,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_labels(
        self,
        *,
        shipment_id: Optional[List[StrictStr]] = None,
        label_state: Optional[List[StrictStr]] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ST52Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _s_t52,
            shipment_id=shipment_id,
            label_state=label_state,
            date_created_from=date_created_from,
            date_created_to=date_created_to,
            last_updated_from=last_updated_from,
            last_updated_to=last_updated_to,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )
