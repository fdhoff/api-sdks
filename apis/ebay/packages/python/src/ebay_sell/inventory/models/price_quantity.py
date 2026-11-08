# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.offer_price_quantity import OfferPriceQuantity
from ebay_sell.inventory.models.ship_to_location_availability import ShipToLocationAvailability
from ebay_sell._runtime import ApiModel


class PriceQuantity(ApiModel):
    """PriceQuantity model."""

    offers: Optional[List[OfferPriceQuantity]] = None
    ship_to_location_availability: Optional[ShipToLocationAvailability] = Field(
        default=None, alias="shipToLocationAvailability"
    )
    sku: Optional[StrictStr] = None
