# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.selected_inventory_discount import SelectedInventoryDiscount
from ebay_sell._runtime import ApiModel


class ItemPriceMarkdown(ApiModel):
    """ItemPriceMarkdown model."""

    apply_free_shipping: Optional[StrictBool] = Field(default=None, alias="applyFreeShipping")
    auto_select_future_inventory: Optional[StrictBool] = Field(default=None, alias="autoSelectFutureInventory")
    block_price_increase_in_item_revision: Optional[StrictBool] = Field(
        default=None, alias="blockPriceIncreaseInItemRevision"
    )
    description: Optional[StrictStr] = None
    end_date: Optional[StrictStr] = Field(default=None, alias="endDate")
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    name: Optional[StrictStr] = None
    priority: Optional[StrictStr] = None
    promotion_image_url: Optional[StrictStr] = Field(default=None, alias="promotionImageUrl")
    promotion_status: Optional[StrictStr] = Field(default=None, alias="promotionStatus")
    selected_inventory_discounts: Optional[List[SelectedInventoryDiscount]] = Field(
        default=None, alias="selectedInventoryDiscounts"
    )
    start_date: Optional[StrictStr] = Field(default=None, alias="startDate")
