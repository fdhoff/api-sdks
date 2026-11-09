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
from mirakl_seller.models.rt01_request import RT01Request
from mirakl_seller.models.rt01_response200 import RT01Response200
from mirakl_seller.models.rt04_request import RT04Request
from mirakl_seller.models.rt04_response200 import RT04Response200
from mirakl_seller.models.rt11_response200 import RT11Response200
from mirakl_seller.models.rt12_response200 import RT12Response200
from mirakl_seller.models.rt21_request import RT21Request
from mirakl_seller.models.rt21_response200 import RT21Response200
from mirakl_seller.models.rt25_request import RT25Request
from mirakl_seller.models.rt25_response200 import RT25Response200
from mirakl_seller.models.rt26_request import RT26Request
from mirakl_seller.models.rt26_response200 import RT26Response200
from mirakl_seller.models.rt27_request import RT27Request
from mirakl_seller.models.rt27_response200 import RT27Response200
from mirakl_seller.models.rt29_request import RT29Request
from mirakl_seller.models.rt29_response200 import RT29Response200
from mirakl_seller.models.rt51_request import RT51Request
from mirakl_seller.models.rt51_response200 import RT51Response200
from mirakl_seller.models.rt52_response200 import RT52Response200

_r_t01: Operation[RT01Response200] = Operation(
    id="RT01",
    method="POST",
    path="/api/returns",
    resource="returns",
    name="create",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=RT01Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_PARTNER_ORDER_RETURN_WRITE",
                    "ROLE_SHOP_ADMIN",
                ),
            ),
        ),
    ),
)
_r_t04: Operation[RT04Response200] = Operation(
    id="RT04",
    method="PUT",
    path="/api/returns",
    resource="returns",
    name="update",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=RT04Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_RETURN_WRITE",
                ),
            ),
        ),
    ),
)
_r_t11: Operation[RT11Response200] = Operation(
    id="RT11",
    method="GET",
    path="/api/returns",
    resource="returns",
    name="list",
    params=(
        Param("return_id", "return_id", "query"),
        Param("return_state", "return_state", "query"),
        Param("return_creation_date_from", "return_creation_date_from", "query"),
        Param("return_creation_date_to", "return_creation_date_to", "query"),
        Param("return_last_updated_from", "return_last_updated_from", "query"),
        Param("return_last_updated_to", "return_last_updated_to", "query"),
        Param("order_commercial_id", "order_commercial_id", "query"),
        Param("order_line_id", "order_line_id", "query"),
        Param("return_rma", "return_rma", "query"),
        Param("customer_id", "customer_id", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
        Param("sort", "sort", "query"),
    ),
    response=RT11Response200,
    returns_json=True,
    iterator="iter",
    item=_models.RT11Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_PARTNER_ORDER_RETURN_READ",
                    "ROLE_SHOP_ADMIN",
                ),
            ),
        ),
    ),
)
_r_t12: Operation[RT12Response200] = Operation(
    id="RT12",
    method="GET",
    path="/api/returns/items_to_return",
    resource="returns",
    name="list_items_to_return",
    params=(
        Param("order_commercial_id", "order_commercial_id", "query"),
        Param("order_line_id", "order_line_id", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
        Param("sort", "sort", "query"),
    ),
    response=RT12Response200,
    returns_json=True,
    iterator="iter_items_to_return",
    item=_models.RT12Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_PARTNER_ORDER_RETURN_READ",
                    "ROLE_SHOP_ADMIN",
                ),
            ),
        ),
    ),
)
_r_t21: Operation[RT21Response200] = Operation(
    id="RT21",
    method="PUT",
    path="/api/returns/accept",
    resource="returns",
    name="accept",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=RT21Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_RETURN_WRITE",
                ),
            ),
        ),
    ),
)
_r_t25: Operation[RT25Response200] = Operation(
    id="RT25",
    method="PUT",
    path="/api/returns/receive",
    resource="returns",
    name="receive",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=RT25Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_PARTNER_ORDER_RETURN_WRITE",
                    "ROLE_SHOP_ADMIN",
                ),
            ),
        ),
    ),
)
_r_t26: Operation[RT26Response200] = Operation(
    id="RT26",
    method="PUT",
    path="/api/returns/compliance",
    resource="returns",
    name="set_compliance",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=RT26Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_RETURN_WRITE",
                ),
            ),
        ),
    ),
)
_r_t27: Operation[RT27Response200] = Operation(
    id="RT27",
    method="PUT",
    path="/api/returns/close",
    resource="returns",
    name="close",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=RT27Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_RETURN_WRITE",
                ),
            ),
        ),
    ),
)
_r_t29: Operation[RT29Response200] = Operation(
    id="RT29",
    method="PUT",
    path="/api/returns/cancel",
    resource="returns",
    name="cancel",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=RT29Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_RETURN_WRITE",
                ),
            ),
        ),
    ),
)
_r_t51: Operation[RT51Response200] = Operation(
    id="RT51",
    method="POST",
    path="/api/returns/return-labels",
    resource="returns",
    name="create_labels",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=RT51Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_RETURN_WRITE",
                ),
            ),
        ),
    ),
)
_r_t52: Operation[RT52Response200] = Operation(
    id="RT52",
    method="GET",
    path="/api/returns/return-labels",
    resource="returns",
    name="list_labels",
    params=(
        Param("return_id", "return_id", "query"),
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
    response=RT52Response200,
    returns_json=True,
    iterator="iter_labels",
    item=_models.RT52Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_ORDER_RETURN_READ",
                ),
            ),
        ),
    ),
)

