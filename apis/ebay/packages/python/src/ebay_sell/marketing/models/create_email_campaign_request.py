# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.price_range import PriceRange
from ebay_sell._runtime import ApiModel


class CreateEmailCampaignRequest(ApiModel):
    """CreateEmailCampaignRequest model."""

    audience_codes: Optional[List[StrictStr]] = Field(default=None, alias="audienceCodes")
    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_type: Optional[StrictStr] = Field(default=None, alias="categoryType")
    email_campaign_type: Optional[StrictStr] = Field(default=None, alias="emailCampaignType")
    item_ids: Optional[List[StrictStr]] = Field(default=None, alias="itemIds")
    item_select_mode: Optional[StrictStr] = Field(default=None, alias="itemSelectMode")
    personalized_message: Optional[StrictStr] = Field(default=None, alias="personalizedMessage")
    price_range: Optional[PriceRange] = Field(default=None, alias="priceRange")
    promotion_id: Optional[StrictStr] = Field(default=None, alias="promotionId")
    promotion_select_mode_enum: Optional[StrictStr] = Field(default=None, alias="promotionSelectModeEnum")
    schedule_date: Optional[StrictStr] = Field(default=None, alias="scheduleDate")
    sort: Optional[StrictStr] = None
    subject: Optional[StrictStr] = None
