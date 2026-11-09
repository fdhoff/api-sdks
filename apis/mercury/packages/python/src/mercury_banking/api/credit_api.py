# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.credit_account_statements_paginated_response import CreditAccountStatementsPaginatedResponse
from mercury_banking.models.credit_accounts_response import CreditAccountsResponse

_get_credit_account_statements: Operation[CreditAccountStatementsPaginatedResponse] = Operation(
    id="getCreditAccountStatements",
    method="GET",
    path="/credit/{accountId}/statements",
    resource="credit",
    name="list_statements",
    params=(
        Param("accountId", "account_id", "path"),
        Param("limit", "limit", "query"),
        Param("order", "order", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("start", "start", "query"),
        Param("end", "end", "query"),
    ),
    response=CreditAccountStatementsPaginatedResponse,
    returns_json=True,
    iterator="iter_statements",
    item=_models.AccountStatement,
    paging=Cursor(items="statements", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_credit: Operation[CreditAccountsResponse] = Operation(
    id="listCredit",
    method="GET",
    path="/credit",
    resource="credit",
    name="list",
    params=(),
    response=CreditAccountsResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _get_credit_account_statements,
    _list_credit,
)


class CreditApi(Resource):
    @checked
    def list_statements(
        self,
        account_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
    ) -> CreditAccountStatementsPaginatedResponse:
        """List one page of a credit account's statements."""
        return self._call(
            _get_credit_account_statements,
            account_id=account_id,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            start=start,
            end=end,
        )

    @checked
    def iter_statements(
        self,
        account_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
    ) -> Iterator[_models.AccountStatement]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_credit_account_statements,
            account_id=account_id,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            start=start,
            end=end,
        )

    @checked
    def list(
        self,
    ) -> CreditAccountsResponse:
        """List your credit accounts."""
        return self._call(
            _list_credit,
        )


class AsyncCreditApi(AsyncResource):
    @checked
    async def list_statements(
        self,
        account_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
    ) -> CreditAccountStatementsPaginatedResponse:
        """List one page of a credit account's statements."""
        return await self._call(
            _get_credit_account_statements,
            account_id=account_id,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            start=start,
            end=end,
        )

    @checked
    def iter_statements(
        self,
        account_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.AccountStatement]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_credit_account_statements,
            account_id=account_id,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
            start=start,
            end=end,
        )

    @checked
    async def list(
        self,
    ) -> CreditAccountsResponse:
        """List your credit accounts."""
        return await self._call(
            _list_credit,
        )