OPERATIONS = (
    _r_t01,
    _r_t04,
    _r_t11,
    _r_t12,
    _r_t21,
    _r_t25,
    _r_t26,
    _r_t27,
    _r_t29,
    _r_t51,
    _r_t52,
)


class ReturnsApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[RT01Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT01Response200:
        """Create returns (RT01)."""
        return self._call(
            _r_t01,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def update(
        self,
        body: Optional[Union[RT04Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT04Response200:
        """Update fields on several returns (RT04)."""
        return self._call(
            _r_t04,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def list(
        self,
        *,
        return_id: Optional[List[StrictStr]] = None,
        return_state: Optional[List[StrictStr]] = None,
        return_creation_date_from: Optional[datetime] = None,
        return_creation_date_to: Optional[datetime] = None,
        return_last_updated_from: Optional[datetime] = None,
        return_last_updated_to: Optional[datetime] = None,
        order_commercial_id: Optional[List[StrictStr]] = None,
        order_line_id: Optional[List[StrictStr]] = None,
        return_rma: Optional[List[StrictStr]] = None,
        customer_id: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> RT11Response200:
        """List one page of returns (RT11)."""
        return self._call(
            _r_t11,
            return_id=return_id,
            return_state=return_state,
            return_creation_date_from=return_creation_date_from,
            return_creation_date_to=return_creation_date_to,
            return_last_updated_from=return_last_updated_from,
            return_last_updated_to=return_last_updated_to,
            order_commercial_id=order_commercial_id,
            order_line_id=order_line_id,
            return_rma=return_rma,
            customer_id=customer_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter(
        self,
        *,
        return_id: Optional[List[StrictStr]] = None,
        return_state: Optional[List[StrictStr]] = None,
        return_creation_date_from: Optional[datetime] = None,
        return_creation_date_to: Optional[datetime] = None,
        return_last_updated_from: Optional[datetime] = None,
        return_last_updated_to: Optional[datetime] = None,
        order_commercial_id: Optional[List[StrictStr]] = None,
        order_line_id: Optional[List[StrictStr]] = None,
        return_rma: Optional[List[StrictStr]] = None,
        customer_id: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.RT11Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _r_t11,
            return_id=return_id,
            return_state=return_state,
            return_creation_date_from=return_creation_date_from,
            return_creation_date_to=return_creation_date_to,
            return_last_updated_from=return_last_updated_from,
            return_last_updated_to=return_last_updated_to,
            order_commercial_id=order_commercial_id,
            order_line_id=order_line_id,
            return_rma=return_rma,
            customer_id=customer_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def list_items_to_return(
        self,
        *,
        order_commercial_id: Optional[List[StrictStr]] = None,
        order_line_id: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> RT12Response200:
        """List one page of items to return (RT12)."""
        return self._call(
            _r_t12,
            order_commercial_id=order_commercial_id,
            order_line_id=order_line_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_items_to_return(
        self,
        *,
        order_commercial_id: Optional[List[StrictStr]] = None,
        order_line_id: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.RT12Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _r_t12,
            order_commercial_id=order_commercial_id,
            order_line_id=order_line_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def accept(
        self,
        body: Optional[Union[RT21Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT21Response200:
        """Accept or refuse return requests (RT21)."""
        return self._call(
            _r_t21,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def receive(
        self,
        body: Optional[Union[RT25Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT25Response200:
        """Confirm that returns were received (RT25)."""
        return self._call(
            _r_t25,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def set_compliance(
        self,
        body: Optional[Union[RT26Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT26Response200:
        """Mark returns as compliant or not (RT26)."""
        return self._call(
            _r_t26,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def close(
        self,
        body: Optional[Union[RT27Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT27Response200:
        """Close returns (RT27)."""
        return self._call(
            _r_t27,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def cancel(
        self,
        body: Optional[Union[RT29Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT29Response200:
        """Cancel returns (RT29)."""
        return self._call(
            _r_t29,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def create_labels(
        self,
        body: Optional[Union[RT51Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT51Response200:
        """Create return labels (RT51)."""
        return self._call(
            _r_t51,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def list_labels(
        self,
        *,
        return_id: Optional[List[StrictStr]] = None,
        label_state: Optional[List[StrictStr]] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> RT52Response200:
        """List one page of return labels (RT52)."""
        return self._call(
            _r_t52,
            return_id=return_id,
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
        return_id: Optional[List[StrictStr]] = None,
        label_state: Optional[List[StrictStr]] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.RT52Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _r_t52,
            return_id=return_id,
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


class AsyncReturnsApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[RT01Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT01Response200:
        """Create returns (RT01)."""
        return await self._call(
            _r_t01,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def update(
        self,
        body: Optional[Union[RT04Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT04Response200:
        """Update fields on several returns (RT04)."""
        return await self._call(
            _r_t04,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def list(
        self,
        *,
        return_id: Optional[List[StrictStr]] = None,
        return_state: Optional[List[StrictStr]] = None,
        return_creation_date_from: Optional[datetime] = None,
        return_creation_date_to: Optional[datetime] = None,
        return_last_updated_from: Optional[datetime] = None,
        return_last_updated_to: Optional[datetime] = None,
        order_commercial_id: Optional[List[StrictStr]] = None,
        order_line_id: Optional[List[StrictStr]] = None,
        return_rma: Optional[List[StrictStr]] = None,
        customer_id: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> RT11Response200:
        """List one page of returns (RT11)."""
        return await self._call(
            _r_t11,
            return_id=return_id,
            return_state=return_state,
            return_creation_date_from=return_creation_date_from,
            return_creation_date_to=return_creation_date_to,
            return_last_updated_from=return_last_updated_from,
            return_last_updated_to=return_last_updated_to,
            order_commercial_id=order_commercial_id,
            order_line_id=order_line_id,
            return_rma=return_rma,
            customer_id=customer_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter(
        self,
        *,
        return_id: Optional[List[StrictStr]] = None,
        return_state: Optional[List[StrictStr]] = None,
        return_creation_date_from: Optional[datetime] = None,
        return_creation_date_to: Optional[datetime] = None,
        return_last_updated_from: Optional[datetime] = None,
        return_last_updated_to: Optional[datetime] = None,
        order_commercial_id: Optional[List[StrictStr]] = None,
        order_line_id: Optional[List[StrictStr]] = None,
        return_rma: Optional[List[StrictStr]] = None,
        customer_id: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.RT11Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _r_t11,
            return_id=return_id,
            return_state=return_state,
            return_creation_date_from=return_creation_date_from,
            return_creation_date_to=return_creation_date_to,
            return_last_updated_from=return_last_updated_from,
            return_last_updated_to=return_last_updated_to,
            order_commercial_id=order_commercial_id,
            order_line_id=order_line_id,
            return_rma=return_rma,
            customer_id=customer_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    async def list_items_to_return(
        self,
        *,
        order_commercial_id: Optional[List[StrictStr]] = None,
        order_line_id: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> RT12Response200:
        """List one page of items to return (RT12)."""
        return await self._call(
            _r_t12,
            order_commercial_id=order_commercial_id,
            order_line_id=order_line_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter_items_to_return(
        self,
        *,
        order_commercial_id: Optional[List[StrictStr]] = None,
        order_line_id: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.RT12Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _r_t12,
            order_commercial_id=order_commercial_id,
            order_line_id=order_line_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    async def accept(
        self,
        body: Optional[Union[RT21Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT21Response200:
        """Accept or refuse return requests (RT21)."""
        return await self._call(
            _r_t21,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def receive(
        self,
        body: Optional[Union[RT25Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT25Response200:
        """Confirm that returns were received (RT25)."""
        return await self._call(
            _r_t25,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def set_compliance(
        self,
        body: Optional[Union[RT26Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT26Response200:
        """Mark returns as compliant or not (RT26)."""
        return await self._call(
            _r_t26,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def close(
        self,
        body: Optional[Union[RT27Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT27Response200:
        """Close returns (RT27)."""
        return await self._call(
            _r_t27,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def cancel(
        self,
        body: Optional[Union[RT29Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT29Response200:
        """Cancel returns (RT29)."""
        return await self._call(
            _r_t29,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def create_labels(
        self,
        body: Optional[Union[RT51Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> RT51Response200:
        """Create return labels (RT51)."""
        return await self._call(
            _r_t51,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def list_labels(
        self,
        *,
        return_id: Optional[List[StrictStr]] = None,
        label_state: Optional[List[StrictStr]] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> RT52Response200:
        """List one page of return labels (RT52)."""
        return await self._call(
            _r_t52,
            return_id=return_id,
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
        return_id: Optional[List[StrictStr]] = None,
        label_state: Optional[List[StrictStr]] = None,
        date_created_from: Optional[datetime] = None,
        date_created_to: Optional[datetime] = None,
        last_updated_from: Optional[datetime] = None,
        last_updated_to: Optional[datetime] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.RT52Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _r_t52,
            return_id=return_id,
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
