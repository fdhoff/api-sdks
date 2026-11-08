# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import Field, StrictBool, StrictStr
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, FileInput, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.listing_image import ListingImage
from etsy_seller.models.listing_images import ListingImages

_delete_listing_image: Operation[None] = Operation(
    id="deleteListingImage",
    method="DELETE",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/images/{listing_image_id}",
    resource="listing_images",
    name="delete",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("listing_image_id", "listing_image_id", "path"),
    ),
    response=None,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)
_get_listing_image: Operation[ListingImage] = Operation(
    id="getListingImage",
    method="GET",
    path="/v3/application/listings/{listing_id}/images/{listing_image_id}",
    resource="listing_images",
    name="get",
    params=(
        Param("listing_id", "listing_id", "path"),
        Param("listing_image_id", "listing_image_id", "path"),
    ),
    response=ListingImage,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_get_listing_images: Operation[ListingImages] = Operation(
    id="getListingImages",
    method="GET",
    path="/v3/application/listings/{listing_id}/images",
    resource="listing_images",
    name="list",
    params=(Param("listing_id", "listing_id", "path"),),
    response=ListingImages,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_upload_listing_image: Operation[ListingImage] = Operation(
    id="uploadListingImage",
    method="POST",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/images",
    resource="listing_images",
    name="upload",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("image", "image", "form"),
        Param("listing_image_id", "listing_image_id", "form"),
        Param("rank", "rank", "form"),
        Param("overwrite", "overwrite", "form"),
        Param("is_watermarked", "is_watermarked", "form"),
        Param("alt_text", "alt_text", "form"),
    ),
    response=ListingImage,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)

OPERATIONS = (
    _delete_listing_image,
    _get_listing_image,
    _get_listing_images,
    _upload_listing_image,
)


class ListingImagesApi(Resource):
    @checked
    def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        listing_image_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete an image from a listing."""
        return self._call(
            _delete_listing_image,
            shop_id=shop_id,
            listing_id=listing_id,
            listing_image_id=listing_image_id,
        )

    @checked
    def get(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        listing_image_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingImage:
        """Get one image of a listing."""
        return self._call(
            _get_listing_image,
            listing_id=listing_id,
            listing_image_id=listing_image_id,
        )

    @checked
    def list(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingImages:
        """List a listing's images."""
        return self._call(
            _get_listing_images,
            listing_id=listing_id,
        )

    @checked
    def upload(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        image: Optional[FileInput] = None,
        listing_image_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        rank: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        overwrite: Optional[StrictBool] = None,
        is_watermarked: Optional[StrictBool] = None,
        alt_text: Optional[StrictStr] = None,
    ) -> ListingImage:
        """Upload an image to a listing, or attach an existing one."""
        return self._call(
            _upload_listing_image,
            shop_id=shop_id,
            listing_id=listing_id,
            image=image,
            listing_image_id=listing_image_id,
            rank=rank,
            overwrite=overwrite,
            is_watermarked=is_watermarked,
            alt_text=alt_text,
        )


class AsyncListingImagesApi(AsyncResource):
    @checked
    async def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        listing_image_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete an image from a listing."""
        return await self._call(
            _delete_listing_image,
            shop_id=shop_id,
            listing_id=listing_id,
            listing_image_id=listing_image_id,
        )

    @checked
    async def get(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        listing_image_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingImage:
        """Get one image of a listing."""
        return await self._call(
            _get_listing_image,
            listing_id=listing_id,
            listing_image_id=listing_image_id,
        )

    @checked
    async def list(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingImages:
        """List a listing's images."""
        return await self._call(
            _get_listing_images,
            listing_id=listing_id,
        )

    @checked
    async def upload(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        image: Optional[FileInput] = None,
        listing_image_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        rank: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        overwrite: Optional[StrictBool] = None,
        is_watermarked: Optional[StrictBool] = None,
        alt_text: Optional[StrictStr] = None,
    ) -> ListingImage:
        """Upload an image to a listing, or attach an existing one."""
        return await self._call(
            _upload_listing_image,
            shop_id=shop_id,
            listing_id=listing_id,
            image=image,
            listing_image_id=listing_image_id,
            rank=rank,
            overwrite=overwrite,
            is_watermarked=is_watermarked,
            alt_text=alt_text,
        )
