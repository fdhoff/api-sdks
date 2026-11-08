# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.amount import Amount
from ebay_sell.marketing.models.coupon_configuration import CouponConfiguration
from ebay_sell.marketing.models.discount_rule import DiscountRule
from ebay_sell.marketing.models.inventory_criterion import InventoryCriterion
from ebay_sell._runtime import ApiModel


class ItemPromotionResponse(ApiModel):
    """ItemPromotionResponse model."""

    apply_discount_to_single_item_only: Optional[StrictBool] = Field(
        default=None, alias="applyDiscountToSingleItemOnly"
    )
    budget: Optional[Amount] = None
    coupon_configuration: Optional[CouponConfiguration] = Field(default=None, alias="couponConfiguration")
    description: Optional[StrictStr] = None
    discount_rules: Optional[List[DiscountRule]] = Field(default=None, alias="discountRules")
    end_date: Optional[StrictStr] = Field(default=None, alias="endDate")
    inventory_criterion: Optional[InventoryCriterion] = Field(default=None, alias="inventoryCriterion")
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    name: Optional[StrictStr] = None
    priority: Optional[StrictStr] = None
    promotion_id: Optional[StrictStr] = Field(default=None, alias="promotionId")
    promotion_image_url: Optional[StrictStr] = Field(default=None, alias="promotionImageUrl")
    promotion_status: Optional[StrictStr] = Field(default=None, alias="promotionStatus")
    promotion_type: Optional[StrictStr] = Field(default=None, alias="promotionType")
    start_date: Optional[StrictStr] = Field(default=None, alias="startDate")
