# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.time_duration import TimeDuration
from ebay_sell._runtime import ApiModel


class AvailabilityDistribution(ApiModel):
    """AvailabilityDistribution model."""

    fulfillment_time: Optional[TimeDuration] = Field(default=None, alias="fulfillmentTime")
    merchant_location_key: Optional[StrictStr] = Field(default=None, alias="merchantLocationKey")
    quantity: Optional[StrictInt] = None
