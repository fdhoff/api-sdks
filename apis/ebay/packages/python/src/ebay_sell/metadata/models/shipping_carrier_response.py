# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.shipping_carrier import ShippingCarrier
from ebay_sell._runtime import ApiModel


class ShippingCarrierResponse(ApiModel):
    """ShippingCarrierResponse model."""

    shipping_carriers: Optional[List[ShippingCarrier]] = Field(default=None, alias="shippingCarriers")
