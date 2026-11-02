# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from backmarket_seller._runtime import ApiModel


class PickupInfo(ApiModel):
    """PickupInfo model."""

    confirmation_number: StrictStr = Field(alias="confirmationNumber")
    date_pickup_actual: StrictStr = Field(alias="datePickupActual")
    date_pickup_range_start: StrictStr = Field(alias="datePickupRangeStart")
    date_pickup_range_end: StrictStr = Field(alias="datePickupRangeEnd")
    date_pickup_requested: StrictStr = Field(alias="datePickupRequested")
    is_canceled: StrictBool = Field(alias="isCanceled")
    pickup_id: StrictInt = Field(alias="pickupId")
