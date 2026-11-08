# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union
from uuid import UUID

from pydantic import Field, StrictInt, StrictStr
from typing_extensions import Annotated

from backmarket_seller import models as _models
from backmarket_seller._runtime import AsyncResource, Operation, Param, Resource, checked
from backmarket_seller.models.listing_detail import ListingDetail
from backmarket_seller.models.listing_page import ListingPage
from backmarket_seller.models.listing_update import ListingUpdate
from backmarket_seller.models.listings_batch import ListingsBatch
from backmarket_seller.models.listings_catalog import ListingsCatalog
from backmarket_seller.models.updated_listing import UpdatedListing

_get_ws_list_listing: Operation[ListingPage] = Operation(
    id="get-ws-list-listing",
    method="GET",
    path="/ws/listings",
    resource="listings",
    name="list",
    params=(
        Param("publication_state", "publication_state", "query"),
        Param("min_quantity", "min_quantity", "query"),
        Param("max_quantity", "max_quantity", "query"),
        Param("page", "page", "query"),
        Param("page-size", "page_size", "query"),
    ),
    response=ListingPage,
    iterator="iter",
    item=_models.ListingPublic,
)
_get_ws_listing_detail: Operation[ListingDetail] = Operation(
    id="get-ws-listing-detail",
    method="GET",
    path="/ws/listings/detail",
    resource="listings",
    name="find",
    params=(
        Param("sku", "sku", "query"),
        Param("listing_id", "listing_id", "query"),
        Param("id", "id", "query"),
    ),
    response=ListingDetail,
)
_get_ws_specific_listing: Operation[ListingDetail] = Operation(
    id="get-ws-specific-listing",
    method="GET",
    path="/ws/listings/{listingId}",
    resource="listings",
    name="get",
    params=(Param("listingId", "listing_id", "path"),),
    response=ListingDetail,
)
_post_ws_create_or_update_listings: Operation[ListingsBatch] = Operation(
    id="post-ws-create-or-update-listings",
    method="POST",
    path="/ws/listings",
    resource="listings",
    name="batch_update",
    params=(),
    response=ListingsBatch,
)
_update_ws_specific_listing: Operation[UpdatedListing] = Operation(
    id="update-ws-specific-listing",
    method="POST",
    path="/ws/listings/{listingId}",
    resource="listings",
    name="update",
    params=(Param("listingId", "listing_id", "path"),),
    response=UpdatedListing,
)

OPERATIONS = (
    _get_ws_list_listing,
    _get_ws_listing_detail,
    _get_ws_specific_listing,
    _post_ws_create_or_update_listings,
    _update_ws_specific_listing,
)


class ListingsApi(Resource):
    @checked
    def list(
        self,
        *,
        publication_state: Optional[StrictInt] = None,
        min_quantity: Optional[StrictInt] = None,
        max_quantity: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> ListingPage:
        """List one page of listings."""
        return self._call(
            _get_ws_list_listing,
            publication_state=publication_state,
            min_quantity=min_quantity,
            max_quantity=max_quantity,
            page=page,
            page_size=page_size,
        )

    @checked
    def iter(
        self,
        *,
        publication_state: Optional[StrictInt] = None,
        min_quantity: Optional[StrictInt] = None,
        max_quantity: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> Iterator[_models.ListingPublic]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_list_listing,
            publication_state=publication_state,
            min_quantity=min_quantity,
            max_quantity=max_quantity,
            page=page,
            page_size=page_size,
        )

    @checked
    def find(
        self,
        *,
        sku: Optional[StrictStr] = None,
        listing_id: Optional[StrictInt] = None,
        id: Optional[UUID] = None,
    ) -> ListingDetail:
        """Find one listing by SKU or identifier."""
        return self._call(
            _get_ws_listing_detail,
            sku=sku,
            listing_id=listing_id,
            id=id,
        )

    @checked
    def get(
        self,
        listing_id: StrictStr,
    ) -> ListingDetail:
        """Get one listing."""
        return self._call(
            _get_ws_specific_listing,
            listing_id=listing_id,
        )

    @checked
    def batch_update(
        self,
        body: Optional[Union[ListingsCatalog, Mapping[str, Any]]] = None,
    ) -> ListingsBatch:
        """Create or update listings from a CSV catalog."""
        return self._call(
            _post_ws_create_or_update_listings,
            _body=body,
        )

    @checked
    def update(
        self,
        listing_id: StrictStr,
        body: Optional[Union[ListingUpdate, Mapping[str, Any]]] = None,
    ) -> UpdatedListing:
        """Update one listing."""
        return self._call(
            _update_ws_specific_listing,
            listing_id=listing_id,
            _body=body,
        )


class AsyncListingsApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        publication_state: Optional[StrictInt] = None,
        min_quantity: Optional[StrictInt] = None,
        max_quantity: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> ListingPage:
        """List one page of listings."""
        return await self._call(
            _get_ws_list_listing,
            publication_state=publication_state,
            min_quantity=min_quantity,
            max_quantity=max_quantity,
            page=page,
            page_size=page_size,
        )

    @checked
    def iter(
        self,
        *,
        publication_state: Optional[StrictInt] = None,
        min_quantity: Optional[StrictInt] = None,
        max_quantity: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> AsyncIterator[_models.ListingPublic]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_list_listing,
            publication_state=publication_state,
            min_quantity=min_quantity,
            max_quantity=max_quantity,
            page=page,
            page_size=page_size,
        )

    @checked
    async def find(
        self,
        *,
        sku: Optional[StrictStr] = None,
        listing_id: Optional[StrictInt] = None,
        id: Optional[UUID] = None,
    ) -> ListingDetail:
        """Find one listing by SKU or identifier."""
        return await self._call(
            _get_ws_listing_detail,
            sku=sku,
            listing_id=listing_id,
            id=id,
        )

    @checked
    async def get(
        self,
        listing_id: StrictStr,
    ) -> ListingDetail:
        """Get one listing."""
        return await self._call(
            _get_ws_specific_listing,
            listing_id=listing_id,
        )

    @checked
    async def batch_update(
        self,
        body: Optional[Union[ListingsCatalog, Mapping[str, Any]]] = None,
    ) -> ListingsBatch:
        """Create or update listings from a CSV catalog."""
        return await self._call(
            _post_ws_create_or_update_listings,
            _body=body,
        )

    @checked
    async def update(
        self,
        listing_id: StrictStr,
        body: Optional[Union[ListingUpdate, Mapping[str, Any]]] = None,
    ) -> UpdatedListing:
        """Update one listing."""
        return await self._call(
            _update_ws_specific_listing,
            listing_id=listing_id,
            _body=body,
        )
