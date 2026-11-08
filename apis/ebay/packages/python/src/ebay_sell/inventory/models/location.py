# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.address import Address
from ebay_sell.inventory.models.geo_coordinates import GeoCoordinates
from ebay_sell._runtime import ApiModel


class Location(ApiModel):
    """Location model."""

    address: Optional[Address] = None
    geo_coordinates: Optional[GeoCoordinates] = Field(default=None, alias="geoCoordinates")
    location_id: Optional[StrictStr] = Field(default=None, alias="locationId")
