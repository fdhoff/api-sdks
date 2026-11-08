# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.proposed_bid import ProposedBid
from ebay_sell._runtime import ApiModel


class SuggestedBids(ApiModel):
    """SuggestedBids model."""

    keyword_text: Optional[StrictStr] = Field(default=None, alias="keywordText")
    match_type: Optional[StrictStr] = Field(default=None, alias="matchType")
    proposed_bid: Optional[ProposedBid] = Field(default=None, alias="proposedBid")
