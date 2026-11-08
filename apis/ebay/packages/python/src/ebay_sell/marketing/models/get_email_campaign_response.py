# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.campaign_audience import CampaignAudience
from ebay_sell.marketing.models.price_range import PriceRange
from ebay_sell._runtime import ApiModel


class GetEmailCampaignResponse(ApiModel):
    """GetEmailCampaignResponse model."""

    audiences: Optional[List[CampaignAudience]] = None
    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_type: Optional[StrictStr] = Field(default=None, alias="categoryType")
    creation_date: Optional[StrictStr] = Field(default=None, alias="creationDate")
    email_campaign_id: Optional[StrictStr] = Field(default=None, alias="emailCampaignId")
    email_campaign_status: Optional[StrictStr] = Field(default=None, alias="emailCampaignStatus")
    email_campaign_type: Optional[StrictStr] = Field(default=None, alias="emailCampaignType")
    item_ids: Optional[List[StrictStr]] = Field(default=None, alias="itemIds")
    item_select_mode: Optional[StrictStr] = Field(default=None, alias="itemSelectMode")
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    modification_date: Optional[StrictStr] = Field(default=None, alias="modificationDate")
    personalized_message: Optional[StrictStr] = Field(default=None, alias="personalizedMessage")
    price_range: Optional[PriceRange] = Field(default=None, alias="priceRange")
    promotion_id: Optional[StrictStr] = Field(default=None, alias="promotionId")
    promotion_select_mode: Optional[StrictStr] = Field(default=None, alias="promotionSelectMode")
    schedule_date: Optional[StrictStr] = Field(default=None, alias="scheduleDate")
    schedule_date_type: Optional[StrictStr] = Field(default=None, alias="scheduleDateType")
    sent_date: Optional[StrictStr] = Field(default=None, alias="sentDate")
    sort: Optional[StrictStr] = None
    subject: Optional[StrictStr] = None
