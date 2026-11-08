# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.inventory_item import InventoryItem
from ebay_sell.marketing.models.selection_rule import SelectionRule
from ebay_sell._runtime import ApiModel


class RuleCriteria(ApiModel):
    """RuleCriteria model."""

    exclude_inventory_items: Optional[List[InventoryItem]] = Field(default=None, alias="excludeInventoryItems")
    exclude_listing_ids: Optional[List[StrictStr]] = Field(default=None, alias="excludeListingIds")
    markup_inventory_items: Optional[List[InventoryItem]] = Field(default=None, alias="markupInventoryItems")
    markup_listing_ids: Optional[List[StrictStr]] = Field(default=None, alias="markupListingIds")
    selection_rules: Optional[List[SelectionRule]] = Field(default=None, alias="selectionRules")
