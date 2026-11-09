# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ShipmentTrackingDetailType(ApiModel):
    """ShipmentTrackingDetailType model."""

    carrier: Optional[StrictStr] = None
    current_status: Optional[StrictStr] = Field(default=None, alias="currentStatus")
    estimate_from_date: Optional[Timestamp] = Field(default=None, alias="estimateFromDate")
    estimate_to_date: Optional[Timestamp] = Field(default=None, alias="estimateToDate")
    tracking_number: Optional[StrictStr] = Field(default=None, alias="trackingNumber")
    tracking_url: Optional[StrictStr] = Field(default=None, alias="trackingURL")
