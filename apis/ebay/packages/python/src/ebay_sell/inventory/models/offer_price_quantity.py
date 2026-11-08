# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.amount import Amount
from ebay_sell._runtime import ApiModel


class OfferPriceQuantity(ApiModel):
    """OfferPriceQuantity model."""

    available_quantity: Optional[StrictInt] = Field(default=None, alias="availableQuantity")
    offer_id: Optional[StrictStr] = Field(default=None, alias="offerId")
    price: Optional[Amount] = None
