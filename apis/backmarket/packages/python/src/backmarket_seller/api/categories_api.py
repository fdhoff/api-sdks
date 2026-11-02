# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Any, AsyncIterator, Dict, Iterator, List, Mapping, Optional, Tuple, Union

from pydantic import Field, StrictFloat, StrictInt, StrictStr
from typing_extensions import Annotated

from pydantic import Field, StrictInt, field_validator
from typing import List, Optional
from typing_extensions import Annotated
from backmarket_seller.models.category_tree import CategoryTree
from backmarket_seller._runtime import AsyncResource, FileInput, Operation, Param, Resource

_get_bm_catalog_category: Operation[List[CategoryTree]] = Operation(
    id="get-bm-catalog-category",
    method="GET",
    path="/ws/category/tree",
    resource="categories",
    name="list",
    params=(),
    response=List[CategoryTree],
)
_get_bm_catalog_category_branch: Operation[CategoryTree] = Operation(
    id="get-bm-catalog-category-branch",
    method="GET",
    path="/ws/category/tree/{categoryId}",
    resource="categories",
    name="get",
    params=(Param("categoryId", "category_id", "path"),),
    response=CategoryTree,
)

OPERATIONS = (
    _get_bm_catalog_category,
    _get_bm_catalog_category_branch,
)


class CategoriesApi(Resource):
    def list(
        self,
    ) -> List[CategoryTree]:
        """List the category tree."""
        return self._call(
            _get_bm_catalog_category,
        )

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
    async def list(
        self,
    ) -> List[CategoryTree]:
        """List the category tree."""
        return await self._call(
            _get_bm_catalog_category,
        )

    async def get(
        self,
        category_id: StrictInt,
    ) -> CategoryTree:
        """Get one branch of the category tree."""
        return await self._call(
            _get_bm_catalog_category_branch,
            category_id=category_id,
        )
