# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Dict, Iterator, List, Mapping, Optional, Tuple, Union

from pydantic import Field, StrictFloat, StrictInt, StrictStr
from typing_extensions import Annotated

from pydantic import Field, StrictInt, StrictStr, field_validator
from typing import Optional
from typing_extensions import Annotated
from uuid import UUID
from backmarket_seller.models.listing_detail import ListingDetail
from backmarket_seller.models.listing_page import ListingPage
from backmarket_seller.models.listing_update import ListingUpdate
from backmarket_seller.models.listings_batch import ListingsBatch
from backmarket_seller.models.listings_catalog import ListingsCatalog
from backmarket_seller.models.updated_listing import UpdatedListing
from backmarket_seller.models import ListingPublic
from backmarket_seller._runtime import AsyncResource, FileInput, Operation, Param, Resource

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
    item=ListingPublic,
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

    def iter(
        self,
        *,
        publication_state: Optional[StrictInt] = None,
        min_quantity: Optional[StrictInt] = None,
        max_quantity: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> Iterator[ListingPublic]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_list_listing,
            publication_state=publication_state,
            min_quantity=min_quantity,
            max_quantity=max_quantity,
            page=page,
            page_size=page_size,
        )

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

    def get(
        self,
        listing_id: StrictStr,
    ) -> ListingDetail:
        """Get one listing."""
        return self._call(
            _get_ws_specific_listing,
            listing_id=listing_id,
        )

    def batch_update(
        self,
        body: Optional[Union[ListingsCatalog, Mapping[str, Any]]] = None,
    ) -> ListingsBatch:
        """Create or update listings from a CSV catalog."""
        return self._call(
            _post_ws_create_or_update_listings,
            _body=body,
        )

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

    def iter(
        self,
        *,
        publication_state: Optional[StrictInt] = None,
        min_quantity: Optional[StrictInt] = None,
        max_quantity: Optional[StrictInt] = None,
        page: Optional[StrictInt] = None,
        page_size: Optional[Annotated[int, Field(le=50, strict=True)]] = None,
    ) -> AsyncIterator[ListingPublic]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_ws_list_listing,
            publication_state=publication_state,
            min_quantity=min_quantity,
            max_quantity=max_quantity,
            page=page,
            page_size=page_size,
        )

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

    async def get(
        self,
        listing_id: StrictStr,
    ) -> ListingDetail:
        """Get one listing."""
        return await self._call(
            _get_ws_specific_listing,
            listing_id=listing_id,
        )

    async def batch_update(
        self,
        body: Optional[Union[ListingsCatalog, Mapping[str, Any]]] = None,
    ) -> ListingsBatch:
        """Create or update listings from a CSV catalog."""
        return await self._call(
            _post_ws_create_or_update_listings,
            _body=body,
        )

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
