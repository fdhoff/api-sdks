# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.shipping_location import ShippingLocation
from ebay_sell._runtime import ApiModel


class ShippingLocationResponse(ApiModel):
    """ShippingLocationResponse model."""

    shipping_locations: Optional[List[ShippingLocation]] = Field(default=None, alias="shippingLocations")
