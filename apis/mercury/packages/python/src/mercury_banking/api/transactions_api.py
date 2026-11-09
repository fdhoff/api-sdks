# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, List, Mapping, Optional, Union
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, FileInput, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.api_update_transaction_request import ApiUpdateTransactionRequest
from mercury_banking.models.transaction import Transaction
from mercury_banking.models.transactions_paginated_response import TransactionsPaginatedResponse
from mercury_banking.models.uploaded_attachment import UploadedAttachment

_get_transaction_by_id: Operation[Transaction] = Operation(
    id="getTransactionById",
    method="GET",
    path="/transaction/{transactionId}",
    resource="transactions",
    name="get",
    params=(Param("transactionId", "transaction_id", "path"),),
    response=Transaction,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_transactions: Operation[TransactionsPaginatedResponse] = Operation(
    id="listTransactions",
    method="GET",
    path="/transactions",
    resource="transactions",
    name="list",
    params=(
        Param("status", "status", "query"),
        Param("search", "search", "query"),
        Param("start", "start", "query"),
        Param("end", "end", "query"),
        Param("postedStart", "posted_start", "query"),
        Param("postedEnd", "posted_end", "query"),
        Param("accountId", "account_id", "query"),
        Param("cardId", "card_id", "query"),
        Param("mercuryCategory", "mercury_category", "query"),
        Param("categoryId", "category_id", "query"),
        Param("start_at", "start_at", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("limit", "limit", "query"),
        Param("order", "order", "query"),
    ),
    response=TransactionsPaginatedResponse,
    returns_json=True,
    iterator="iter",
    item=_models.Transaction,
    paging=Cursor(items="transactions", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_update_transaction: Operation[Transaction] = Operation(
    id="updateTransaction",
    method="PATCH",
    path="/transaction/{transactionId}",
    resource="transactions",
    name="update",
    params=(Param("transactionId", "transaction_id", "path"),),
    response=Transaction,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_upload_transaction_attachment: Operation[UploadedAttachment] = Operation(
    id="uploadTransactionAttachment",
    method="POST",
    path="/transaction/{transactionId}/attachments",
    resource="transactions",
    name="upload_attachment",
    params=(
        Param("transactionId", "transaction_id", "path"),
        Param("attachmentType", "attachment_type", "form"),
        Param("file", "file", "form"),
    ),
    response=UploadedAttachment,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _get_transaction_by_id,
    _list_transactions,
    _update_transaction,
    _upload_transaction_attachment,
)


class TransactionsApi(Resource):
    @checked
    def get(
        self,
        transaction_id: UUID,
    ) -> Transaction:
        """Get one transaction."""
        return self._call(
            _get_transaction_by_id,
            transaction_id=transaction_id,
        )

    @checked
    def list(
        self,
        *,
        status: Optional[List[StrictStr]] = None,
        search: Optional[StrictStr] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
        posted_start: Optional[StrictStr] = None,
        posted_end: Optional[StrictStr] = None,
        account_id: Optional[List[UUID]] = None,
        card_id: Optional[List[StrictStr]] = None,
        mercury_category: Optional[StrictStr] = None,
        category_id: Optional[StrictStr] = None,
        start_at: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
    ) -> TransactionsPaginatedResponse:
        """List one page of transactions across your accounts."""
        return self._call(
            _list_transactions,
            status=status,
            search=search,
            start=start,
            end=end,
            posted_start=posted_start,
            posted_end=posted_end,
            account_id=account_id,
            card_id=card_id,
            mercury_category=mercury_category,
            category_id=category_id,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            limit=limit,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        status: Optional[List[StrictStr]] = None,
        search: Optional[StrictStr] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
        posted_start: Optional[StrictStr] = None,
        posted_end: Optional[StrictStr] = None,
        account_id: Optional[List[UUID]] = None,
        card_id: Optional[List[StrictStr]] = None,
        mercury_category: Optional[StrictStr] = None,
        category_id: Optional[StrictStr] = None,
        start_at: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.Transaction]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_transactions,
            status=status,
            search=search,
            start=start,
            end=end,
            posted_start=posted_start,
            posted_end=posted_end,
            account_id=account_id,
            card_id=card_id,
            mercury_category=mercury_category,
            category_id=category_id,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            limit=limit,
            order=order,
        )

    @checked
    def update(
        self,
        transaction_id: UUID,
        body: Optional[Union[ApiUpdateTransactionRequest, Mapping[str, Any]]] = None,
    ) -> Transaction:
        """Update a transaction's note or category."""
        return self._call(
            _update_transaction,
            transaction_id=transaction_id,
            _body=body,
        )

    @checked
    def upload_attachment(
        self,
        transaction_id: UUID,
        *,
        file: FileInput,
        attachment_type: Optional[StrictStr] = None,
    ) -> UploadedAttachment:
        """Attach a file"""
        return self._call(
            _upload_transaction_attachment,
            transaction_id=transaction_id,
            attachment_type=attachment_type,
            file=file,
        )


class AsyncTransactionsApi(AsyncResource):
    @checked
    async def get(
        self,
        transaction_id: UUID,
    ) -> Transaction:
        """Get one transaction."""
        return await self._call(
            _get_transaction_by_id,
            transaction_id=transaction_id,
        )

    @checked
    async def list(
        self,
        *,
        status: Optional[List[StrictStr]] = None,
        search: Optional[StrictStr] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
        posted_start: Optional[StrictStr] = None,
        posted_end: Optional[StrictStr] = None,
        account_id: Optional[List[UUID]] = None,
        card_id: Optional[List[StrictStr]] = None,
        mercury_category: Optional[StrictStr] = None,
        category_id: Optional[StrictStr] = None,
        start_at: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
    ) -> TransactionsPaginatedResponse:
        """List one page of transactions across your accounts."""
        return await self._call(
            _list_transactions,
            status=status,
            search=search,
            start=start,
            end=end,
            posted_start=posted_start,
            posted_end=posted_end,
            account_id=account_id,
            card_id=card_id,
            mercury_category=mercury_category,
            category_id=category_id,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            limit=limit,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        status: Optional[List[StrictStr]] = None,
        search: Optional[StrictStr] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
        posted_start: Optional[StrictStr] = None,
        posted_end: Optional[StrictStr] = None,
        account_id: Optional[List[UUID]] = None,
        card_id: Optional[List[StrictStr]] = None,
        mercury_category: Optional[StrictStr] = None,
        category_id: Optional[StrictStr] = None,
        start_at: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.Transaction]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_transactions,
            status=status,
            search=search,
            start=start,
            end=end,
            posted_start=posted_start,
            posted_end=posted_end,
            account_id=account_id,
            card_id=card_id,
            mercury_category=mercury_category,
            category_id=category_id,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            limit=limit,
            order=order,
        )

    @checked
    async def update(
        self,
        transaction_id: UUID,
        body: Optional[Union[ApiUpdateTransactionRequest, Mapping[str, Any]]] = None,
    ) -> Transaction:
        """Update a transaction's note or category."""
        return await self._call(
            _update_transaction,
            transaction_id=transaction_id,
            _body=body,
        )

    @checked
    async def upload_attachment(
        self,
        transaction_id: UUID,
        *,
        file: FileInput,
        attachment_type: Optional[StrictStr] = None,
    ) -> UploadedAttachment:
        """Attach a file"""
        return await self._call(
            _upload_transaction_attachment,
            transaction_id=transaction_id,
            attachment_type=attachment_type,
            file=file,
        )
