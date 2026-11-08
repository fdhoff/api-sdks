# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.item_basis import ItemBasis
from ebay_sell._runtime import ApiModel


class TargetingItems(ApiModel):
    """TargetingItems model."""

    bases: Optional[List[ItemBasis]] = None
    listing_id: Optional[StrictStr] = Field(default=None, alias="listingId")
