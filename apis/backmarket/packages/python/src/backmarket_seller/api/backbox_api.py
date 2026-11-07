# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, List, Optional
from uuid import UUID

from pydantic import Field, StrictInt
from typing_extensions import Annotated

from backmarket_seller import models as _models
from backmarket_seller._runtime import AsyncResource, Operation, Param, Resource, checked
from backmarket_seller.models.backbox_page import BackboxPage
from backmarket_seller.models.competitor import Competitor

_get_backbox_data: Operation[BackboxPage] = Operation(
    id="GetBackboxData",
    method="GET",
    path="/ws/listings_bi",
    resource="backbox",
    name="list",
    params=(
        Param("page", "page", "query"),
        Param("page-size", "page_size", "query"),
    ),
    response=BackboxPage,
    iterator="iter",
    item=_models.Backbox,
)
_get_ws_backbox_v1_competitors: Operation[List[Competitor]] = Operation(
    id="get-ws-backbox-v1-competitors",
    method="GET",
    path="/ws/backbox/v1/competitors/{listingId}",
    resource="backbox",
    name="list_competitors",
    params=(Param("listingId", "listing_id", "path"),),
    response=List[Competitor],
)

OPERATIONS = (
    _get_backbox_data,
    _get_ws_backbox_v1_competitors,
)


class BackboxApi(Resource):
    @checked
    def list(
        self,
        *,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> BackboxPage:
        """List one page of Backbox data."""
        return self._call(
            _get_backbox_data,
            page=page,
            page_size=page_size,
        )

    @checked
    def iter(
        self,
        *,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> Iterator[_models.Backbox]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_backbox_data,
            page=page,
            page_size=page_size,
        )

    @checked
    def list_competitors(
        self,
        listing_id: UUID,
    ) -> List[Competitor]:
        """List competitors for a listing."""
        return self._call(
            _get_ws_backbox_v1_competitors,
            listing_id=listing_id,
        )


class AsyncBackboxApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> BackboxPage:
        """List one page of Backbox data."""
        return await self._call(
            _get_backbox_data,
            page=page,
            page_size=page_size,
        )

    @checked
    def iter(
        self,
        *,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> AsyncIterator[_models.Backbox]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_backbox_data,
            page=page,
            page_size=page_size,
        )

    @checked
    async def list_competitors(
        self,
        listing_id: UUID,
    ) -> List[Competitor]:
        """List competitors for a listing."""
        return await self._call(
            _get_ws_backbox_v1_competitors,
            listing_id=listing_id,
        )
