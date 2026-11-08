# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.varies_by import VariesBy
from ebay_sell._runtime import ApiModel


class InventoryItemGroup(ApiModel):
    """InventoryItemGroup model."""

    aspects: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    image_urls: Optional[List[StrictStr]] = Field(default=None, alias="imageUrls")
    inventory_item_group_key: Optional[StrictStr] = Field(default=None, alias="inventoryItemGroupKey")
    subtitle: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    variant_skus: Optional[List[StrictStr]] = Field(default=None, alias="variantSKUs")
    varies_by: Optional[VariesBy] = Field(default=None, alias="variesBy")
    video_ids: Optional[List[StrictStr]] = Field(default=None, alias="videoIds")
