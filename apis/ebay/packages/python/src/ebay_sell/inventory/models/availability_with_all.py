# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.pickup_at_location_availability import PickupAtLocationAvailability
from ebay_sell.inventory.models.ship_to_location_availability_with_all import ShipToLocationAvailabilityWithAll
from ebay_sell._runtime import ApiModel


class AvailabilityWithAll(ApiModel):
    """AvailabilityWithAll model."""

    pickup_at_location_availability: Optional[List[PickupAtLocationAvailability]] = Field(
        default=None, alias="pickupAtLocationAvailability"
    )
    ship_to_location_availability: Optional[ShipToLocationAvailabilityWithAll] = Field(
        default=None, alias="shipToLocationAvailability"
    )
