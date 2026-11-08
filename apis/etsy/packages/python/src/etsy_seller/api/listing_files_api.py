# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from etsy_seller._runtime import AsyncResource, FileInput, Operation, Param, Resource, Scheme, checked
from etsy_seller.models.shop_listing_file import ShopListingFile
from etsy_seller.models.shop_listing_files import ShopListingFiles

_delete_listing_file: Operation[None] = Operation(
    id="deleteListingFile",
    method="DELETE",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/files/{listing_file_id}",
    resource="listing_files",
    name="delete",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("listing_file_id", "listing_file_id", "path"),
    ),
    response=None,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)
_get_all_listing_files: Operation[ShopListingFiles] = Operation(
    id="getAllListingFiles",
    method="GET",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/files",
    resource="listing_files",
    name="list",
    params=(
        Param("listing_id", "listing_id", "path"),
        Param("shop_id", "shop_id", "path"),
    ),
    response=ShopListingFiles,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_r",)),
        ),
    ),
)
_get_listing_file: Operation[ShopListingFile] = Operation(
    id="getListingFile",
    method="GET",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/files/{listing_file_id}",
    resource="listing_files",
    name="get",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("listing_file_id", "listing_file_id", "path"),
    ),
    response=ShopListingFile,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_r",)),
        ),
    ),
)
_upload_listing_file: Operation[ShopListingFile] = Operation(
    id="uploadListingFile",
    method="POST",
    path="/v3/application/shops/{shop_id}/listings/{listing_id}/files",
    resource="listing_files",
    name="upload",
    params=(
        Param("shop_id", "shop_id", "path"),
        Param("listing_id", "listing_id", "path"),
        Param("listing_file_id", "listing_file_id", "form"),
        Param("file", "file", "form"),
        Param("name", "name", "form"),
        Param("rank", "rank", "form"),
    ),
    response=ShopListingFile,
    returns_json=True,
    security=(
        (
            Scheme("api_key", ()),
            Scheme("oauth2", ("listings_w",)),
        ),
    ),
)

OPERATIONS = (
    _delete_listing_file,
    _get_all_listing_files,
    _get_listing_file,
    _upload_listing_file,
)


class ListingFilesApi(Resource):
    @checked
    def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        listing_file_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a file from a digital listing."""
        return self._call(
            _delete_listing_file,
            shop_id=shop_id,
            listing_id=listing_id,
            listing_file_id=listing_file_id,
        )

    @checked
    def list(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopListingFiles:
        """List a digital listing's files."""
        return self._call(
            _get_all_listing_files,
            listing_id=listing_id,
            shop_id=shop_id,
        )

    @checked
    def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        listing_file_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopListingFile:
        """Get one file of a digital listing."""
        return self._call(
            _get_listing_file,
            shop_id=shop_id,
            listing_id=listing_id,
            listing_file_id=listing_file_id,
        )

    @checked
    def upload(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        listing_file_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        file: Optional[FileInput] = None,
        name: Optional[StrictStr] = None,
        rank: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
    ) -> ShopListingFile:
        """Upload a file to a digital listing, or attach an existing one."""
        return self._call(
            _upload_listing_file,
            shop_id=shop_id,
            listing_id=listing_id,
            listing_file_id=listing_file_id,
            file=file,
            name=name,
            rank=rank,
        )


class AsyncListingFilesApi(AsyncResource):
    @checked
    async def delete(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        listing_file_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> None:
        """Delete a file from a digital listing."""
        return await self._call(
            _delete_listing_file,
            shop_id=shop_id,
            listing_id=listing_id,
            listing_file_id=listing_file_id,
        )

    @checked
    async def list(
        self,
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        shop_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopListingFiles:
        """List a digital listing's files."""
        return await self._call(
            _get_all_listing_files,
            listing_id=listing_id,
            shop_id=shop_id,
        )

    @checked
    async def get(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        listing_file_id: Annotated[int, Field(strict=True, ge=1)],
    ) -> ShopListingFile:
        """Get one file of a digital listing."""
        return await self._call(
            _get_listing_file,
            shop_id=shop_id,
            listing_id=listing_id,
            listing_file_id=listing_file_id,
        )

    @checked
    async def upload(
        self,
        shop_id: Annotated[int, Field(strict=True, ge=1)],
        listing_id: Annotated[int, Field(strict=True, ge=1)],
        *,
        listing_file_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
        file: Optional[FileInput] = None,
        name: Optional[StrictStr] = None,
        rank: Optional[Annotated[int, Field(strict=True, ge=1)]] = None,
    ) -> ShopListingFile:
        """Upload a file to a digital listing, or attach an existing one."""
        return await self._call(
            _upload_listing_file,
            shop_id=shop_id,
            listing_id=listing_id,
            listing_file_id=listing_file_id,
            file=file,
            name=name,
            rank=rank,
        )
