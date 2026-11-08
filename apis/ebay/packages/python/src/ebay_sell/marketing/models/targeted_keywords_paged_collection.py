# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.suggested_keywords import SuggestedKeywords
from ebay_sell._runtime import ApiModel


class TargetedKeywordsPagedCollection(ApiModel):
    """TargetedKeywordsPagedCollection model."""

    suggested_keywords: Optional[List[SuggestedKeywords]] = Field(default=None, alias="suggestedKeywords")
