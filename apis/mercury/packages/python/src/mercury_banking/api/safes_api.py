# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import List
from uuid import UUID

from mercury_banking._runtime import (
    AsyncDownload,
    AsyncResource,
    Download,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from mercury_banking.models.api_safe_request import APISafeRequest

_get_safe_request: Operation[APISafeRequest] = Operation(
    id="getSafeRequest",
    method="GET",
    path="/safes/{safeRequestId}",
    resource="safes",
    name="get",
    params=(Param("safeRequestId", "safe_request_id", "path"),),
    response=APISafeRequest,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_safe_request_document: Operation[None] = Operation(
    id="getSafeRequestDocument",
    method="GET",
    path="/safes/{safeRequestId}/document",
    resource="safes",
    name="download_document",
    params=(Param("safeRequestId", "safe_request_id", "path"),),
    response=None,
    binary_response=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_safe_requests: Operation[List[APISafeRequest]] = Operation(
    id="getSafeRequests",
    method="GET",
    path="/safes",
    resource="safes",
    name="list",
    params=(),
    response=List[APISafeRequest],
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _get_safe_request,
    _get_safe_request_document,
    _get_safe_requests,
)


class SafesApi(Resource):
    @checked
    def get(
        self,
        safe_request_id: UUID,
    ) -> APISafeRequest:
        """Get one SAFE request."""
        return self._call(
            _get_safe_request,
            safe_request_id=safe_request_id,
        )

    @checked
    def download_document(
        self,
        safe_request_id: UUID,
    ) -> Download:
        """Download a SAFE request's document as a PDF. Close the download, or read it in a `with` block."""
        return self._download(
            _get_safe_request_document,
            safe_request_id=safe_request_id,
        )

    @checked
    def list(
        self,
    ) -> List[APISafeRequest]:
        """List your SAFE requests."""
        return self._call(
            _get_safe_requests,
        )


class AsyncSafesApi(AsyncResource):
    @checked
    async def get(
        self,
        safe_request_id: UUID,
    ) -> APISafeRequest:
        """Get one SAFE request."""
        return await self._call(
            _get_safe_request,
            safe_request_id=safe_request_id,
        )

    @checked
    async def download_document(
        self,
        safe_request_id: UUID,
    ) -> AsyncDownload:
        """Download a SAFE request's document as a PDF. Close the download, or read it in an `async with` block."""
        return await self._download(
            _get_safe_request_document,
            safe_request_id=safe_request_id,
        )

    @checked
    async def list(
        self,
    ) -> List[APISafeRequest]:
        """List your SAFE requests."""
        return await self._call(
            _get_safe_requests,
        )
