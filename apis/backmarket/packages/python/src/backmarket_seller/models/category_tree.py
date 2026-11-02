# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from backmarket_seller.models.category_tree_attributes_inner import CategoryTreeAttributesInner
from backmarket_seller._runtime import ApiModel


class CategoryTree(ApiModel):
    """CategoryTree model."""

    category_id: StrictInt
    category_name: StrictStr
    marketplace_category_id: StrictInt
    is_leaf: StrictBool
    attributes: List[CategoryTreeAttributesInner]
    childrens: List[CategoryTree]


CategoryTree.model_rebuild(raise_errors=False)
