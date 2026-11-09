# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.api_v1_receipt_response import ApiV1ReceiptResponse
from mercury_banking.models.api_v1_receipt_upload_url_request import ApiV1ReceiptUploadUrlRequest
from mercury_banking.models.api_v1_receipt_upload_url_response import ApiV1ReceiptUploadUrlResponse
from mercury_banking.models.api_v1_receipts_paginated_response import ApiV1ReceiptsPaginatedResponse

_create_receipt_upload_url: Operation[ApiV1ReceiptUploadUrlResponse] = Operation(
    id="createReceiptUploadUrl",
    method="POST",
    path="/spend/receipts",
    resource="receipts",
    name="create_upload_url",
    params=(),
    response=ApiV1ReceiptUploadUrlResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_receipt: Operation[ApiV1ReceiptResponse] = Operation(
    id="getReceipt",
    method="GET",
    path="/spend/receipts/{receiptId}",
    resource="receipts",
    name="get",
    params=(Param("receiptId", "receipt_id", "path"),),
    response=ApiV1ReceiptResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_receipts: Operation[ApiV1ReceiptsPaginatedResponse] = Operation(
    id="listReceipts",
    method="GET",
    path="/spend/receipts",
    resource="receipts",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("start_at", "start_at", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
    ),
    response=ApiV1ReceiptsPaginatedResponse,
    returns_json=True,
    iterator="iter",
    item=_models.ApiV1ReceiptResponse,
    paging=Cursor(items="receipts", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_match_receipt: Operation[None] = Operation(
    id="matchReceipt",
    method="POST",
    path="/spend/receipts/{receiptId}/match",
    resource="receipts",
    name="match",
    params=(Param("receiptId", "receipt_id", "path"),),
    response=None,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _create_receipt_upload_url,
    _get_receipt,
    _list_receipts,
    _match_receipt,
)


class ReceiptsApi(Resource):
    @checked
    def create_upload_url(
        self,
        body: Optional[Union[ApiV1ReceiptUploadUrlRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1ReceiptUploadUrlResponse:
        """Get a short-lived URL to upload a receipt file to."""
        return self._call(
            _create_receipt_upload_url,
            _body=body,
        )

    @checked
    def get(
        self,
        receipt_id: UUID,
    ) -> ApiV1ReceiptResponse:
        """Get one receipt."""
        return self._call(
            _get_receipt,
            receipt_id=receipt_id,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> ApiV1ReceiptsPaginatedResponse:
        """List one page of receipts."""
        return self._call(
            _list_receipts,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.ApiV1ReceiptResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_receipts,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def match(
        self,
        receipt_id: UUID,
    ) -> None:
        """Start matching an uploaded receipt to a transaction."""
        return self._call(
            _match_receipt,
            receipt_id=receipt_id,
        )


class AsyncReceiptsApi(AsyncResource):
    @checked
    async def create_upload_url(
        self,
        body: Optional[Union[ApiV1ReceiptUploadUrlRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1ReceiptUploadUrlResponse:
        """Get a short-lived URL to upload a receipt file to."""
        return await self._call(
            _create_receipt_upload_url,
            _body=body,
        )

    @checked
    async def get(
        self,
        receipt_id: UUID,
    ) -> ApiV1ReceiptResponse:
        """Get one receipt."""
        return await self._call(
            _get_receipt,
            receipt_id=receipt_id,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> ApiV1ReceiptsPaginatedResponse:
        """List one page of receipts."""
        return await self._call(
            _list_receipts,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ApiV1ReceiptResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_receipts,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    async def match(
        self,
        receipt_id: UUID,
    ) -> None:
        """Start matching an uploaded receipt to a transaction."""
        return await self._call(
            _match_receipt,
            receipt_id=receipt_id,
        )
