# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.amount import Amount
from ebay_sell._runtime import ApiModel


class PricingSummary(ApiModel):
    """PricingSummary model."""

    auction_reserve_price: Optional[Amount] = Field(default=None, alias="auctionReservePrice")
    auction_start_price: Optional[Amount] = Field(default=None, alias="auctionStartPrice")
    minimum_advertised_price: Optional[Amount] = Field(default=None, alias="minimumAdvertisedPrice")
    originally_sold_for_retail_price_on: Optional[StrictStr] = Field(
        default=None, alias="originallySoldForRetailPriceOn"
    )
    original_retail_price: Optional[Amount] = Field(default=None, alias="originalRetailPrice")
    price: Optional[Amount] = None
    pricing_visibility: Optional[StrictStr] = Field(default=None, alias="pricingVisibility")
