# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import (
    AsyncDownload,
    AsyncResource,
    Cursor,
    Download,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from mercury_banking.models.api_v1_ar_attachment_response_data import ApiV1ArAttachmentResponseData
from mercury_banking.models.api_v1_ar_attachments_response_data import ApiV1ArAttachmentsResponseData
from mercury_banking.models.api_v1_ar_invoice_create_request import ApiV1ArInvoiceCreateRequest
from mercury_banking.models.api_v1_ar_invoice_response import ApiV1ArInvoiceResponse
from mercury_banking.models.api_v1_ar_invoice_update_request import ApiV1ArInvoiceUpdateRequest
from mercury_banking.models.api_v1_ar_invoices_paginated_response import ApiV1ArInvoicesPaginatedResponse

_cancel_invoice: Operation[None] = Operation(
    id="cancelInvoice",
    method="POST",
    path="/ar/invoices/{invoiceId}/cancel",
    resource="invoices",
    name="cancel",
    params=(Param("invoiceId", "invoice_id", "path"),),
    response=None,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_create_invoice: Operation[ApiV1ArInvoiceResponse] = Operation(
    id="createInvoice",
    method="POST",
    path="/ar/invoices",
    resource="invoices",
    name="create",
    params=(),
    response=ApiV1ArInvoiceResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_attachment: Operation[ApiV1ArAttachmentResponseData] = Operation(
    id="getAttachment",
    method="GET",
    path="/ar/attachments/{attachmentId}",
    resource="invoices",
    name="get_attachment",
    params=(Param("attachmentId", "attachment_id", "path"),),
    response=ApiV1ArAttachmentResponseData,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_invoice: Operation[ApiV1ArInvoiceResponse] = Operation(
    id="getInvoice",
    method="GET",
    path="/ar/invoices/{invoiceId}",
    resource="invoices",
    name="get",
    params=(Param("invoiceId", "invoice_id", "path"),),
    response=ApiV1ArInvoiceResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_invoice_pdf: Operation[None] = Operation(
    id="getInvoicePdf",
    method="GET",
    path="/ar/invoices/{invoiceId}/pdf",
    resource="invoices",
    name="download_pdf",
    params=(Param("invoiceId", "invoice_id", "path"),),
    response=None,
    binary_response=True,
    accept="application/pdf",
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_invoice_attachments: Operation[ApiV1ArAttachmentsResponseData] = Operation(
    id="listInvoiceAttachments",
    method="GET",
    path="/ar/invoices/{invoiceId}/attachments",
    resource="invoices",
    name="list_attachments",
    params=(Param("invoiceId", "invoice_id", "path"),),
    response=ApiV1ArAttachmentsResponseData,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_invoices: Operation[ApiV1ArInvoicesPaginatedResponse] = Operation(
    id="listInvoices",
    method="GET",
    path="/ar/invoices",
    resource="invoices",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("order", "order", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
    ),
    response=ApiV1ArInvoicesPaginatedResponse,
    returns_json=True,
    iterator="iter",
    item=_models.ApiV1ArInvoicesData,
    paging=Cursor(items="invoices", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_update_invoice: Operation[ApiV1ArInvoiceResponse] = Operation(
    id="updateInvoice",
    method="POST",
    path="/ar/invoices/{invoiceId}",
    resource="invoices",
    name="update",
    params=(Param("invoiceId", "invoice_id", "path"),),
    response=ApiV1ArInvoiceResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _cancel_invoice,
    _create_invoice,
    _get_attachment,
    _get_invoice,
    _get_invoice_pdf,
    _list_invoice_attachments,
    _list_invoices,
    _update_invoice,
)


class InvoicesApi(Resource):
    @checked
    def cancel(
        self,
        invoice_id: UUID,
    ) -> None:
        """Cancel an invoice."""
        return self._call(
            _cancel_invoice,
            invoice_id=invoice_id,
        )

    @checked
    def create(
        self,
        body: Optional[Union[ApiV1ArInvoiceCreateRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1ArInvoiceResponse:
        """Create an invoice."""
        return self._call(
            _create_invoice,
            _body=body,
        )

    @checked
    def get_attachment(
        self,
        attachment_id: UUID,
    ) -> ApiV1ArAttachmentResponseData:
        """Get one invoice attachment"""
        return self._call(
            _get_attachment,
            attachment_id=attachment_id,
        )

    @checked
    def get(
        self,
        invoice_id: UUID,
    ) -> ApiV1ArInvoiceResponse:
        """Get one invoice."""
        return self._call(
            _get_invoice,
            invoice_id=invoice_id,
        )

    @checked
    def download_pdf(
        self,
        invoice_id: UUID,
    ) -> Download:
        """Download an invoice as a PDF. Close the download, or read it in a `with` block."""
        return self._download(
            _get_invoice_pdf,
            invoice_id=invoice_id,
        )

    @checked
    def list_attachments(
        self,
        invoice_id: UUID,
    ) -> ApiV1ArAttachmentsResponseData:
        """List an invoice's attachments."""
        return self._call(
            _list_invoice_attachments,
            invoice_id=invoice_id,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
    ) -> ApiV1ArInvoicesPaginatedResponse:
        """List one page of invoices."""
        return self._call(
            _list_invoices,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
    ) -> Iterator[_models.ApiV1ArInvoicesData]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_invoices,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )

    @checked
    def update(
        self,
        invoice_id: UUID,
        body: Optional[Union[ApiV1ArInvoiceUpdateRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1ArInvoiceResponse:
        """Update an invoice."""
        return self._call(
            _update_invoice,
            invoice_id=invoice_id,
            _body=body,
        )


class AsyncInvoicesApi(AsyncResource):
    @checked
    async def cancel(
        self,
        invoice_id: UUID,
    ) -> None:
        """Cancel an invoice."""
        return await self._call(
            _cancel_invoice,
            invoice_id=invoice_id,
        )

    @checked
    async def create(
        self,
        body: Optional[Union[ApiV1ArInvoiceCreateRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1ArInvoiceResponse:
        """Create an invoice."""
        return await self._call(
            _create_invoice,
            _body=body,
        )

    @checked
    async def get_attachment(
        self,
        attachment_id: UUID,
    ) -> ApiV1ArAttachmentResponseData:
        """Get one invoice attachment"""
        return await self._call(
            _get_attachment,
            attachment_id=attachment_id,
        )

    @checked
    async def get(
        self,
        invoice_id: UUID,
    ) -> ApiV1ArInvoiceResponse:
        """Get one invoice."""
        return await self._call(
            _get_invoice,
            invoice_id=invoice_id,
        )

    @checked
    async def download_pdf(
        self,
        invoice_id: UUID,
    ) -> AsyncDownload:
        """Download an invoice as a PDF. Close the download, or read it in an `async with` block."""
        return await self._download(
            _get_invoice_pdf,
            invoice_id=invoice_id,
        )

    @checked
    async def list_attachments(
        self,
        invoice_id: UUID,
    ) -> ApiV1ArAttachmentsResponseData:
        """List an invoice's attachments."""
        return await self._call(
            _list_invoice_attachments,
            invoice_id=invoice_id,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
    ) -> ApiV1ArInvoicesPaginatedResponse:
        """List one page of invoices."""
        return await self._call(
            _list_invoices,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
    ) -> AsyncIterator[_models.ApiV1ArInvoicesData]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_invoices,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )

    @checked
    async def update(
        self,
        invoice_id: UUID,
        body: Optional[Union[ApiV1ArInvoiceUpdateRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1ArInvoiceResponse:
        """Update an invoice."""
        return await self._call(
            _update_invoice,
            invoice_id=invoice_id,
            _body=body,
        )
