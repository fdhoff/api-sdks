# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.bid_preference import BidPreference
from ebay_sell.marketing.models.dynamic_ad_rate_preference import DynamicAdRatePreference
from ebay_sell._runtime import ApiModel


class FundingStrategy(ApiModel):
    """FundingStrategy model."""

    ad_rate_strategy: Optional[StrictStr] = Field(default=None, alias="adRateStrategy")
    bidding_strategy: Optional[StrictStr] = Field(default=None, alias="biddingStrategy")
    bid_percentage: Optional[StrictStr] = Field(default=None, alias="bidPercentage")
    bid_preferences: Optional[List[BidPreference]] = Field(default=None, alias="bidPreferences")
    dynamic_ad_rate_preferences: Optional[List[DynamicAdRatePreference]] = Field(
        default=None, alias="dynamicAdRatePreferences"
    )
    funding_model: Optional[StrictStr] = Field(default=None, alias="fundingModel")
