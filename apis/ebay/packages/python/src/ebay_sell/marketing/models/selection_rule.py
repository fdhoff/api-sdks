# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.amount import Amount
from ebay_sell._runtime import ApiModel


class SelectionRule(ApiModel):
    """SelectionRule model."""

    brands: Optional[List[StrictStr]] = None
    category_ids: Optional[List[StrictStr]] = Field(default=None, alias="categoryIds")
    category_scope: Optional[StrictStr] = Field(default=None, alias="categoryScope")
    listing_condition_ids: Optional[List[StrictStr]] = Field(default=None, alias="listingConditionIds")
    max_price: Optional[Amount] = Field(default=None, alias="maxPrice")
    min_price: Optional[Amount] = Field(default=None, alias="minPrice")
