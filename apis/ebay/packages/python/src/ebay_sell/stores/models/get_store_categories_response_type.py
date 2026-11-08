# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.stores.models.store_category_type import StoreCategoryType
from ebay_sell._runtime import ApiModel


class GetStoreCategoriesResponseType(ApiModel):
    """GetStoreCategoriesResponseType model."""

    store_categories: Optional[List[StoreCategoryType]] = Field(default=None, alias="storeCategories")
