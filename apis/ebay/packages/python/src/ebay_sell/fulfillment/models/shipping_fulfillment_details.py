# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.line_item_reference import LineItemReference
from ebay_sell._runtime import ApiModel


class ShippingFulfillmentDetails(ApiModel):
    """ShippingFulfillmentDetails model."""

    line_items: Optional[List[LineItemReference]] = Field(default=None, alias="lineItems")
    shipped_date: Optional[StrictStr] = Field(default=None, alias="shippedDate")
    shipping_carrier_code: Optional[StrictStr] = Field(default=None, alias="shippingCarrierCode")
    tracking_number: Optional[StrictStr] = Field(default=None, alias="trackingNumber")
