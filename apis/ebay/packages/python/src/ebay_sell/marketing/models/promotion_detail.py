# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class PromotionDetail(ApiModel):
    """PromotionDetail model."""

    coupon_code: Optional[StrictStr] = Field(default=None, alias="couponCode")
    description: Optional[StrictStr] = None
    end_date: Optional[StrictStr] = Field(default=None, alias="endDate")
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    name: Optional[StrictStr] = None
    priority: Optional[StrictStr] = None
    promotion_href: Optional[StrictStr] = Field(default=None, alias="promotionHref")
    promotion_id: Optional[StrictStr] = Field(default=None, alias="promotionId")
    promotion_image_url: Optional[StrictStr] = Field(default=None, alias="promotionImageUrl")
    promotion_status: Optional[StrictStr] = Field(default=None, alias="promotionStatus")
    promotion_type: Optional[StrictStr] = Field(default=None, alias="promotionType")
    start_date: Optional[StrictStr] = Field(default=None, alias="startDate")
