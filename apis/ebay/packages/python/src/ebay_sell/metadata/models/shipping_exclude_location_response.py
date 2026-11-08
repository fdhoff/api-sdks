# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.shipping_exclude_location import ShippingExcludeLocation
from ebay_sell._runtime import ApiModel


class ShippingExcludeLocationResponse(ApiModel):
    """ShippingExcludeLocationResponse model."""

    exclude_shipping_locations: Optional[List[ShippingExcludeLocation]] = Field(
        default=None, alias="excludeShippingLocations"
    )
