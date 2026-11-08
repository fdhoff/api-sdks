# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.amount import Amount
from ebay_sell.marketing.models.item_markdown_status import ItemMarkdownStatus
from ebay_sell._runtime import ApiModel


class ListingDetail(ApiModel):
    """ListingDetail model."""

    current_price: Optional[Amount] = Field(default=None, alias="currentPrice")
    free_shipping: Optional[StrictBool] = Field(default=None, alias="freeShipping")
    inventory_reference_id: Optional[StrictStr] = Field(default=None, alias="inventoryReferenceId")
    inventory_reference_type: Optional[StrictStr] = Field(default=None, alias="inventoryReferenceType")
    listing_category_id: Optional[StrictStr] = Field(default=None, alias="listingCategoryId")
    listing_condition: Optional[StrictStr] = Field(default=None, alias="listingCondition")
    listing_condition_id: Optional[StrictStr] = Field(default=None, alias="listingConditionId")
    listing_id: Optional[StrictStr] = Field(default=None, alias="listingId")
    listing_promotion_statuses: Optional[List[ItemMarkdownStatus]] = Field(
        default=None, alias="listingPromotionStatuses"
    )
    quantity: Optional[StrictInt] = None
    store_category_id: Optional[StrictStr] = Field(default=None, alias="storeCategoryId")
    title: Optional[StrictStr] = None
