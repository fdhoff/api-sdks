# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class AncestorReference(ApiModel):
    """AncestorReference model."""

    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_name: Optional[StrictStr] = Field(default=None, alias="categoryName")
    category_subtree_node_href: Optional[StrictStr] = Field(default=None, alias="categorySubtreeNodeHref")
    category_tree_node_level: Optional[StrictInt] = Field(default=None, alias="categoryTreeNodeLevel")
