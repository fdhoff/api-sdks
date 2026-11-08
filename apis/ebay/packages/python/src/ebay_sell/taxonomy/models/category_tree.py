# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.taxonomy.models.category_tree_node import CategoryTreeNode
from ebay_sell._runtime import ApiModel


class CategoryTree(ApiModel):
    """CategoryTree model."""

    applicable_marketplace_ids: Optional[List[StrictStr]] = Field(default=None, alias="applicableMarketplaceIds")
    category_tree_id: Optional[StrictStr] = Field(default=None, alias="categoryTreeId")
    category_tree_version: Optional[StrictStr] = Field(default=None, alias="categoryTreeVersion")
    root_category_node: Optional[CategoryTreeNode] = Field(default=None, alias="rootCategoryNode")
