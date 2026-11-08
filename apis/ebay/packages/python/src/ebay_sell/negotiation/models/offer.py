# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.negotiation.models.offered_item import OfferedItem
from ebay_sell.negotiation.models.time_duration import TimeDuration
from ebay_sell.negotiation.models.user import User
from ebay_sell._runtime import ApiModel


class Offer(ApiModel):
    """Offer model."""

    allow_counter_offer: Optional[StrictBool] = Field(default=None, alias="allowCounterOffer")
    buyer: Optional[User] = None
    creation_date: Optional[StrictStr] = Field(default=None, alias="creationDate")
    initiated_by: Optional[StrictStr] = Field(default=None, alias="initiatedBy")
    last_modified_date: Optional[StrictStr] = Field(default=None, alias="lastModifiedDate")
    message: Optional[StrictStr] = None
    offer_duration: Optional[TimeDuration] = Field(default=None, alias="offerDuration")
    offered_items: Optional[List[OfferedItem]] = Field(default=None, alias="offeredItems")
    offer_id: Optional[StrictStr] = Field(default=None, alias="offerId")
    offer_status: Optional[StrictStr] = Field(default=None, alias="offerStatus")
    offer_type: Optional[StrictStr] = Field(default=None, alias="offerType")
    revision: Optional[StrictStr] = None
