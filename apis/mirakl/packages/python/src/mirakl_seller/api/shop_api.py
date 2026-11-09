# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, List, Mapping, Optional, Union

from pydantic import StrictInt, StrictStr

from mirakl_seller._runtime import (
    AsyncDownload,
    AsyncResource,
    Download,
    FileInput,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from mirakl_seller.models.a01_response200 import A01Response200
from mirakl_seller.models.a02_request import A02Request
from mirakl_seller.models.a02_response200 import A02Response200
from mirakl_seller.models.a21_response200 import A21Response200
from mirakl_seller.models.s30_response200 import S30Response200
from mirakl_seller.models.s32_request_multipart_form_data_shop_documents import S32RequestMultipartFormDataShopDocuments
from mirakl_seller.models.s32_response200 import S32Response200

_a01: Operation[A01Response200] = Operation(
    id="A01",
    method="GET",
    path="/api/account",
    resource="shop",
    name="get",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=A01Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_SHOP_READ",
                ),
            ),
        ),
    ),
)
_a02: Operation[A02Response200] = Operation(
    id="A02",
    method="PUT",
    path="/api/account",
    resource="shop",
    name="update",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=A02Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_SHOP_UPDATE",
                ),
            ),
        ),
    ),
)
_a21: Operation[A21Response200] = Operation(
    id="A21",
    method="GET",
    path="/api/account/statistics",
    resource="shop",
    name="get_statistics",
    params=(
        Param("periods", "periods", "query"),
        Param("channel_code", "channel_code", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=A21Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_SHOP_READ",
                ),
            ),
        ),
    ),
)
_s30: Operation[S30Response200] = Operation(
    id="S30",
    method="GET",
    path="/api/shops/documents",
    resource="shop",
    name="list_documents",
    params=(Param("shop_id", "shop_id", "query", defaulted=True),),
    response=S30Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_SHOP_DOCUMENT_READ",
                ),
            ),
        ),
    ),
)
_s31: Operation[None] = Operation(
    id="S31",
    method="GET",
    path="/api/shops/documents/download",
    resource="shop",
    name="download_documents",
    params=(
        Param("document_ids", "document_ids", "query"),
        Param("type_codes", "type_codes", "query"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    binary_response=True,
    accept="application/octet-stream",
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_SHOP_DOCUMENT_READ",
                ),
            ),
        ),
    ),
)
_s32: Operation[S32Response200] = Operation(
    id="S32",
    method="POST",
    path="/api/shops/documents",
    resource="shop",
    name="upload_documents",
    params=(
        Param("shop_id", "shop_id", "query", defaulted=True),
        Param("files", "files", "form"),
        Param("shop_documents", "shop_documents", "form"),
    ),
    response=S32Response200,
    returns_json=True,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_SHOP_DOCUMENT_WRITE",
                ),
            ),
        ),
    ),
)
_s33: Operation[None] = Operation(
    id="S33",
    method="DELETE",
    path="/api/shops/documents/{document_id}",
    resource="shop",
    name="delete_document",
    params=(
        Param("document_id", "document_id", "path"),
        Param("shop_id", "shop_id", "query", defaulted=True),
    ),
    response=None,
    security=(
        (
            Scheme(
                "Shop-API-Key",
                (
                    "ROLE_SHOP_ADMIN",
                    "ROLE_PARTNER_SHOP_DOCUMENT_DELETE",
                ),
            ),
        ),
    ),
)

OPERATIONS = (
    _a01,
    _a02,
    _a21,
    _s30,
    _s31,
    _s32,
    _s33,
)


class ShopApi(Resource):
    @checked
    def get(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> A01Response200:
        """Get your shop's information (A01)."""
        return self._call(
            _a01,
            shop_id=shop_id,
        )

    @checked
    def update(
        self,
        body: Optional[Union[A02Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> A02Response200:
        """Update your shop's information (A02)."""
        return self._call(
            _a02,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    def get_statistics(
        self,
        *,
        periods: Optional[StrictStr] = None,
        channel_code: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> A21Response200:
        """Get your shop's statistics (A21)."""
        return self._call(
            _a21,
            periods=periods,
            channel_code=channel_code,
            shop_id=shop_id,
        )

    @checked
    def list_documents(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> S30Response200:
        """List your shop's documents (S30)."""
        return self._call(
            _s30,
            shop_id=shop_id,
        )

    @checked
    def download_documents(
        self,
        *,
        document_ids: Optional[StrictStr] = None,
        type_codes: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> Download:
        """Download one or more shop documents (S31). Close the download, or read it in a `with` block."""
        return self._download(
            _s31,
            document_ids=document_ids,
            type_codes=type_codes,
            shop_id=shop_id,
        )

    @checked
    def upload_documents(
        self,
        *,
        files: List[FileInput],
        shop_documents: S32RequestMultipartFormDataShopDocuments,
        shop_id: Optional[StrictInt] = None,
    ) -> S32Response200:
        """Upload business documents to your shop (S32)."""
        return self._call(
            _s32,
            shop_id=shop_id,
            files=files,
            shop_documents=shop_documents,
        )

    @checked
    def delete_document(
        self,
        document_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Delete a shop document (S33)."""
        return self._call(
            _s33,
            document_id=document_id,
            shop_id=shop_id,
        )


class AsyncShopApi(AsyncResource):
    @checked
    async def get(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> A01Response200:
        """Get your shop's information (A01)."""
        return await self._call(
            _a01,
            shop_id=shop_id,
        )

    @checked
    async def update(
        self,
        body: Optional[Union[A02Request, Mapping[str, Any]]] = None,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> A02Response200:
        """Update your shop's information (A02)."""
        return await self._call(
            _a02,
            _body=body,
            shop_id=shop_id,
        )

    @checked
    async def get_statistics(
        self,
        *,
        periods: Optional[StrictStr] = None,
        channel_code: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> A21Response200:
        """Get your shop's statistics (A21)."""
        return await self._call(
            _a21,
            periods=periods,
            channel_code=channel_code,
            shop_id=shop_id,
        )

    @checked
    async def list_documents(
        self,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> S30Response200:
        """List your shop's documents (S30)."""
        return await self._call(
            _s30,
            shop_id=shop_id,
        )

    @checked
    async def download_documents(
        self,
        *,
        document_ids: Optional[StrictStr] = None,
        type_codes: Optional[StrictStr] = None,
        shop_id: Optional[StrictInt] = None,
    ) -> AsyncDownload:
        """Download one or more shop documents (S31). Close the download, or read it in an `async with` block."""
        return await self._download(
            _s31,
            document_ids=document_ids,
            type_codes=type_codes,
            shop_id=shop_id,
        )

    @checked
    async def upload_documents(
        self,
        *,
        files: List[FileInput],
        shop_documents: S32RequestMultipartFormDataShopDocuments,
        shop_id: Optional[StrictInt] = None,
    ) -> S32Response200:
        """Upload business documents to your shop (S32)."""
        return await self._call(
            _s32,
            shop_id=shop_id,
            files=files,
            shop_documents=shop_documents,
        )

    @checked
    async def delete_document(
        self,
        document_id: StrictInt,
        *,
        shop_id: Optional[StrictInt] = None,
    ) -> None:
        """Delete a shop document (S33)."""
        return await self._call(
            _s33,
            document_id=document_id,
            shop_id=shop_id,
        )
