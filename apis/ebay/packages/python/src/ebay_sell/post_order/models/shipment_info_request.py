# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.text import Text
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ShipmentInfoRequest(ApiModel):
    """ShipmentInfoRequest model."""

    proof_of_shipment_uploaded: Optional[StrictBool] = Field(default=None, alias="proofOfShipmentUploaded")
    seller_comments: Optional[Text] = Field(default=None, alias="sellerComments")
    shipped_with_tracking: Optional[StrictBool] = Field(default=None, alias="shippedWithTracking")
    shipping_carrier_name: Optional[StrictStr] = Field(default=None, alias="shippingCarrierName")
    shipping_date: Optional[Timestamp] = Field(default=None, alias="shippingDate")
    tracking_number: Optional[StrictStr] = Field(default=None, alias="trackingNumber")
