# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.send_money_approval_request_response import SendMoneyApprovalRequestResponse
from mercury_banking.models.send_money_approval_requests_paginated_response import (
    SendMoneyApprovalRequestsPaginatedResponse,
)

_get_send_money_approval_request: Operation[SendMoneyApprovalRequestResponse] = Operation(
    id="getSendMoneyApprovalRequest",
    method="GET",
    path="/request-send-money/{requestId}",
    resource="send_money_requests",
    name="get",
    params=(Param("requestId", "request_id", "path"),),
    response=SendMoneyApprovalRequestResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_send_money_approval_requests: Operation[SendMoneyApprovalRequestsPaginatedResponse] = Operation(
    id="listSendMoneyApprovalRequests",
    method="GET",
    path="/request-send-money",
    resource="send_money_requests",
    name="list",
    params=(
        Param("accountId", "account_id", "query"),
        Param("status", "status", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("limit", "limit", "query"),
    ),
    response=SendMoneyApprovalRequestsPaginatedResponse,
    returns_json=True,
    iterator="iter",
    item=_models.SendMoneyApprovalRequestResponse,
    paging=Cursor(items="requests", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _get_send_money_approval_request,
    _list_send_money_approval_requests,
)


class SendMoneyRequestsApi(Resource):
    @checked
    def get(
        self,
        request_id: UUID,
    ) -> SendMoneyApprovalRequestResponse:
        """Get one request to send money."""
        return self._call(
            _get_send_money_approval_request,
            request_id=request_id,
        )

    @checked
    def list(
        self,
        *,
        account_id: Optional[UUID] = None,
        status: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
    ) -> SendMoneyApprovalRequestsPaginatedResponse:
        """List one page of requests to send money."""
        return self._call(
            _list_send_money_approval_requests,
            account_id=account_id,
            status=status,
            start_after=start_after,
            end_before=end_before,
            limit=limit,
        )

    @checked
    def iter(
        self,
        *,
        account_id: Optional[UUID] = None,
        status: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
    ) -> Iterator[_models.SendMoneyApprovalRequestResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_send_money_approval_requests,
            account_id=account_id,
            status=status,
            start_after=start_after,
            end_before=end_before,
            limit=limit,
        )


class AsyncSendMoneyRequestsApi(AsyncResource):
    @checked
    async def get(
        self,
        request_id: UUID,
    ) -> SendMoneyApprovalRequestResponse:
        """Get one request to send money."""
        return await self._call(
            _get_send_money_approval_request,
            request_id=request_id,
        )

    @checked
    async def list(
        self,
        *,
        account_id: Optional[UUID] = None,
        status: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
    ) -> SendMoneyApprovalRequestsPaginatedResponse:
        """List one page of requests to send money."""
        return await self._call(
            _list_send_money_approval_requests,
            account_id=account_id,
            status=status,
            start_after=start_after,
            end_before=end_before,
            limit=limit,
        )

    @checked
    def iter(
        self,
        *,
        account_id: Optional[UUID] = None,
        status: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
    ) -> AsyncIterator[_models.SendMoneyApprovalRequestResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_send_money_approval_requests,
            account_id=account_id,
            status=status,
            start_after=start_after,
            end_before=end_before,
            limit=limit,
        )
