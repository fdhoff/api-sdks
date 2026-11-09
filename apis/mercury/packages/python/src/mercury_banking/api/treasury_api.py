# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import (
    AsyncResource,
    Cursor,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from mercury_banking.models.treasury_accounts_paginated_response import TreasuryAccountsPaginatedResponse
from mercury_banking.models.treasury_statements_paginated_response import TreasuryStatementsPaginatedResponse
from mercury_banking.models.treasury_transactions_response import TreasuryTransactionsResponse

_get_treasury: Operation[TreasuryAccountsPaginatedResponse] = Operation(
    id="getTreasury",
    method="GET",
    path="/treasury",
    resource="treasury",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
    ),
    response=TreasuryAccountsPaginatedResponse,
    returns_json=True,
    iterator="iter",
    item=_models.TreasuryAccount,
    paging=Cursor(items="accounts", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_treasury_statements: Operation[TreasuryStatementsPaginatedResponse] = Operation(
    id="getTreasuryStatements",
    method="GET",
    path="/treasury/{treasuryId}/statements",
    resource="treasury",
    name="list_statements",
    params=(
        Param("treasuryId", "treasury_id", "path"),
        Param("limit", "limit", "query"),
        Param("order", "order", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("documentType", "document_type", "query"),
    ),
    response=TreasuryStatementsPaginatedResponse,
    returns_json=True,
    iterator="iter_statements",
    item=_models.TreasuryStatement,
    paging=Cursor(items="statements", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_treasury_transactions: Operation[TreasuryTransactionsResponse] = Operation(
    id="getTreasuryTransactions",
    method="GET",
    path="/treasury/{treasuryId}/transactions",
    resource="treasury",
    name="list_transactions",
    params=(
        Param("treasuryId", "treasury_id", "path"),
        Param("limit", "limit", "query"),
        Param("order", "order", "query"),
        Param("cursor", "cursor", "query"),
    ),
    response=TreasuryTransactionsResponse,
    returns_json=True,
    iterator="iter_transactions",
    item=_models.TreasuryTxn,
    paging=Cursor(items="transactions", next="cursor", param="cursor"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _get_treasury,
    _get_treasury_statements,
    _get_treasury_transactions,
)


class TreasuryApi(Resource):
    @checked
    def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> TreasuryAccountsPaginatedResponse:
        """List one page of treasury accounts."""
        return self._call(
            _get_treasury,
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
    ) -> Iterator[_models.TreasuryAccount]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_treasury,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def list_statements(
        self,
        treasury_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        document_type: Optional[StrictStr] = None,
    ) -> TreasuryStatementsPaginatedResponse:
        """List one page of a treasury account's statements."""
        return self._call(
            _get_treasury_statements,
            treasury_id=treasury_id,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            document_type=document_type,
        )

    @checked
    def iter_statements(
        self,
        treasury_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        document_type: Optional[StrictStr] = None,
    ) -> Iterator[_models.TreasuryStatement]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_treasury_statements,
            treasury_id=treasury_id,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            document_type=document_type,
        )

    @checked
    def list_transactions(
        self,
        treasury_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        cursor: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> TreasuryTransactionsResponse:
        """List one page of a treasury account's transactions."""
        return self._call(
            _get_treasury_transactions,
            treasury_id=treasury_id,
            limit=limit,
            order=order,
            cursor=cursor,
        )

    @checked
    def iter_transactions(
        self,
        treasury_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        cursor: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> Iterator[_models.TreasuryTxn]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_treasury_transactions,
            treasury_id=treasury_id,
            limit=limit,
            order=order,
            cursor=cursor,
        )


class AsyncTreasuryApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> TreasuryAccountsPaginatedResponse:
        """List one page of treasury accounts."""
        return await self._call(
            _get_treasury,
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
    ) -> AsyncIterator[_models.TreasuryAccount]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_treasury,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    async def list_statements(
        self,
        treasury_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        document_type: Optional[StrictStr] = None,
    ) -> TreasuryStatementsPaginatedResponse:
        """List one page of a treasury account's statements."""
        return await self._call(
            _get_treasury_statements,
            treasury_id=treasury_id,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            document_type=document_type,
        )

    @checked
    def iter_statements(
        self,
        treasury_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        document_type: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.TreasuryStatement]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_treasury_statements,
            treasury_id=treasury_id,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            document_type=document_type,
        )

    @checked
    async def list_transactions(
        self,
        treasury_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        cursor: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> TreasuryTransactionsResponse:
        """List one page of a treasury account's transactions."""
        return await self._call(
            _get_treasury_transactions,
            treasury_id=treasury_id,
            limit=limit,
            order=order,
            cursor=cursor,
        )

    @checked
    def iter_transactions(
        self,
        treasury_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        cursor: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
    ) -> AsyncIterator[_models.TreasuryTxn]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_treasury_transactions,
            treasury_id=treasury_id,
            limit=limit,
            order=order,
            cursor=cursor,
        )
