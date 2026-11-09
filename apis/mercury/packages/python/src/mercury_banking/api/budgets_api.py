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
    Operation,
    Param,
    Resource,
    Scheme,
    checked,
)
from mercury_banking.models.api_v1_assign_transaction_request import ApiV1AssignTransactionRequest
from mercury_banking.models.api_v1_budget_expenditures_response import ApiV1BudgetExpendituresResponse
from mercury_banking.models.api_v1_budget_id_response import ApiV1BudgetIdResponse
from mercury_banking.models.api_v1_budget_members_response import ApiV1BudgetMembersResponse
from mercury_banking.models.api_v1_create_budget_request import ApiV1CreateBudgetRequest
from mercury_banking.models.api_v1_spend_budget_response import ApiV1SpendBudgetResponse
from mercury_banking.models.api_v1_spend_budgets_response import ApiV1SpendBudgetsResponse
from mercury_banking.models.api_v1_update_budget_request import ApiV1UpdateBudgetRequest

_archive_budget: Operation[None] = Operation(
    id="archiveBudget",
    method="POST",
    path="/spend/budgets/{budgetId}/archive",
    resource="budgets",
    name="archive",
    params=(Param("budgetId", "budget_id", "path"),),
    response=None,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_assign_transaction_to_budget: Operation[None] = Operation(
    id="assignTransactionToBudget",
    method="POST",
    path="/spend/budgets/{budgetId}/assign-transaction",
    resource="budgets",
    name="assign_transaction",
    params=(Param("budgetId", "budget_id", "path"),),
    response=None,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_create_budget: Operation[ApiV1BudgetIdResponse] = Operation(
    id="createBudget",
    method="POST",
    path="/spend/budgets",
    resource="budgets",
    name="create",
    params=(),
    response=ApiV1BudgetIdResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_budget: Operation[ApiV1SpendBudgetResponse] = Operation(
    id="getBudget",
    method="GET",
    path="/spend/budgets/{budgetId}",
    resource="budgets",
    name="get",
    params=(Param("budgetId", "budget_id", "path"),),
    response=ApiV1SpendBudgetResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_budget_expenditures: Operation[ApiV1BudgetExpendituresResponse] = Operation(
    id="getBudgetExpenditures",
    method="GET",
    path="/spend/budgets/{budgetId}/expenditures",
    resource="budgets",
    name="list_expenditures",
    params=(
        Param("budgetId", "budget_id", "path"),
        Param("limit", "limit", "query"),
        Param("start_at", "start_at", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
    ),
    response=ApiV1BudgetExpendituresResponse,
    returns_json=True,
    iterator="iter_expenditures",
    item=_models.ApiV1BudgetExpenditure,
    paging=Cursor(items="expenditures", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_get_budget_members: Operation[ApiV1BudgetMembersResponse] = Operation(
    id="getBudgetMembers",
    method="GET",
    path="/spend/budgets/{budgetId}/members",
    resource="budgets",
    name="list_members",
    params=(
        Param("budgetId", "budget_id", "path"),
        Param("limit", "limit", "query"),
        Param("start_at", "start_at", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
    ),
    response=ApiV1BudgetMembersResponse,
    returns_json=True,
    iterator="iter_members",
    item=_models.ApiV1BudgetMember,
    paging=Cursor(items="members", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_budgets: Operation[ApiV1SpendBudgetsResponse] = Operation(
    id="listBudgets",
    method="GET",
    path="/spend/budgets",
    resource="budgets",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("start_at", "start_at", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
        Param("order", "order", "query"),
    ),
    response=ApiV1SpendBudgetsResponse,
    returns_json=True,
    iterator="iter",
    item=_models.ApiV1SpendBudgetResponse,
    paging=Cursor(items="budgets", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_update_budget: Operation[ApiV1BudgetIdResponse] = Operation(
    id="updateBudget",
    method="POST",
    path="/spend/budgets/{budgetId}",
    resource="budgets",
    name="update",
    params=(Param("budgetId", "budget_id", "path"),),
    response=ApiV1BudgetIdResponse,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _archive_budget,
    _assign_transaction_to_budget,
    _create_budget,
    _get_budget,
    _get_budget_expenditures,
    _get_budget_members,
    _list_budgets,
    _update_budget,
)


class BudgetsApi(Resource):
    @checked
    def archive(
        self,
        budget_id: UUID,
    ) -> None:
        """Archive a published budget"""
        return self._call(
            _archive_budget,
            budget_id=budget_id,
        )

    @checked
    def assign_transaction(
        self,
        budget_id: UUID,
        body: Optional[Union[ApiV1AssignTransactionRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Count a transaction against a budget."""
        return self._call(
            _assign_transaction_to_budget,
            budget_id=budget_id,
            _body=body,
        )

    @checked
    def create(
        self,
        body: Optional[Union[ApiV1CreateBudgetRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1BudgetIdResponse:
        """Create a budget."""
        return self._call(
            _create_budget,
            _body=body,
        )

    @checked
    def get(
        self,
        budget_id: UUID,
    ) -> ApiV1SpendBudgetResponse:
        """Get one budget."""
        return self._call(
            _get_budget,
            budget_id=budget_id,
        )

    @checked
    def list_expenditures(
        self,
        budget_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> ApiV1BudgetExpendituresResponse:
        """List one page of a budget's spending."""
        return self._call(
            _get_budget_expenditures,
            budget_id=budget_id,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter_expenditures(
        self,
        budget_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.ApiV1BudgetExpenditure]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_budget_expenditures,
            budget_id=budget_id,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def list_members(
        self,
        budget_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> ApiV1BudgetMembersResponse:
        """List one page of a budget's members."""
        return self._call(
            _get_budget_members,
            budget_id=budget_id,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter_members(
        self,
        budget_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> Iterator[_models.ApiV1BudgetMember]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_budget_members,
            budget_id=budget_id,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
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
    ) -> ApiV1SpendBudgetsResponse:
        """List one page of budgets."""
        return self._call(
            _list_budgets,
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
    ) -> Iterator[_models.ApiV1SpendBudgetResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_budgets,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def update(
        self,
        budget_id: UUID,
        body: Optional[Union[ApiV1UpdateBudgetRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1BudgetIdResponse:
        """Update a budget."""
        return self._call(
            _update_budget,
            budget_id=budget_id,
            _body=body,
        )


class AsyncBudgetsApi(AsyncResource):
    @checked
    async def archive(
        self,
        budget_id: UUID,
    ) -> None:
        """Archive a published budget"""
        return await self._call(
            _archive_budget,
            budget_id=budget_id,
        )

    @checked
    async def assign_transaction(
        self,
        budget_id: UUID,
        body: Optional[Union[ApiV1AssignTransactionRequest, Mapping[str, Any]]] = None,
    ) -> None:
        """Count a transaction against a budget."""
        return await self._call(
            _assign_transaction_to_budget,
            budget_id=budget_id,
            _body=body,
        )

    @checked
    async def create(
        self,
        body: Optional[Union[ApiV1CreateBudgetRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1BudgetIdResponse:
        """Create a budget."""
        return await self._call(
            _create_budget,
            _body=body,
        )

    @checked
    async def get(
        self,
        budget_id: UUID,
    ) -> ApiV1SpendBudgetResponse:
        """Get one budget."""
        return await self._call(
            _get_budget,
            budget_id=budget_id,
        )

    @checked
    async def list_expenditures(
        self,
        budget_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> ApiV1BudgetExpendituresResponse:
        """List one page of a budget's spending."""
        return await self._call(
            _get_budget_expenditures,
            budget_id=budget_id,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter_expenditures(
        self,
        budget_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ApiV1BudgetExpenditure]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_budget_expenditures,
            budget_id=budget_id,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    async def list_members(
        self,
        budget_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> ApiV1BudgetMembersResponse:
        """List one page of a budget's members."""
        return await self._call(
            _get_budget_members,
            budget_id=budget_id,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    def iter_members(
        self,
        budget_id: UUID,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        start_at: Optional[UUID] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
        order: Optional[StrictStr] = None,
    ) -> AsyncIterator[_models.ApiV1BudgetMember]:
        """Iterate every item across all pages."""
        return self._paginate(
            _get_budget_members,
            budget_id=budget_id,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
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
    ) -> ApiV1SpendBudgetsResponse:
        """List one page of budgets."""
        return await self._call(
            _list_budgets,
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
    ) -> AsyncIterator[_models.ApiV1SpendBudgetResponse]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_budgets,
            limit=limit,
            start_at=start_at,
            start_after=start_after,
            end_before=end_before,
            order=order,
        )

    @checked
    async def update(
        self,
        budget_id: UUID,
        body: Optional[Union[ApiV1UpdateBudgetRequest, Mapping[str, Any]]] = None,
    ) -> ApiV1BudgetIdResponse:
        """Update a budget."""
        return await self._call(
            _update_budget,
            budget_id=budget_id,
            _body=body,
        )
