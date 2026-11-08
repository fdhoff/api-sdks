# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import Field, StrictBool
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.listing_personalization import ListingPersonalization
from etsy_seller.models.update_listing_personalization_request import UpdateListingPersonalizationRequest

_delete_listing_personalization: Operation[None] = Operation(
    id="deleteListingPersonalization",
    method="DELETE",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/personalization",
    resource="listing_personalization",
    name="delete",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
    ),
    response=None,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)
_get_listing_personalization: Operation[ListingPersonalization] = Operation(
    id="getListingPersonalization",
    method="GET",
    path="/v3/application/listings/{listing_id}/personalization",
    resource="listing_personalization",
    name="get",
    params=(Param("listing_id", "listing_id", "path"),),
    response=ListingPersonalization,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_update_listing_personalization: Operation[ListingPersonalization] = Operation(
    id="updateListingPersonalization",
    method="POST",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/personalization",
    resource="listing_personalization",
    name="update",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("supports_multiple_personalization_questions", "supports_multiple_personalization_questions", "query"),
    ),
    response=ListingPersonalization,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)

OPERATIONS = (
    _delete_listing_personalization,
    _get_listing_personalization,
    _update_listing_personalization,
)


class ListingPersonalizationApi(Resource):
    @checked
    def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Remove a listing's personalization questions."""
        return self._call(
            _delete_listing_personalization,
            shop_id=shop_id,
            listing_id=listing_id,
        )

    @checked
    def get(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingPersonalization:
        """Get a listing's personalization questions."""
        return self._call(
            _get_listing_personalization,
            listing_id=listing_id,
        )

    @checked
    def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        body: Optional[Union[UpdateListingPersonalizationRequest, Mapping[str, Any]]] = None,
        *,
        supports_multiple_personalization_questions: Optional[StrictBool] = None,
    ) -> ListingPersonalization:
        """Set a listing's personalization questions."""
        return self._call(
            _update_listing_personalization,
            shop_id=shop_id,
            listing_id=listing_id,
            _body=body,
            supports_multiple_personalization_questions=supports_multiple_personalization_questions,
        )


class AsyncListingPersonalizationApi(AsyncResource):
    @checked
    async def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Remove a listing's personalization questions."""
        return await self._call(
            _delete_listing_personalization,
            shop_id=shop_id,
            listing_id=listing_id,
        )

    @checked
    async def get(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingPersonalization:
        """Get a listing's personalization questions."""
        return await self._call(
            _get_listing_personalization,
            listing_id=listing_id,
        )

    @checked
    async def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        body: Optional[Union[UpdateListingPersonalizationRequest, Mapping[str, Any]]] = None,
        *,
        supports_multiple_personalization_questions: Optional[StrictBool] = None,
    ) -> ListingPersonalization:
        """Set a listing's personalization questions."""
        return await self._call(
            _update_listing_personalization,
            shop_id=shop_id,
            listing_id=listing_id,
            _body=body,
            supports_multiple_personalization_questions=supports_multiple_personalization_questions,
        )
