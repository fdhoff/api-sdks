# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.taxonomy.models.category import Category
from ebay_sell._runtime import ApiModel


class CategoryTreeNode(ApiModel):
    """CategoryTreeNode model."""

    category: Optional[Category] = None
    category_tree_node_level: Optional[StrictInt] = Field(default=None, alias="categoryTreeNodeLevel")
    child_category_tree_nodes: Optional[List[CategoryTreeNode]] = Field(default=None, alias="childCategoryTreeNodes")
    leaf_category_tree_node: Optional[StrictBool] = Field(default=None, alias="leafCategoryTreeNode")
    parent_category_tree_node_href: Optional[StrictStr] = Field(default=None, alias="parentCategoryTreeNodeHref")


CategoryTreeNode.model_rebuild(raise_errors=False)
