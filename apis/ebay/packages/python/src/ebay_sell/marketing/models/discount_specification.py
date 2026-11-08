# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.amount import Amount
from ebay_sell._runtime import ApiModel


class DiscountSpecification(ApiModel):
    """DiscountSpecification model."""

    for_each_amount: Optional[Amount] = Field(default=None, alias="forEachAmount")
    for_each_quantity: Optional[StrictInt] = Field(default=None, alias="forEachQuantity")
    min_amount: Optional[Amount] = Field(default=None, alias="minAmount")
    min_quantity: Optional[StrictInt] = Field(default=None, alias="minQuantity")
    number_of_discounted_items: Optional[StrictInt] = Field(default=None, alias="numberOfDiscountedItems")
