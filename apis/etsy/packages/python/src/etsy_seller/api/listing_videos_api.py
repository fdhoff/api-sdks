# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, FileInput, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.listing_video import ListingVideo
from etsy_seller.models.listing_videos import ListingVideos

_delete_listing_video: Operation[None] = Operation(
    id="deleteListingVideo",
    method="DELETE",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/videos/{video_id}",
    resource="listing_videos",
    name="delete",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("video_id", "video_id", "path"),
    ),
    response=None,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)
_get_listing_video: Operation[ListingVideo] = Operation(
    id="getListingVideo",
    method="GET",
    path="/v3/application/listings/{listing_id}/videos/{video_id}",
    resource="listing_videos",
    name="get",
    params=(
        Param("video_id", "video_id", "path"),
        Param("listing_id", "listing_id", "path"),
    ),
    response=ListingVideo,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_get_listing_videos: Operation[ListingVideos] = Operation(
    id="getListingVideos",
    method="GET",
    path="/v3/application/listings/{listing_id}/videos",
    resource="listing_videos",
    name="list",
    params=(Param("listing_id", "listing_id", "path"),),
    response=ListingVideos,
    returns_json=True,
    security=((Scheme("api_key", ()),),),
)
_upload_listing_video: Operation[ListingVideo] = Operation(
    id="uploadListingVideo",
    method="POST",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/videos",
    resource="listing_videos",
    name="upload",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("video_id", "video_id", "form"),
        Param("video", "video", "form"),
        Param("name", "name", "form"),
    ),
    response=ListingVideo,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)

OPERATIONS = (
    _delete_listing_video,
    _get_listing_video,
    _get_listing_videos,
    _upload_listing_video,
)


class ListingVideosApi(Resource):
    @checked
    def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        video_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a video from a listing."""
        return self._call(
            _delete_listing_video,
            shop_id=shop_id,
            listing_id=listing_id,
            video_id=video_id,
        )

    @checked
    def get(
        self,
        video_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingVideo:
        """Get one video of a listing."""
        return self._call(
            _get_listing_video,
            video_id=video_id,
            listing_id=listing_id,
        )

    @checked
    def list(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingVideos:
        """List a listing&#39;s videos."""
        return self._call(
            _get_listing_videos,
            listing_id=listing_id,
        )

    @checked
    def upload(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        video_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        video: Optional[FileInput] = None,
        name: Optional[StrictStr] = None,
    ) -> ListingVideo:
        """Upload a video to a listing, or attach an existing one."""
        return self._call(
            _upload_listing_video,
            shop_id=shop_id,
            listing_id=listing_id,
            video_id=video_id,
            video=video,
            name=name,
        )


class AsyncListingVideosApi(AsyncResource):
    @checked
    async def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        video_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a video from a listing."""
        return await self._call(
            _delete_listing_video,
            shop_id=shop_id,
            listing_id=listing_id,
            video_id=video_id,
        )

    @checked
    async def get(
        self,
        video_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingVideo:
        """Get one video of a listing."""
        return await self._call(
            _get_listing_video,
            video_id=video_id,
            listing_id=listing_id,
        )

    @checked
    async def list(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ListingVideos:
        """List a listing&#39;s videos."""
        return await self._call(
            _get_listing_videos,
            listing_id=listing_id,
        )

    @checked
    async def upload(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        video_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        video: Optional[FileInput] = None,
        name: Optional[StrictStr] = None,
    ) -> ListingVideo:
        """Upload a video to a listing, or attach an existing one."""
        return await self._call(
            _upload_listing_video,
            shop_id=shop_id,
            listing_id=listing_id,
            video_id=video_id,
            video=video,
            name=name,
        )
