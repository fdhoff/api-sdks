# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.targeting_items import TargetingItems
from ebay_sell._runtime import ApiModel


class TargetedAdsPagedCollection(ApiModel):
    """TargetedAdsPagedCollection model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    suggested_items: Optional[List[TargetingItems]] = Field(default=None, alias="suggestedItems")
    total: Optional[StrictInt] = None
