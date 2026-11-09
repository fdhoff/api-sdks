# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import (
    AsyncResource,
    Cursor,
    FileInput,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from mercury_banking.models.add_recipient_request import AddRecipientRequest
from mercury_banking.models.edit_recipient_request import EditRecipientRequest
from mercury_banking.models.recipient_info import RecipientInfo
from mercury_banking.models.recipients_attachments_paginated_response import RecipientsAttachmentsPaginatedResponse
from mercury_banking.models.recipients_paginated_response import RecipientsPaginatedResponse

_create_recipient: Operation[RecipientInfo] = Operation(
    id="createRecipient",
    method="POST",
    path="/recipients",
    resource="recipients",
    name="create",
    params=(),
    response=RecipientInfo,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_delete_recipient: Operation[None] = Operation(
    id="deleteRecipient",
    method="DELETE",
    path="/recipient/{recipientId}",
    resource="recipients",
    name="delete",
    params=(Param("recipientId", "recipient_id", "path"),),
    response=None,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_recipient: Operation[RecipientInfo] = Operation(
    id="getRecipient",
    method="GET",
    path="/recipient/{recipientId}",
    resource="recipients",
    name="get",
    params=(Param("recipientId", "recipient_id", "path"),),
    response=RecipientInfo,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_recipients: Operation[RecipientsPaginatedResponse] = Operation(
    id="getRecipients",
    method="GET",
    path="/recipients",
    resource="recipients",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
    ),
    response=RecipientsPaginatedResponse,
    returns_json=True,
    iterator="iter",
    item=_models.RecipientInfo,
    paging=Cursor(items="recipients", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_recipients_attachments: Operation[RecipientsAttachmentsPaginatedResponse] = Operation(
    id="listRecipientsAttachments",
    method="GET",
    path="/recipients/attachments",
    resource="recipients",
    name="list_attachments",
    params=(
        Param("limit", "limit", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
    ),
    response=RecipientsAttachmentsPaginatedResponse,
    returns_json=True,
    iterator="iter_attachments",
    item=_models.RecipientAttachmentWithId,
    paging=Cursor(items="attachments", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_update_recipient: Operation[RecipientInfo] = Operation(
    id="updateRecipient",
    method="POST",
    path="/recipient/{recipientId}",
    resource="recipients",
    name="update",
    params=(Param("recipientId", "recipient_id", "path"),),
    response=RecipientInfo,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_upload_recipient_attachment: Operation[None] = Operation(
    id="uploadRecipientAttachment",
    method="POST",
    path="/recipient/{recipientId}/attachments",
    resource="recipients",
    name="upload_attachment",
    params=(
        Param("recipientId", "recipient_id", "path"),
        Param("file", "file", "form"),
    ),
    response=None,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _create_recipient,
    _delete_recipient,
    _get_recipient,
    _get_recipients,
    _list_recipients_attachments,
    _update_recipient,
    _upload_recipient_attachment,
)


class RecipientsApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[AddRecipientRequest, Mapping[str, Any]]] = None,
    ) -> RecipientInfo:
        """Create a payment recipient."""
        return self._call(
            _create_recipient,
            _body=body,
        )

    @checked
    def delete(
        self,
        recipient_id: UUID,
    ) -> None:
        """Delete a payment recipient."""
        return self._call(
            _delete_recipient,
            recipient_id=recipient_id,
        )

    @checked
    def get(
        self,
        recipient_id: UUID,
    ) -> RecipientInfo:
        """Get one payment recipient."""
        return self._call(
            _get_recipient,
            recipient_id=recipient_id,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> RecipientsPaginatedResponse:
        """List one page of payment recipients."""
        return self._call(
            _get_recipients,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.RecipientInfo]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_recipients,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def list_attachments(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> RecipientsAttachmentsPaginatedResponse:
        """List one page of the files attached to recipients."""
        return self._call(
            _list_recipients_attachments,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter_attachments(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.RecipientAttachmentWithId]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_recipients_attachments,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def update(
        self,
        recipient_id: UUID,
        body: Optional[Union[EditRecipientRequest, Mapping[str, Any]]] = None,
    ) -> RecipientInfo:
        """Update a payment recipient."""
        return self._call(
            _update_recipient,
            recipient_id=recipient_id,
            _body=body,
        )

    @checked
    def upload_attachment(
        self,
        recipient_id: UUID,
        *,
        file: FileInput,
    ) -> None:
        """Attach a file"""
        return self._call(
            _upload_recipient_attachment,
            recipient_id=recipient_id,
            file=file,
        )


class AsyncRecipientsApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[AddRecipientRequest, Mapping[str, Any]]] = None,
    ) -> RecipientInfo:
        """Create a payment recipient."""
        return await self._call(
            _create_recipient,
            _body=body,
        )

    @checked
    async def delete(
        self,
        recipient_id: UUID,
    ) -> None:
        """Delete a payment recipient."""
        return await self._call(
            _delete_recipient,
            recipient_id=recipient_id,
        )

    @checked
    async def get(
        self,
        recipient_id: UUID,
    ) -> RecipientInfo:
        """Get one payment recipient."""
        return await self._call(
            _get_recipient,
            recipient_id=recipient_id,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> RecipientsPaginatedResponse:
        """List one page of payment recipients."""
        return await self._call(
            _get_recipients,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.RecipientInfo]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_recipients,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    async def list_attachments(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> RecipientsAttachmentsPaginatedResponse:
        """List one page of the files attached to recipients."""
        return await self._call(
            _list_recipients_attachments,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter_attachments(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.RecipientAttachmentWithId]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_recipients_attachments,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    async def update(
        self,
        recipient_id: UUID,
        body: Optional[Union[EditRecipientRequest, Mapping[str, Any]]] = None,
    ) -> RecipientInfo:
        """Update a payment recipient."""
        return await self._call(
            _update_recipient,
            recipient_id=recipient_id,
            _body=body,
        )

    @checked
    async def upload_attachment(
        self,
        recipient_id: UUID,
        *,
        file: FileInput,
    ) -> None:
        """Attach a file"""
        return await self._call(
            _upload_recipient_attachment,
            recipient_id=recipient_id,
            file=file,
        )
