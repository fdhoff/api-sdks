# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.discount_benefit import DiscountBenefit
from ebay_sell.marketing.models.inventory_criterion import InventoryCriterion
from ebay_sell._runtime import ApiModel


class SelectedInventoryDiscount(ApiModel):
    """SelectedInventoryDiscount model."""

    discount_benefit: Optional[DiscountBenefit] = Field(default=None, alias="discountBenefit")
    discount_id: Optional[StrictStr] = Field(default=None, alias="discountId")
    inventory_criterion: Optional[InventoryCriterion] = Field(default=None, alias="inventoryCriterion")
    rule_order: Optional[StrictInt] = Field(default=None, alias="ruleOrder")
