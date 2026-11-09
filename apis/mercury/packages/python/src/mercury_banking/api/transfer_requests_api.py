# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.transfer_money_approval_request_api_request import TransferMoneyApprovalRequestAPIRequest
from mercury_banking.models.transfer_money_approval_request_response import TransferMoneyApprovalRequestResponse
from mercury_banking.models.transfer_money_approval_requests_paginated_response import (
    TransferMoneyApprovalRequestsPaginatedResponse,
)

_get_transfer_money_approval_request: Operation[TransferMoneyApprovalRequestResponse] = Operation(
    id="getTransferMoneyApprovalRequest",
    method="GET",
    path="/request-transfer/{requestId}",
    resource="transfer_requests",
    name="get",
    params=(Param("requestId", "request_id", "path"),),
    response=TransferMoneyApprovalRequestResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_transfer_money_approval_requests: Operation[TransferMoneyApprovalRequestsPaginatedResponse] = Operation(
    id="listTransferMoneyApprovalRequests",
    method="GET",
    path="/request-transfer",
    resource="transfer_requests",
    name="list",
    params=(
        Param("sourceAccountId", "source_account_id", "query"),
        Param("destinationAccountId", "destination_account_id", "query"),
        Param("status", "status", "query"),
        Param("start_at", "start_at", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("limit", "limit", "query"),
        Param("order", "order", "query"),
    ),
    response=TransferMoneyApprovalRequestsPaginatedResponse,
    returns_json=True,
    iterator="iter",
    item=_models.TransferMoneyApprovalRequestResponse,
    paging=Cursor(items="requests", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_request_transfer_money: Operation[TransferMoneyApprovalRequestResponse] = Operation(
    id="requestTransferMoney",
    method="POST",
    path="/request-transfer",
    resource="transfer_requests",
    name="create",
    params=(),
    response=TransferMoneyApprovalRequestResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
    idempotency_key="idempotencyKey",
)

OPERATIONS = (
    _get_transfer_money_approval_request,
    _list_transfer_money_approval_requests,
    _request_transfer_money,
)


class TransferRequestsApi(Resource):
    @checked
    def get(
        self,
        request_id: UUID,
    ) -> TransferMoneyApprovalRequestResponse:
        """Get one request to move money between accounts."""
        return self._call(
            _get_transfer_money_approval_request,
            request_id=request_id,
        )

    @checked
    def list(
        self,
        *,
        source_account_id: Optional[UUID] = None,
        destination_account_id: Optional[UUID] = None,
        status: Optional[StrictStr] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
    ) -> TransferMoneyApprovalRequestsPaginatedResponse:
        """List one page of requests to move money between accounts."""
        return self._call(
            _list_transfer_money_approval_requests,
            source_account_id=source_account_id,
            destination_account_id=destination_account_id,
            status=status,
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
        source_account_id: Optional[UUID] = None,
        destination_account_id: Optional[UUID] = None,
        status: Optional[StrictStr] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.TransferMoneyApprovalRequestResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_transfer_money_approval_requests,
            source_account_id=source_account_id,
            destination_account_id=destination_account_id,
            status=status,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            limit=limit,
            order=order,
        )

    @checked
    def create(
        self,
        body: Optional[Union[TransferMoneyApprovalRequestAPIRequest, Mapping[str, Any]]] = None,
    ) -> TransferMoneyApprovalRequestResponse:
        """Ask to move money between accounts"""
        return self._call(
            _request_transfer_money,
            _body=body,
        )


class AsyncTransferRequestsApi(AsyncResource):
    @checked
    async def get(
        self,
        request_id: UUID,
    ) -> TransferMoneyApprovalRequestResponse:
        """Get one request to move money between accounts."""
        return await self._call(
            _get_transfer_money_approval_request,
            request_id=request_id,
        )

    @checked
    async def list(
        self,
        *,
        source_account_id: Optional[UUID] = None,
        destination_account_id: Optional[UUID] = None,
        status: Optional[StrictStr] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
    ) -> TransferMoneyApprovalRequestsPaginatedResponse:
        """List one page of requests to move money between accounts."""
        return await self._call(
            _list_transfer_money_approval_requests,
            source_account_id=source_account_id,
            destination_account_id=destination_account_id,
            status=status,
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
        source_account_id: Optional[UUID] = None,
        destination_account_id: Optional[UUID] = None,
        status: Optional[StrictStr] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.TransferMoneyApprovalRequestResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_transfer_money_approval_requests,
            source_account_id=source_account_id,
            destination_account_id=destination_account_id,
            status=status,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            limit=limit,
            order=order,
        )

    @checked
    async def create(
        self,
        body: Optional[Union[TransferMoneyApprovalRequestAPIRequest, Mapping[str, Any]]] = None,
    ) -> TransferMoneyApprovalRequestResponse:
        """Ask to move money between accounts"""
        return await self._call(
            _request_transfer_money,
            _body=body,
        )
