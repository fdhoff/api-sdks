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
    Offset,
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from mercury_banking.models.account_cards_response import AccountCardsResponse
from mercury_banking.models.accounts_paginated_response import AccountsPaginatedResponse
from mercury_banking.models.depository_account_statements_paginated_response import (
    DepositoryAccountStatementsPaginatedResponse,
)
from mercury_banking.models.internal_transfer_api_request import InternalTransferAPIRequest
from mercury_banking.models.internal_transfer_api_response import InternalTransferAPIResponse
from mercury_banking.models.post_transaction_api_request import PostTransactionAPIRequest
from mercury_banking.models.send_money_api_request import SendMoneyAPIRequest
from mercury_banking.models.send_money_approval_request_response import SendMoneyApprovalRequestResponse
from mercury_banking.models.transaction import Transaction
from mercury_banking.models.transactions_response import TransactionsResponse

_create_internal_transfer: Operation[InternalTransferAPIResponse] = Operation(
    id="createInternalTransfer",
    method="POST",
    path="/transfer",
    resource="accounts",
    name="transfer",
    params=(),
    response=InternalTransferAPIResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
    idempotency_key="idempotencyKey",
)
_create_transaction: Operation[Transaction] = Operation(
    id="createTransaction",
    method="POST",
    path="/account/{accountId}/transactions",
    resource="accounts",
    name="send_money",
    params=(Param("accountId", "account_id", "path"),),
    response=Transaction,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
    idempotency_key="idempotencyKey",
)
_get_account_cards: Operation[AccountCardsResponse] = Operation(
    id="getAccountCards",
    method="GET",
    path="/account/{accountId}/cards",
    resource="accounts",
    name="list_cards",
    params=(Param("accountId", "account_id", "path"),),
    response=AccountCardsResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_account_statements: Operation[DepositoryAccountStatementsPaginatedResponse] = Operation(
    id="getAccountStatements",
    method="GET",
    path="/account/{accountId}/statements",
    resource="accounts",
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
    response=DepositoryAccountStatementsPaginatedResponse,
    returns_json=True,
    iterator="iter_statements",
    item=_models.DepositoryAccountStatement,
    paging=Cursor(items="statements", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_accounts: Operation[AccountsPaginatedResponse] = Operation(
    id="getAccounts",
    method="GET",
    path="/accounts",
    resource="accounts",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("order", "order", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
    ),
    response=AccountsPaginatedResponse,
    returns_json=True,
    iterator="iter",
    item=_models.Account,
    paging=Cursor(items="accounts", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_transaction: Operation[Transaction] = Operation(
    id="getTransaction",
    method="GET",
    path="/account/{accountId}/transaction/{transactionId}",
    resource="accounts",
    name="get_transaction",
    params=(
        Param("accountId", "account_id", "path"),
        Param("transactionId", "transaction_id", "path"),
    ),
    response=Transaction,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_account_transactions: Operation[TransactionsResponse] = Operation(
    id="listAccountTransactions",
    method="GET",
    path="/account/{accountId}/transactions",
    resource="accounts",
    name="list_transactions",
    params=(
        Param("accountId", "account_id", "path"),
        Param("limit", "limit", "query"),
        Param("start", "start", "query"),
        Param("end", "end", "query"),
        Param("search", "search", "query"),
        Param("status", "status", "query"),
        Param("offset", "offset", "query"),
        Param("order", "order", "query"),
        Param("requestId", "request_id", "query"),
        Param("mercuryCategory", "mercury_category", "query"),
        Param("categoryId", "category_id", "query"),
    ),
    response=TransactionsResponse,
    returns_json=True,
    iterator="iter_transactions",
    item=_models.Transaction,
    paging=Offset(items="transactions", total="total", offset="offset"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_request_send_money: Operation[SendMoneyApprovalRequestResponse] = Operation(
    id="requestSendMoney",
    method="POST",
    path="/account/{accountId}/request-send-money",
    resource="accounts",
    name="request_send_money",
    params=(Param("accountId", "account_id", "path"),),
    response=SendMoneyApprovalRequestResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
    idempotency_key="idempotencyKey",
)

OPERATIONS = (
    _create_internal_transfer,
    _create_transaction,
    _get_account_cards,
    _get_account_statements,
    _get_accounts,
    _get_transaction,
    _list_account_transactions,
    _request_send_money,
)


class AccountsApi(Resource):
    @checked
    def transfer(
        self,
        body: Optional[Union[InternalTransferAPIRequest, Mapping[str, Any]]] = None,
    ) -> InternalTransferAPIResponse:
        """Move money between two of your accounts."""
        return self._call(
            _create_internal_transfer,
            _body=body,
        )

    @checked
    def send_money(
        self,
        account_id: UUID,
        body: Optional[Union[PostTransactionAPIRequest, Mapping[str, Any]]] = None,
    ) -> Transaction:
        """Send money from an account to a recipient."""
        return self._call(
            _create_transaction,
            account_id=account_id,
            _body=body,
        )

    @checked
    def list_cards(
        self,
        account_id: UUID,
    ) -> AccountCardsResponse:
        """List the cards issued on an account."""
        return self._call(
            _get_account_cards,
            account_id=account_id,
        )

    @checked
    def list_statements(
        self,
        account_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
    ) -> DepositoryAccountStatementsPaginatedResponse:
        """List one page of an account's statements."""
        return self._call(
            _get_account_statements,
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
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
    ) -> Iterator[_models.DepositoryAccountStatement]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_account_statements,
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
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
    ) -> AccountsPaginatedResponse:
        """List one page of your accounts."""
        return self._call(
            _get_accounts,
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
    ) -> Iterator[_models.Account]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_accounts,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )

    @checked
    def get_transaction(
        self,
        account_id: UUID,
        transaction_id: UUID,
    ) -> Transaction:
        """Get one transaction of an account."""
        return self._call(
            _get_transaction,
            account_id=account_id,
            transaction_id=transaction_id,
        )

    @checked
    def list_transactions(
        self,
        account_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
        search: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        order: Optional[StrictStr] = None,
        request_id: Optional[UUID] = None,
        mercury_category: Optional[StrictStr] = None,
        category_id: Optional[UUID] = None,
    ) -> TransactionsResponse:
        """List one page of an account's transactions."""
        return self._call(
            _list_account_transactions,
            account_id=account_id,
            limit=limit,
            start=start,
            end=end,
            search=search,
            status=status,
            offset=offset,
            order=order,
            request_id=request_id,
            mercury_category=mercury_category,
            category_id=category_id,
        )

    @checked
    def iter_transactions(
        self,
        account_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
        search: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        order: Optional[StrictStr] = None,
        request_id: Optional[UUID] = None,
        mercury_category: Optional[StrictStr] = None,
        category_id: Optional[UUID] = None,
    ) -> Iterator[_models.Transaction]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_account_transactions,
            account_id=account_id,
            limit=limit,
            start=start,
            end=end,
            search=search,
            status=status,
            offset=offset,
            order=order,
            request_id=request_id,
            mercury_category=mercury_category,
            category_id=category_id,
        )

    @checked
    def request_send_money(
        self,
        account_id: UUID,
        body: Optional[Union[SendMoneyAPIRequest, Mapping[str, Any]]] = None,
    ) -> SendMoneyApprovalRequestResponse:
        """Ask to send money from an account"""
        return self._call(
            _request_send_money,
            account_id=account_id,
            _body=body,
        )


class AsyncAccountsApi(AsyncResource):
    @checked
    async def transfer(
        self,
        body: Optional[Union[InternalTransferAPIRequest, Mapping[str, Any]]] = None,
    ) -> InternalTransferAPIResponse:
        """Move money between two of your accounts."""
        return await self._call(
            _create_internal_transfer,
            _body=body,
        )

    @checked
    async def send_money(
        self,
        account_id: UUID,
        body: Optional[Union[PostTransactionAPIRequest, Mapping[str, Any]]] = None,
    ) -> Transaction:
        """Send money from an account to a recipient."""
        return await self._call(
            _create_transaction,
            account_id=account_id,
            _body=body,
        )

    @checked
    async def list_cards(
        self,
        account_id: UUID,
    ) -> AccountCardsResponse:
        """List the cards issued on an account."""
        return await self._call(
            _get_account_cards,
            account_id=account_id,
        )

    @checked
    async def list_statements(
        self,
        account_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
    ) -> DepositoryAccountStatementsPaginatedResponse:
        """List one page of an account's statements."""
        return await self._call(
            _get_account_statements,
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
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.DepositoryAccountStatement]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_account_statements,
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
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
    ) -> AccountsPaginatedResponse:
        """List one page of your accounts."""
        return await self._call(
            _get_accounts,
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
    ) -> AsyncIterator[_models.Account]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_accounts,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )

    @checked
    async def get_transaction(
        self,
        account_id: UUID,
        transaction_id: UUID,
    ) -> Transaction:
        """Get one transaction of an account."""
        return await self._call(
            _get_transaction,
            account_id=account_id,
            transaction_id=transaction_id,
        )

    @checked
    async def list_transactions(
        self,
        account_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
        search: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        order: Optional[StrictStr] = None,
        request_id: Optional[UUID] = None,
        mercury_category: Optional[StrictStr] = None,
        category_id: Optional[UUID] = None,
    ) -> TransactionsResponse:
        """List one page of an account's transactions."""
        return await self._call(
            _list_account_transactions,
            account_id=account_id,
            limit=limit,
            start=start,
            end=end,
            search=search,
            status=status,
            offset=offset,
            order=order,
            request_id=request_id,
            mercury_category=mercury_category,
            category_id=category_id,
        )

    @checked
    def iter_transactions(
        self,
        account_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start: Optional[StrictStr] = None,
        end: Optional[StrictStr] = None,
        search: Optional[StrictStr] = None,
        status: Optional[StrictStr] = None,
        offset: Optional[Annotated[int, Field(strict=True, ge=0)]] = None,
        order: Optional[StrictStr] = None,
        request_id: Optional[UUID] = None,
        mercury_category: Optional[StrictStr] = None,
        category_id: Optional[UUID] = None,
    ) -> AsyncIterator[_models.Transaction]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_account_transactions,
            account_id=account_id,
            limit=limit,
            start=start,
            end=end,
            search=search,
            status=status,
            offset=offset,
            order=order,
            request_id=request_id,
            mercury_category=mercury_category,
            category_id=category_id,
        )

    @checked
    async def request_send_money(
        self,
        account_id: UUID,
        body: Optional[Union[SendMoneyAPIRequest, Mapping[str, Any]]] = None,
    ) -> SendMoneyApprovalRequestResponse:
        """Ask to send money from an account"""
        return await self._call(
            _request_send_money,
            account_id=account_id,
            _body=body,
        )
