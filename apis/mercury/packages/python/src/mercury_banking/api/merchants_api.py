# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.merchants_response import MerchantsResponse

_list_merchants: Operation[MerchantsResponse] = Operation(
    id="listMerchants",
    method="GET",
    path="/merchants",
    resource="merchants",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("order", "order", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("search", "search", "query"),
    ),
    response=MerchantsResponse,
    returns_json=True,
    iterator="iter",
    item=_models.MerchantInfo,
    paging=Cursor(items="data", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (_list_merchants,)


class MerchantsApi(Resource):
    @checked
    def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        search: Optional[StrictStr] = None,
    ) -> MerchantsResponse:
        """List one page of merchants you have paid."""
        return self._call(
            _list_merchants,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            search=search,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        search: Optional[StrictStr] = None,
    ) -> Iterator[_models.MerchantInfo]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_merchants,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            search=search,
        )


class AsyncMerchantsApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        search: Optional[StrictStr] = None,
    ) -> MerchantsResponse:
        """List one page of merchants you have paid."""
        return await self._call(
            _list_merchants,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            search=search,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        search: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.MerchantInfo]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_merchants,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            search=search,
        )
