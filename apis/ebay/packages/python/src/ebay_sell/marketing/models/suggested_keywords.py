# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.additional_info import AdditionalInfo
from ebay_sell._runtime import ApiModel


class SuggestedKeywords(ApiModel):
    """SuggestedKeywords model."""

    additional_info: Optional[List[AdditionalInfo]] = Field(default=None, alias="additionalInfo")
    keyword_text: Optional[StrictStr] = Field(default=None, alias="keywordText")
    match_type: Optional[StrictStr] = Field(default=None, alias="matchType")
