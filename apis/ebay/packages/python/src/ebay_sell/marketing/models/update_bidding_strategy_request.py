# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.bid_preference import BidPreference
from ebay_sell._runtime import ApiModel


class UpdateBiddingStrategyRequest(ApiModel):
    """UpdateBiddingStrategyRequest model."""

    bidding_strategy: Optional[StrictStr] = Field(default=None, alias="biddingStrategy")
    bid_preferences: Optional[List[BidPreference]] = Field(default=None, alias="bidPreferences")
