# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.amount import Amount
from ebay_sell._runtime import ApiModel


class DeliveryCost(ApiModel):
    """DeliveryCost model."""

    discount_amount: Optional[Amount] = Field(default=None, alias="discountAmount")
    handling_cost: Optional[Amount] = Field(default=None, alias="handlingCost")
    import_charges: Optional[Amount] = Field(default=None, alias="importCharges")
    shipping_cost: Optional[Amount] = Field(default=None, alias="shippingCost")
    shipping_intermediation_fee: Optional[Amount] = Field(default=None, alias="shippingIntermediationFee")
