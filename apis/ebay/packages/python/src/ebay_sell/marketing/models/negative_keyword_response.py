# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.error import Error
from ebay_sell._runtime import ApiModel


class NegativeKeywordResponse(ApiModel):
    """NegativeKeywordResponse model."""

    ad_group_id: Optional[StrictStr] = Field(default=None, alias="adGroupId")
    campaign_id: Optional[StrictStr] = Field(default=None, alias="campaignId")
    errors: Optional[List[Error]] = None
    href: Optional[StrictStr] = None
    negative_keyword_id: Optional[StrictStr] = Field(default=None, alias="negativeKeywordId")
    negative_keyword_match_type: Optional[StrictStr] = Field(default=None, alias="negativeKeywordMatchType")
    negative_keyword_text: Optional[StrictStr] = Field(default=None, alias="negativeKeywordText")
    status_code: Optional[StrictInt] = Field(default=None, alias="statusCode")
