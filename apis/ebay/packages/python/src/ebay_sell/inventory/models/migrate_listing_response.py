# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.error import Error
from ebay_sell.inventory.models.inventory_item_listing import InventoryItemListing
from ebay_sell._runtime import ApiModel


class MigrateListingResponse(ApiModel):
    """MigrateListingResponse model."""

    errors: Optional[List[Error]] = None
    inventory_item_group_key: Optional[StrictStr] = Field(default=None, alias="inventoryItemGroupKey")
    inventory_items: Optional[List[InventoryItemListing]] = Field(default=None, alias="inventoryItems")
    listing_id: Optional[StrictStr] = Field(default=None, alias="listingId")
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    status_code: Optional[StrictInt] = Field(default=None, alias="statusCode")
    warnings: Optional[List[Error]] = None
