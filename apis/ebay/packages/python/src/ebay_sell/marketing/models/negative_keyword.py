# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class NegativeKeyword(ApiModel):
    """NegativeKeyword model."""

    ad_group_id: Optional[StrictStr] = Field(default=None, alias="adGroupId")
    campaign_id: Optional[StrictStr] = Field(default=None, alias="campaignId")
    negative_keyword_id: Optional[StrictStr] = Field(default=None, alias="negativeKeywordId")
    negative_keyword_match_type: Optional[StrictStr] = Field(default=None, alias="negativeKeywordMatchType")
    negative_keyword_status: Optional[StrictStr] = Field(default=None, alias="negativeKeywordStatus")
    negative_keyword_text: Optional[StrictStr] = Field(default=None, alias="negativeKeywordText")
