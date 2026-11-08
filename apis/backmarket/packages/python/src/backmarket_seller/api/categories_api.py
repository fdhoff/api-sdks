# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import List

from pydantic import StrictInt

from backmarket_seller._runtime import AsyncResource, Operation, Param, Resource, checked
from backmarket_seller.models.category_tree import CategoryTree

_get_bm_catalog_category: Operation[List[CategoryTree]] = Operation(
    id="get-bm-catalog-category",
    method="GET",
    path="/ws/category/tree",
    resource="categories",
    name="list",
    params=(),
    response=List[CategoryTree],
    returns_json=True,
)
_get_bm_catalog_category_branch: Operation[CategoryTree] = Operation(
    id="get-bm-catalog-category-branch",
    method="GET",
    path="/ws/category/tree/{categoryId}",
    resource="categories",
    name="get",
    params=(Param("categoryId", "category_id", "path"),),
    response=CategoryTree,
    returns_json=True,
)

OPERATIONS = (
    _get_bm_catalog_category,
    _get_bm_catalog_category_branch,
)


class CategoriesApi(Resource):
    @checked
    def list(
        self,
    ) -> List[CategoryTree]:
        """List the category tree."""
        return self._call(
            _get_bm_catalog_category,
        )

    @checked
    def get(
        self,
        category_id: StrictInt,
    ) -> CategoryTree:
        """Get one branch of the category tree."""
        return self._call(
            _get_bm_catalog_category_branch,
            category_id=category_id,
        )


class AsyncCategoriesApi(AsyncResource):
    @checked
    async def list(
        self,
    ) -> List[CategoryTree]:
        """List the category tree."""
        return await self._call(
            _get_bm_catalog_category,
        )

    @checked
    async def get(
        self,
        category_id: StrictInt,
    ) -> CategoryTree:
        """Get one branch of the category tree."""
        return await self._call(
            _get_bm_catalog_category_branch,
            category_id=category_id,
        )
