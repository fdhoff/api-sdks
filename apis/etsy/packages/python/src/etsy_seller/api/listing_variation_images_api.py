# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import Field
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.listing_variation_images import ListingVariationImages
from etsy_seller.models.update_variation_images_request import UpdateVariationImagesRequest

_get_listing_variation_images: Operation[ListingVariationImages] = Operation(
    id="getListingVariationImages",
    method="GET",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/variation-images",
    resource="listing_variation_images",
    name="list",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
    ),
    response=ListingVariationImages,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_update_variation_images: Operation[ListingVariationImages] = Operation(
    id="updateVariationImages",
    method="POST",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/variation-images",
    resource="listing_variation_images",
    name="update",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
    ),
    response=ListingVariationImages,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)

OPERATIONS = (
    _get_listing_variation_images,
    _update_variation_images,
)


class ListingVariationImagesApi(Resource):
    @checked
    def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingVariationImages:
        """List the images mapped to a listing's variations."""
        return self._call(
            _get_listing_variation_images,
            shop_id=shop_id,
            listing_id=listing_id,
        )

    @checked
    def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        body: Optional[Union[UpdateVariationImagesRequest, Mapping[str, Any]]] = None,
    ) -> ListingVariationImages:
        """Replace the images mapped to a listing's variations."""
        return self._call(
            _update_variation_images,
            shop_id=shop_id,
            listing_id=listing_id,
            _body=body,
        )


class AsyncListingVariationImagesApi(AsyncResource):
    @checked
    async def list(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingVariationImages:
        """List the images mapped to a listing's variations."""
        return await self._call(
            _get_listing_variation_images,
            shop_id=shop_id,
            listing_id=listing_id,
        )

    @checked
    async def update(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        body: Optional[Union[UpdateVariationImagesRequest, Mapping[str, Any]]] = None,
    ) -> ListingVariationImages:
        """Replace the images mapped to a listing's variations."""
        return await self._call(
            _update_variation_images,
            shop_id=shop_id,
            listing_id=listing_id,
            _body=body,
        )
