# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class StoreCategoryType(ApiModel):
    """StoreCategoryType model."""

    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_name: Optional[StrictStr] = Field(default=None, alias="categoryName")
    children_categories: Optional[List[StoreCategoryType]] = Field(default=None, alias="childrenCategories")
    level: Optional[StrictInt] = None
    order: Optional[StrictInt] = None


StoreCategoryType.model_rebuild(raise_errors=False)
