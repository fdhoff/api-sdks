# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell._runtime import ApiModel


class OrderSummary(ApiModel):
    """OrderSummary model."""

    discounts: Optional[Amount] = None
    item_subtotal: Optional[Amount] = Field(default=None, alias="itemSubtotal")
    seller_collected_taxes: Optional[Amount] = Field(default=None, alias="sellerCollectedTaxes")
    shipping_and_handling_costs: Optional[Amount] = Field(default=None, alias="shippingAndHandlingCosts")
