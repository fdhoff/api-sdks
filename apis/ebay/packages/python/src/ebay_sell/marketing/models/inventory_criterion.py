# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.inventory_item import InventoryItem
from ebay_sell.marketing.models.rule_criteria import RuleCriteria
from ebay_sell._runtime import ApiModel


class InventoryCriterion(ApiModel):
    """InventoryCriterion model."""

    inventory_criterion_type: Optional[StrictStr] = Field(default=None, alias="inventoryCriterionType")
    inventory_items: Optional[List[InventoryItem]] = Field(default=None, alias="inventoryItems")
    listing_ids: Optional[List[StrictStr]] = Field(default=None, alias="listingIds")
    rule_criteria: Optional[RuleCriteria] = Field(default=None, alias="ruleCriteria")
