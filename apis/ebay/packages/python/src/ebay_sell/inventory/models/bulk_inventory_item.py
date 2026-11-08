# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.inventory_item_with_sku_locale import InventoryItemWithSkuLocale
from ebay_sell._runtime import ApiModel


class BulkInventoryItem(ApiModel):
    """BulkInventoryItem model."""

    requests: Optional[List[InventoryItemWithSkuLocale]] = None
