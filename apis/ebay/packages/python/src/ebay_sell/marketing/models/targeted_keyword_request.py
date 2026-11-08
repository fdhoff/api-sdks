# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class TargetedKeywordRequest(ApiModel):
    """TargetedKeywordRequest model."""

    additional_info: Optional[List[StrictStr]] = Field(default=None, alias="additionalInfo")
    exclusions: Optional[List[StrictStr]] = None
    listing_ids: Optional[List[StrictStr]] = Field(default=None, alias="listingIds")
    match_type: Optional[StrictStr] = Field(default=None, alias="matchType")
