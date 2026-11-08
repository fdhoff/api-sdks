# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.extended_contact import ExtendedContact
from ebay_sell._runtime import ApiModel


class ShippingStep(ApiModel):
    """ShippingStep model."""

    shipping_carrier_code: Optional[StrictStr] = Field(default=None, alias="shippingCarrierCode")
    shipping_service_code: Optional[StrictStr] = Field(default=None, alias="shippingServiceCode")
    ship_to: Optional[ExtendedContact] = Field(default=None, alias="shipTo")
    ship_to_reference_id: Optional[StrictStr] = Field(default=None, alias="shipToReferenceId")
