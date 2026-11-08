# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.taxonomy.models.ancestor_reference import AncestorReference
from ebay_sell.taxonomy.models.category import Category
from ebay_sell._runtime import ApiModel


class CategorySuggestion(ApiModel):
    """CategorySuggestion model."""

    category: Optional[Category] = None
    category_tree_node_ancestors: Optional[List[AncestorReference]] = Field(
        default=None, alias="categoryTreeNodeAncestors"
    )
    category_tree_node_level: Optional[StrictInt] = Field(default=None, alias="categoryTreeNodeLevel")
    relevancy: Optional[StrictStr] = None
