# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import AsyncIterator, Iterator, Optional
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.auto_transfer_rules_response import AutoTransferRulesResponse

_get_auto_transfer_rules: Operation[AutoTransferRulesResponse] = Operation(
    id="getAutoTransferRules",
    method="GET",
    path="/auto-transfer-rules",
    resource="auto_transfer_rules",
    name="list",
    params=(
        Param("accountId", "account_id", "query"),
        Param("limit", "limit", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
    ),
    response=AutoTransferRulesResponse,
    returns_json=True,
    iterator="iter",
    item=_models.AutoTransferRule,
    paging=Cursor(items="rules", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (_get_auto_transfer_rules,)


class AutoTransferRulesApi(Resource):
    @checked
    def list(
        self,
        *,
        account_id: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> AutoTransferRulesResponse:
        """List one page of automatic transfer rules."""
        return self._call(
            _get_auto_transfer_rules,
            account_id=account_id,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        account_id: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.AutoTransferRule]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_auto_transfer_rules,
            account_id=account_id,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )


class AsyncAutoTransferRulesApi(AsyncResource):
    @checked
    async def list(
        self,
        *,
        account_id: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> AutoTransferRulesResponse:
        """List one page of automatic transfer rules."""
        return await self._call(
            _get_auto_transfer_rules,
            account_id=account_id,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter(
        self,
        *,
        account_id: Optional[UUID] = None,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.AutoTransferRule]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_auto_transfer_rules,
            account_id=account_id,
            limit=limit,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )
