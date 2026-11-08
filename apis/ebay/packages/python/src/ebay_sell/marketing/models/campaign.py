# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.alert import Alert
from ebay_sell.marketing.models.campaign_budget import CampaignBudget
from ebay_sell.marketing.models.campaign_criterion import CampaignCriterion
from ebay_sell.marketing.models.funding_strategy import FundingStrategy
from ebay_sell._runtime import ApiModel


class Campaign(ApiModel):
    """Campaign model."""

    alerts: Optional[List[Alert]] = None
    budget: Optional[CampaignBudget] = None
    campaign_criterion: Optional[CampaignCriterion] = Field(default=None, alias="campaignCriterion")
    campaign_id: Optional[StrictStr] = Field(default=None, alias="campaignId")
    campaign_name: Optional[StrictStr] = Field(default=None, alias="campaignName")
    campaign_status: Optional[StrictStr] = Field(default=None, alias="campaignStatus")
    campaign_targeting_type: Optional[StrictStr] = Field(default=None, alias="campaignTargetingType")
    channels: Optional[List[StrictStr]] = None
    end_date: Optional[StrictStr] = Field(default=None, alias="endDate")
    funding_strategy: Optional[FundingStrategy] = Field(default=None, alias="fundingStrategy")
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    start_date: Optional[StrictStr] = Field(default=None, alias="startDate")
