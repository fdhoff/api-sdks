# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.address import Address
from ebay_sell.fulfillment.models.appointment_details import AppointmentDetails
from ebay_sell.fulfillment.models.pickup_step import PickupStep
from ebay_sell.fulfillment.models.shipping_step import ShippingStep
from ebay_sell._runtime import ApiModel


class FulfillmentStartInstruction(ApiModel):
    """FulfillmentStartInstruction model."""

    appointment: Optional[AppointmentDetails] = None
    ebay_supported_fulfillment: Optional[StrictBool] = Field(default=None, alias="ebaySupportedFulfillment")
    final_destination_address: Optional[Address] = Field(default=None, alias="finalDestinationAddress")
    fulfillment_instructions_type: Optional[StrictStr] = Field(default=None, alias="fulfillmentInstructionsType")
    max_estimated_delivery_date: Optional[StrictStr] = Field(default=None, alias="maxEstimatedDeliveryDate")
    min_estimated_delivery_date: Optional[StrictStr] = Field(default=None, alias="minEstimatedDeliveryDate")
    pickup_step: Optional[PickupStep] = Field(default=None, alias="pickupStep")
    shipping_step: Optional[ShippingStep] = Field(default=None, alias="shippingStep")
