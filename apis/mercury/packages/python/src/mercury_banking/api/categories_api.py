# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Iterator, Mapping, Optional, Union
from uuid import UUID

from pydantic import Field, StrictStr
from typing_extensions import Annotated

from mercury_banking import models as _models
from mercury_banking._runtime import AsyncResource, Cursor, Operation, Param, Resource, Scheme, checked
from mercury_banking.models.categories_paginated_response import CategoriesPaginatedResponse
from mercury_banking.models.category_data import CategoryData
from mercury_banking.models.create_category_api_request import CreateCategoryApiRequest
from mercury_banking.models.edit_category_api_request import EditCategoryApiRequest

_create_category: Operation[CategoryData] = Operation(
    id="createCategory",
    method="POST",
    path="/categories",
    resource="categories",
    name="create",
    params=(),
    response=CategoryData,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_delete_category: Operation[None] = Operation(
    id="deleteCategory",
    method="DELETE",
    path="/categories/{expenseCategoryId}",
    resource="categories",
    name="delete",
    params=(Param("expenseCategoryId", "expense_category_id", "path"),),
    response=None,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_edit_category: Operation[CategoryData] = Operation(
    id="editCategory",
    method="POST",
    path="/categories/{expenseCategoryId}",
    resource="categories",
    name="update",
    params=(Param("expenseCategoryId", "expense_category_id", "path"),),
    response=CategoryData,
    returns_json=True,
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)
_list_categories: Operation[CategoriesPaginatedResponse] = Operation(
    id="listCategories",
    method="GET",
    path="/categories",
    resource="categories",
    name="list",
    params=(
        Param("limit", "limit", "query"),
        Param("order", "order", "query"),
        Param("start_after", "start_after", "query"),
        Param("end_before", "end_before", "query"),
    ),
    response=CategoriesPaginatedResponse,
    returns_json=True,
    iterator="iter",
    item=_models.CategoryData,
    paging=Cursor(items="categories", next="page.nextPage", param="start_after"),
    security=((Scheme("bearerAuth", ()),),),
    host="api",
)

OPERATIONS = (
    _create_category,
    _delete_category,
    _edit_category,
    _list_categories,
)


class CategoriesApi(Resource):
    @checked
    def create(
        self,
        body: Optional[Union[CreateCategoryApiRequest, Mapping[str, Any]]] = None,
    ) -> CategoryData:
        """Create an expense category."""
        return self._call(
            _create_category,
            _body=body,
        )

    @checked
    def delete(
        self,
        expense_category_id: UUID,
    ) -> None:
        """Delete an expense category."""
        return self._call(
            _delete_category,
            expense_category_id=expense_category_id,
        )

    @checked
    def update(
        self,
        expense_category_id: UUID,
        body: Optional[Union[EditCategoryApiRequest, Mapping[str, Any]]] = None,
    ) -> CategoryData:
        """Update an expense category."""
        return self._call(
            _edit_category,
            expense_category_id=expense_category_id,
            _body=body,
        )

    @checked
    def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
    ) -> CategoriesPaginatedResponse:
        """List one page of expense categories."""
        return self._call(
            _list_categories,
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
    ) -> Iterator[_models.CategoryData]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_categories,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )


class AsyncCategoriesApi(AsyncResource):
    @checked
    async def create(
        self,
        body: Optional[Union[CreateCategoryApiRequest, Mapping[str, Any]]] = None,
    ) -> CategoryData:
        """Create an expense category."""
        return await self._call(
            _create_category,
            _body=body,
        )

    @checked
    async def delete(
        self,
        expense_category_id: UUID,
    ) -> None:
        """Delete an expense category."""
        return await self._call(
            _delete_category,
            expense_category_id=expense_category_id,
        )

    @checked
    async def update(
        self,
        expense_category_id: UUID,
        body: Optional[Union[EditCategoryApiRequest, Mapping[str, Any]]] = None,
    ) -> CategoryData:
        """Update an expense category."""
        return await self._call(
            _edit_category,
            expense_category_id=expense_category_id,
            _body=body,
        )

    @checked
    async def list(
        self,
        *,
        limit: Optional[Annotated[int, Field(le=1000, strict=True, ge=1)]] = None,
        order: Optional[StrictStr] = None,
        start_after: Optional[UUID] = None,
        end_before: Optional[UUID] = None,
    ) -> CategoriesPaginatedResponse:
        """List one page of expense categories."""
        return await self._call(
            _list_categories,
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
    ) -> AsyncIterator[_models.CategoryData]:
        """Iterate every item across all pages."""
        return self._paginate(
            _list_categories,
            limit=limit,
            order=order,
            start_after=start_after,
            end_before=end_before,
        )
