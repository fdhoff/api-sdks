# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class TrackingInfo(ApiModel):
    """TrackingInfo model."""

    shipment_tracking_number: Optional[StrictStr] = Field(default=None, alias="shipmentTrackingNumber")
    shipping_carrier_code: Optional[StrictStr] = Field(default=None, alias="shippingCarrierCode")
