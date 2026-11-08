# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ListingDetails(ApiModel):
    """ListingDetails model."""

    listing_id: Optional[StrictStr] = Field(default=None, alias="listingId")
    listing_on_hold: Optional[StrictBool] = Field(default=None, alias="listingOnHold")
    listing_status: Optional[StrictStr] = Field(default=None, alias="listingStatus")
    sold_quantity: Optional[StrictInt] = Field(default=None, alias="soldQuantity")
