# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.amount import Amount
from ebay_sell._runtime import ApiModel


class PricingSummary(ApiModel):
    """PricingSummary model."""

    adjustment: Optional[Amount] = None
    delivery_cost: Optional[Amount] = Field(default=None, alias="deliveryCost")
    delivery_discount: Optional[Amount] = Field(default=None, alias="deliveryDiscount")
    fee: Optional[Amount] = None
    price_discount: Optional[Amount] = Field(default=None, alias="priceDiscount")
    price_subtotal: Optional[Amount] = Field(default=None, alias="priceSubtotal")
    tax: Optional[Amount] = None
    total: Optional[Amount] = None
