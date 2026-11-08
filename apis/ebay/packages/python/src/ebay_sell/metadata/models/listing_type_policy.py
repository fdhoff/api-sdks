# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.listing_duration import ListingDuration
from ebay_sell._runtime import ApiModel


class ListingTypePolicy(ApiModel):
    """ListingTypePolicy model."""

    category_id: Optional[StrictStr] = Field(default=None, alias="categoryId")
    category_tree_id: Optional[StrictStr] = Field(default=None, alias="categoryTreeId")
    digital_good_delivery_enabled: Optional[StrictBool] = Field(default=None, alias="digitalGoodDeliveryEnabled")
    listing_durations: Optional[List[ListingDuration]] = Field(default=None, alias="listingDurations")
    pickup_drop_off_enabled: Optional[StrictBool] = Field(default=None, alias="pickupDropOffEnabled")
