# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.funding_strategy import FundingStrategy
from ebay_sell._runtime import ApiModel


class CloneCampaignRequest(ApiModel):
    """CloneCampaignRequest model."""

    campaign_name: Optional[StrictStr] = Field(default=None, alias="campaignName")
    end_date: Optional[StrictStr] = Field(default=None, alias="endDate")
    funding_strategy: Optional[FundingStrategy] = Field(default=None, alias="fundingStrategy")
    start_date: Optional[StrictStr] = Field(default=None, alias="startDate")
