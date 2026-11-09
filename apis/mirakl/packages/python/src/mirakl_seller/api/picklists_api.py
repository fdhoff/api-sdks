# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from datetime import datetime
from typing import AsyncIterator, Iterator, List, Optional

from pydantic import Field, StrictInt, StrictStr
from typing_extensions import Annotated

from mirakl_seller import models as _models
from mirakl_seller._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mirakl_seller.models.pl11_response200 import PL11Response200

_p_l11: Operation[PL11Response200] = Operation(
    id="PL11",
    method="GET",
    path="/api/picklists",
    resource="picklists",
    name="list",
    params=(
        Param("pickrun_code", "pickrun_code", "query"),
        Param("pickup_date_min", "pickup_date_min", "query"),
        Param("pickup_date_max", "pickup_date_max", "query"),
        Param("picklist_id", "picklist_id", "query"),
        Param("picklist_state", "picklist_state", "query"),
        Param("order_line_id", "order_line_id", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("limit", "limit", "query"),
        Param("page_token", "page_token", "query"),
        Param("sort", "sort", "query"),
    ),
    response=PL11Response200,
    returns_json=True,
    iterator="iter",
    item=_models.PL11Response200Data,
    paging=Cursor(items="data", next="next_page_token", param="page_token"),
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_PICKLIST_READ",
                ),
            ),
        ),
    ),
)

OPERATIONS = (_p_l11,)


class PicklistsApi(Resource):
    @checked
    def list(
        self,
        *,
        pickrun_code: Optional[StrictStr] = None,
        pickup_date_min: Optional[datetime] = None,
        pickup_date_max: Optional[datetime] = None,
        picklist_id: Optional[List[StrictStr]] = None,
        picklist_state: Optional[List[StrictStr]] = None,
        order_line_id: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> PL11Response200:
        """List one page of picklists (PL11)."""
        return self._call(
            _p_l11,
            pickrun_code=pickrun_code,
            pickup_date_min=pickup_date_min,
            pickup_date_max=pickup_date_max,
            picklist_id=picklist_id,
            picklist_state=picklist_state,
            order_line_id=order_line_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter(
        self,
        *,
        pickrun_code: Optional[StrictStr] = None,
        pickup_date_min: Optional[datetime] = None,
        pickup_date_max: Optional[datetime] = None,
        picklist_id: Optional[List[StrictStr]] = None,
        picklist_state: Optional[List[StrictStr]] = None,
        order_line_id: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> Iterator[_models.PL11Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _p_l11,
            pickrun_code=pickrun_code,
            pickup_date_min=pickup_date_min,
            pickup_date_max=pickup_date_max,
            picklist_id=picklist_id,
            picklist_state=picklist_state,
            order_line_id=order_line_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )


class AsyncPicklistsApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        pickrun_code: Optional[StrictStr] = None,
        pickup_date_min: Optional[datetime] = None,
        pickup_date_max: Optional[datetime] = None,
        picklist_id: Optional[List[StrictStr]] = None,
        picklist_state: Optional[List[StrictStr]] = None,
        order_line_id: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> PL11Response200:
        """List one page of picklists (PL11)."""
        return await self._call(
            _p_l11,
            pickrun_code=pickrun_code,
            pickup_date_min=pickup_date_min,
            pickup_date_max=pickup_date_max,
            picklist_id=picklist_id,
            picklist_state=picklist_state,
            order_line_id=order_line_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )

    @checked
    def iter(
        self,
        *,
        pickrun_code: Optional[StrictStr] = None,
        pickup_date_min: Optional[datetime] = None,
        pickup_date_max: Optional[datetime] = None,
        picklist_id: Optional[List[StrictStr]] = None,
        picklist_state: Optional[List[StrictStr]] = None,
        order_line_id: Optional[List[StrictStr]] = None,
        shop_id: Optional[StrictInt] = None,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        page_token: Optional[StrictStr] = None,
        sort: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.PL11Response200Data]:
        """Iterate every item across all pages."""
        return self._paginate(
            _p_l11,
            pickrun_code=pickrun_code,
            pickup_date_min=pickup_date_min,
            pickup_date_max=pickup_date_max,
            picklist_id=picklist_id,
            picklist_state=picklist_state,
            order_line_id=order_line_id,
            shop_id=shop_id,
            limit=limit,
            page_token=page_token,
            sort=sort,
        )
