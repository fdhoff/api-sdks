# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.inventory_item_with_sku_locale_groupid import InventoryItemWithSkuLocaleGroupid
from ebay_sell._runtime import ApiModel


class InventoryItems(ApiModel):
    """InventoryItems model."""

    href: Optional[StrictStr] = None
    inventory_items: Optional[List[InventoryItemWithSkuLocaleGroupid]] = Field(default=None, alias="inventoryItems")
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    prev: Optional[StrictStr] = None
    size: Optional[StrictInt] = None
    total: Optional[StrictInt] = None
