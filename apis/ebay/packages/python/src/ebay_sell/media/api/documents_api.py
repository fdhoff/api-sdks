# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, Mapping, Optional, Union

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, FileInput, Operation, Param, Resource, Scheme, checked
from ebay_sell.media.models.create_document_from_url_request import CreateDocumentFromUrlRequest
from ebay_sell.media.models.create_document_request import CreateDocumentRequest
from ebay_sell.media.models.create_document_response import CreateDocumentResponse
from ebay_sell.media.models.document_response import DocumentResponse

_create_document: Operation[CreateDocumentResponse] = Operation(
    id="createDocument",
    method="POST",
    path="/commerce/media/v1_beta/document",
    resource="documents",
    name="create",
    params=(),
    response=CreateDocumentResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_create_document_from_url: Operation[CreateDocumentResponse] = Operation(
    id="createDocumentFromUrl",
    method="POST",
    path="/commerce/media/v1_beta/document/create_document_from_url",
    resource="documents",
    name="create_from_url",
    params=(),
    response=CreateDocumentResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_get_document: Operation[DocumentResponse] = Operation(
    id="getDocument",
    method="GET",
    path="/commerce/media/v1_beta/document/{document_id}",
    resource="documents",
    name="get",
    params=(Param("document_id", "document_id", "path"),),
    response=DocumentResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)
_upload_document: Operation[DocumentResponse] = Operation(
    id="uploadDocument",
    method="POST",
    path="/commerce/media/v1_beta/document/{document_id}/upload",
    resource="documents",
    name="upload",
    params=(
        Param("document_id", "document_id", "path"),
        Param("file", "file", "form"),
    ),
    response=DocumentResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope/sell.inventory",)),),),
    host="api",
)

OPERATIONS = (
    _create_document,
    _create_document_from_url,
    _get_document,
    _upload_document,
)


class DocumentsApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[CreateDocumentRequest, Mapping[str, Any]]] = None,
    ) -> CreateDocumentResponse:
        """Create a document resource to upload a file to."""
        return self._call(
            _create_document,
            _body=body,
        )

    @checked
    def create_from_url(
        self,
        body: Optional[Union[CreateDocumentFromUrlRequest, Mapping[str, Any]]] = None,
    ) -> CreateDocumentResponse:
        """Create a document from a public URL."""
        return self._call(
            _create_document_from_url,
            _body=body,
        )

    @checked
    def get(
        self,
        document_id: StrictStr,
    ) -> DocumentResponse:
        """Get one document and its status."""
        return self._call(
            _get_document,
            document_id=document_id,
        )

    @checked
    def upload(
        self,
        document_id: StrictStr,
        *,
        file: FileInput,
    ) -> DocumentResponse:
        """Upload the file of a document."""
        return self._call(
            _upload_document,
            document_id=document_id,
            file=file,
        )


class AsyncDocumentsApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[CreateDocumentRequest, Mapping[str, Any]]] = None,
    ) -> CreateDocumentResponse:
        """Create a document resource to upload a file to."""
        return await self._call(
            _create_document,
            _body=body,
        )

    @checked
    async def create_from_url(
        self,
        body: Optional[Union[CreateDocumentFromUrlRequest, Mapping[str, Any]]] = None,
    ) -> CreateDocumentResponse:
        """Create a document from a public URL."""
        return await self._call(
            _create_document_from_url,
            _body=body,
        )

    @checked
    async def get(
        self,
        document_id: StrictStr,
    ) -> DocumentResponse:
        """Get one document and its status."""
        return await self._call(
            _get_document,
            document_id=document_id,
        )

    @checked
    async def upload(
        self,
        document_id: StrictStr,
        *,
        file: FileInput,
    ) -> DocumentResponse:
        """Upload the file of a document."""
        return await self._call(
            _upload_document,
            document_id=document_id,
            file=file,
        )
