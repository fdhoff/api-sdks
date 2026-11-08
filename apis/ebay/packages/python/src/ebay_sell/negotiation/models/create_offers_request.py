# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.negotiation.models.offered_item import OfferedItem
from ebay_sell.negotiation.models.time_duration import TimeDuration
from ebay_sell._runtime import ApiModel


class CreateOffersRequest(ApiModel):
    """CreateOffersRequest model."""

    allow_counter_offer: Optional[StrictBool] = Field(default=None, alias="allowCounterOffer")
    message: Optional[StrictStr] = None
    offer_duration: Optional[TimeDuration] = Field(default=None, alias="offerDuration")
    offered_items: Optional[List[OfferedItem]] = Field(default=None, alias="offeredItems")
