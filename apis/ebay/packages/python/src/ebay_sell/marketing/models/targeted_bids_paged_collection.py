# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.suggested_bids import SuggestedBids
from ebay_sell._runtime import ApiModel


class TargetedBidsPagedCollection(ApiModel):
    """TargetedBidsPagedCollection model."""

    suggested_bids: Optional[List[SuggestedBids]] = Field(default=None, alias="suggestedBids")
