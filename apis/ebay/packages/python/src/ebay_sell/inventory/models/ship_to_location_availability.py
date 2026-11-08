# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.availability_distribution import AvailabilityDistribution
from ebay_sell._runtime import ApiModel


class ShipToLocationAvailability(ApiModel):
    """ShipToLocationAvailability model."""

    availability_distributions: Optional[List[AvailabilityDistribution]] = Field(
        default=None, alias="availabilityDistributions"
    )
    quantity: Optional[StrictInt] = None
