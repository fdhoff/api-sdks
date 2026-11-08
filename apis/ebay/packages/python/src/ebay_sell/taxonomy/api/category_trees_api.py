# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.

from __future__ import annotations

from typing import Optional

from pydantic import StrictStr

from ebay_sell._runtime import AsyncResource, Operation, Param, Resource, Scheme, checked
from ebay_sell.taxonomy.models.aspect_metadata import AspectMetadata
from ebay_sell.taxonomy.models.base_category_tree import BaseCategoryTree
from ebay_sell.taxonomy.models.category_subtree import CategorySubtree
from ebay_sell.taxonomy.models.category_suggestion_response import CategorySuggestionResponse
from ebay_sell.taxonomy.models.category_tree import CategoryTree
from ebay_sell.taxonomy.models.expired_categories import ExpiredCategories
from ebay_sell.taxonomy.models.get_categories_aspect_response import GetCategoriesAspectResponse
from ebay_sell.taxonomy.models.get_compatibility_metadata_response import GetCompatibilityMetadataResponse
from ebay_sell.taxonomy.models.get_compatibility_property_values_response import GetCompatibilityPropertyValuesResponse

_fetch_item_aspects: Operation[GetCategoriesAspectResponse] = Operation(
    id="fetchItemAspects",
    method="GET",
    path="/commerce/taxonomy/v1/category_tree/{category_tree_id}/fetch_item_aspects",
    resource="category_trees",
    name="fetch_item_aspects",
    params=(Param("category_tree_id", "category_tree_id", "path"),),
    response=GetCategoriesAspectResponse,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/metadata.insights",
                ),
            ),
        ),
    ),
    host="api",
)
_get_category_subtree: Operation[CategorySubtree] = Operation(
    id="getCategorySubtree",
    method="GET",
    path="/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_subtree",
    resource="category_trees",
    name="get_subtree",
    params=(
        Param("category_tree_id", "category_tree_id", "path"),
        Param("category_id", "category_id", "query"),
    ),
    response=CategorySubtree,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_category_suggestions: Operation[CategorySuggestionResponse] = Operation(
    id="getCategorySuggestions",
    method="GET",
    path="/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_category_suggestions",
    resource="category_trees",
    name="get_suggestions",
    params=(
        Param("category_tree_id", "category_tree_id", "path"),
        Param("q", "q", "query"),
    ),
    response=CategorySuggestionResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_category_tree: Operation[CategoryTree] = Operation(
    id="getCategoryTree",
    method="GET",
    path="/commerce/taxonomy/v1/category_tree/{category_tree_id}",
    resource="category_trees",
    name="get",
    params=(Param("category_tree_id", "category_tree_id", "path"),),
    response=CategoryTree,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_compatibility_properties: Operation[GetCompatibilityMetadataResponse] = Operation(
    id="getCompatibilityProperties",
    method="GET",
    path="/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_properties",
    resource="category_trees",
    name="get_compatibility_properties",
    params=(
        Param("category_tree_id", "category_tree_id", "path"),
        Param("category_id", "category_id", "query"),
    ),
    response=GetCompatibilityMetadataResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_compatibility_property_values: Operation[GetCompatibilityPropertyValuesResponse] = Operation(
    id="getCompatibilityPropertyValues",
    method="GET",
    path="/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_compatibility_property_values",
    resource="category_trees",
    name="get_compatibility_property_values",
    params=(
        Param("category_tree_id", "category_tree_id", "path"),
        Param("compatibility_property", "compatibility_property", "query"),
        Param("category_id", "category_id", "query"),
        Param("filter", "filter", "query"),
    ),
    response=GetCompatibilityPropertyValuesResponse,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_default_category_tree_id: Operation[BaseCategoryTree] = Operation(
    id="getDefaultCategoryTreeId",
    method="GET",
    path="/commerce/taxonomy/v1/get_default_category_tree_id",
    resource="category_trees",
    name="get_default_id",
    params=(Param("marketplace_id", "marketplace_id", "query"),),
    response=BaseCategoryTree,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_expired_categories: Operation[ExpiredCategories] = Operation(
    id="getExpiredCategories",
    method="GET",
    path="/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_expired_categories",
    resource="category_trees",
    name="get_expired_categories",
    params=(Param("category_tree_id", "category_tree_id", "path"),),
    response=ExpiredCategories,
    returns_json=True,
    security=((Scheme("api_auth", ("https://api.ebay.com/oauth/api_scope",)),),),
    host="api",
)
_get_item_aspects_for_category: Operation[AspectMetadata] = Operation(
    id="getItemAspectsForCategory",
    method="GET",
    path="/commerce/taxonomy/v1/category_tree/{category_tree_id}/get_item_aspects_for_category",
    resource="category_trees",
    name="get_item_aspects",
    params=(
        Param("category_tree_id", "category_tree_id", "path"),
        Param("category_id", "category_id", "query"),
    ),
    response=AspectMetadata,
    returns_json=True,
    security=(
        (
            Scheme(
                "api_auth",
                (
                    "https://api.ebay.com/oauth/api_scope",
                    "https://api.ebay.com/oauth/api_scope/metadata.insights",
                ),
            ),
        ),
    ),
    host="api",
)

OPERATIONS = (
    _fetch_item_aspects,
    _get_category_subtree,
    _get_category_suggestions,
    _get_category_tree,
    _get_compatibility_properties,
    _get_compatibility_property_values,
    _get_default_category_tree_id,
    _get_expired_categories,
    _get_item_aspects_for_category,
)


class CategoryTreesApi(Resource):
    @checked
    def fetch_item_aspects(
        self,
        category_tree_id: StrictStr,
    ) -> GetCategoriesAspectResponse:
        """Get the item aspects of every leaf category in a tree"""
        return self._call(
            _fetch_item_aspects,
            category_tree_id=category_tree_id,
        )

    @checked
    def get_subtree(
        self,
        category_tree_id: StrictStr,
        *,
        category_id: StrictStr,
    ) -> CategorySubtree:
        """Get the part of a category tree under one category."""
        return self._call(
            _get_category_subtree,
            category_tree_id=category_tree_id,
            category_id=category_id,
        )

    @checked
    def get_suggestions(
        self,
        category_tree_id: StrictStr,
        *,
        q: StrictStr,
    ) -> CategorySuggestionResponse:
        """Suggest leaf categories for a search phrase."""
        return self._call(
            _get_category_suggestions,
            category_tree_id=category_tree_id,
            q=q,
        )

    @checked
    def get(
        self,
        category_tree_id: StrictStr,
    ) -> CategoryTree:
        """Get a whole category tree."""
        return self._call(
            _get_category_tree,
            category_tree_id=category_tree_id,
        )

    @checked
    def get_compatibility_properties(
        self,
        category_tree_id: StrictStr,
        *,
        category_id: StrictStr,
    ) -> GetCompatibilityMetadataResponse:
        """List the parts compatibility properties of a category."""
        return self._call(
            _get_compatibility_properties,
            category_tree_id=category_tree_id,
            category_id=category_id,
        )

    @checked
    def get_compatibility_property_values(
        self,
        category_tree_id: StrictStr,
        *,
        compatibility_property: StrictStr,
        category_id: StrictStr,
        filter: Optional[StrictStr] = None,
    ) -> GetCompatibilityPropertyValuesResponse:
        """List the values of one parts compatibility property."""
        return self._call(
            _get_compatibility_property_values,
            category_tree_id=category_tree_id,
            compatibility_property=compatibility_property,
            category_id=category_id,
            filter=filter,
        )

    @checked
    def get_default_id(
        self,
        *,
        marketplace_id: StrictStr,
    ) -> BaseCategoryTree:
        """Get the ID of a marketplace's default category tree."""
        return self._call(
            _get_default_category_tree_id,
            marketplace_id=marketplace_id,
        )

    @checked
    def get_expired_categories(
        self,
        category_tree_id: StrictStr,
    ) -> ExpiredCategories:
        """List the leaf categories that expired and what replaced them."""
        return self._call(
            _get_expired_categories,
            category_tree_id=category_tree_id,
        )

    @checked
    def get_item_aspects(
        self,
        category_tree_id: StrictStr,
        *,
        category_id: StrictStr,
    ) -> AspectMetadata:
        """List the item aspects of one leaf category."""
        return self._call(
            _get_item_aspects_for_category,
            category_tree_id=category_tree_id,
            category_id=category_id,
        )


class AsyncCategoryTreesApi(AsyncResource):
    @checked
    async def fetch_item_aspects(
        self,
        category_tree_id: StrictStr,
    ) -> GetCategoriesAspectResponse:
        """Get the item aspects of every leaf category in a tree"""
        return await self._call(
            _fetch_item_aspects,
            category_tree_id=category_tree_id,
        )

    @checked
    async def get_subtree(
        self,
        category_tree_id: StrictStr,
        *,
        category_id: StrictStr,
    ) -> CategorySubtree:
        """Get the part of a category tree under one category."""
        return await self._call(
            _get_category_subtree,
            category_tree_id=category_tree_id,
            category_id=category_id,
        )

    @checked
    async def get_suggestions(
        self,
        category_tree_id: StrictStr,
        *,
        q: StrictStr,
    ) -> CategorySuggestionResponse:
        """Suggest leaf categories for a search phrase."""
        return await self._call(
            _get_category_suggestions,
            category_tree_id=category_tree_id,
            q=q,
        )

    @checked
    async def get(
        self,
        category_tree_id: StrictStr,
    ) -> CategoryTree:
        """Get a whole category tree."""
        return await self._call(
            _get_category_tree,
            category_tree_id=category_tree_id,
        )

    @checked
    async def get_compatibility_properties(
        self,
        category_tree_id: StrictStr,
        *,
        category_id: StrictStr,
    ) -> GetCompatibilityMetadataResponse:
        """List the parts compatibility properties of a category."""
        return await self._call(
            _get_compatibility_properties,
            category_tree_id=category_tree_id,
            category_id=category_id,
        )

    @checked
    async def get_compatibility_property_values(
        self,
        category_tree_id: StrictStr,
        *,
        compatibility_property: StrictStr,
        category_id: StrictStr,
        filter: Optional[StrictStr] = None,
    ) -> GetCompatibilityPropertyValuesResponse:
        """List the values of one parts compatibility property."""
        return await self._call(
            _get_compatibility_property_values,
            category_tree_id=category_tree_id,
            compatibility_property=compatibility_property,
            category_id=category_id,
            filter=filter,
        )

    @checked
    async def get_default_id(
        self,
        *,
        marketplace_id: StrictStr,
    ) -> BaseCategoryTree:
        """Get the ID of a marketplace's default category tree."""
        return await self._call(
            _get_default_category_tree_id,
            marketplace_id=marketplace_id,
        )

    @checked
    async def get_expired_categories(
        self,
        category_tree_id: StrictStr,
    ) -> ExpiredCategories:
        """List the leaf categories that expired and what replaced them."""
        return await self._call(
            _get_expired_categories,
            category_tree_id=category_tree_id,
        )

    @checked
    async def get_item_aspects(
        self,
        category_tree_id: StrictStr,
        *,
        category_id: StrictStr,
    ) -> AspectMetadata:
        """List the item aspects of one leaf category."""
        return await self._call(
            _get_item_aspects_for_category,
            category_tree_id=category_tree_id,
            category_id=category_id,
        )
