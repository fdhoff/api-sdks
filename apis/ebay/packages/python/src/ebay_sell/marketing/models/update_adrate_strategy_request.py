# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.dynamic_ad_rate_preference import DynamicAdRatePreference
from ebay_sell._runtime import ApiModel


class UpdateAdrateStrategyRequest(ApiModel):
    """UpdateAdrateStrategyRequest model."""

    ad_rate_strategy: Optional[StrictStr] = Field(default=None, alias="adRateStrategy")
    bid_percentage: Optional[StrictStr] = Field(default=None, alias="bidPercentage")
    dynamic_ad_rate_preferences: Optional[List[DynamicAdRatePreference]] = Field(
        default=None, alias="dynamicAdRatePreferences"
    )
