# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.listing_translation import ListingTranslation

_create_listing_translation: Operation[ListingTranslation] = Operation(
    id="createListingTranslation",
    method="POST",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/translations/{language}",
    resource="listing_translations",
    name="create",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("language", "language", "path"),
        Param("title", "title", "urlencoded"),
        Param("description", "description", "urlencoded"),
        Param("tags", "tags", "urlencoded"),
    ),
    response=ListingTranslation,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)
_get_listing_translation: Operation[ListingTranslation] = Operation(
    id="getListingTranslation",
    method="GET",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/translations/{language}",
    resource="listing_translations",
    name="get",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("language", "language", "path"),
    ),
    response=ListingTranslation,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_update_listing_translation: Operation[ListingTranslation] = Operation(
    id="updateListingTranslation",
    method="PUT",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/translations/{language}",
    resource="listing_translations",
    name="update",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("language", "language", "path"),
        Param("title", "title", "urlencoded"),
        Param("description", "description", "urlencoded"),
        Param("tags", "tags", "urlencoded"),
    ),
    response=ListingTranslation,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)

OPERATIONS = (
    _create_listing_translation,
    _get_listing_translation,
    _update_listing_translation,
)


class ListingTranslationsApi(Resource):
    @checked
    def create(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        language: StrictStr,
        *,
        title: StrictStr,
        description: StrictStr,
        tags: Optional[List[StrictStr]] = None,
    ) -> ListingTranslation:
        """Add a listing&#39;s translation into one language."""
        return self._call(
            _create_listing_translation,
            shop_id=shop_id,
            listing_id=listing_id,
            language=language,
            title=title,
            description=description,
            tags=tags,
        )

    @checked
    def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        language: StrictStr,
    ) -> ListingTranslation:
        """Get a listing&#39;s translation into one language."""
        return self._call(
            _get_listing_translation,
            shop_id=shop_id,
            listing_id=listing_id,
            language=language,
        )

    @checked
    def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        language: StrictStr,
        *,
        title: StrictStr,
        description: StrictStr,
        tags: Optional[List[StrictStr]] = None,
    ) -> ListingTranslation:
        """Update a listing&#39;s translation into one language."""
        return self._call(
            _update_listing_translation,
            shop_id=shop_id,
            listing_id=listing_id,
            language=language,
            title=title,
            description=description,
            tags=tags,
        )


class AsyncListingTranslationsApi(AsyncResource):
    @checked
    async def create(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        language: StrictStr,
        *,
        title: StrictStr,
        description: StrictStr,
        tags: Optional[List[StrictStr]] = None,
    ) -> ListingTranslation:
        """Add a listing&#39;s translation into one language."""
        return await self._call(
            _create_listing_translation,
            shop_id=shop_id,
            listing_id=listing_id,
            language=language,
            title=title,
            description=description,
            tags=tags,
        )

    @checked
    async def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        language: StrictStr,
    ) -> ListingTranslation:
        """Get a listing&#39;s translation into one language."""
        return await self._call(
            _get_listing_translation,
            shop_id=shop_id,
            listing_id=listing_id,
            language=language,
        )

    @checked
    async def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        language: StrictStr,
        *,
        title: StrictStr,
        description: StrictStr,
        tags: Optional[List[StrictStr]] = None,
    ) -> ListingTranslation:
        """Update a listing&#39;s translation into one language."""
        return await self._call(
            _update_listing_translation,
            shop_id=shop_id,
            listing_id=listing_id,
            language=language,
            title=title,
            description=description,
            tags=tags,
        )
