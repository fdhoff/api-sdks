# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.campaign_budget import CampaignBudget
from ebay_sell._runtime import ApiModel


class BudgetRecommendationResponse(ApiModel):
    """BudgetRecommendationResponse model."""

    budget: Optional[CampaignBudget] = None
    campaign_id: Optional[StrictStr] = Field(default=None, alias="campaignId")
    channels: Optional[List[StrictStr]] = None
