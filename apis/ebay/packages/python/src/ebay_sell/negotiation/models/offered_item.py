# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.negotiation.models.amount import Amount
from ebay_sell._runtime import ApiModel


class OfferedItem(ApiModel):
    """OfferedItem model."""

    discount_percentage: Optional[StrictStr] = Field(default=None, alias="discountPercentage")
    listing_id: Optional[StrictStr] = Field(default=None, alias="listingId")
    price: Optional[Amount] = None
    quantity: Optional[StrictInt] = None
