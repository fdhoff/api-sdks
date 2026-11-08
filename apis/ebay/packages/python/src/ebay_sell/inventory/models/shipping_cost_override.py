# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.amount import Amount
from ebay_sell._runtime import ApiModel


class ShippingCostOverride(ApiModel):
    """ShippingCostOverride model."""

    additional_shipping_cost: Optional[Amount] = Field(default=None, alias="additionalShippingCost")
    priority: Optional[StrictInt] = None
    shipping_cost: Optional[Amount] = Field(default=None, alias="shippingCost")
    shipping_service_type: Optional[StrictStr] = Field(default=None, alias="shippingServiceType")
    surcharge: Optional[Amount] = None
