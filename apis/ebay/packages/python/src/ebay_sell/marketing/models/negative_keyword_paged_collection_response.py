# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.negative_keyword import NegativeKeyword
from ebay_sell._runtime import ApiModel


class NegativeKeywordPagedCollectionResponse(ApiModel):
    """NegativeKeywordPagedCollectionResponse model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    negative_keywords: Optional[List[NegativeKeyword]] = Field(default=None, alias="negativeKeywords")
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
