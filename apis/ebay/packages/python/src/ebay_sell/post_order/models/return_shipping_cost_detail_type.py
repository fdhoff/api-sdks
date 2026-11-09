# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.itemized_return_shipping_cost_type import ItemizedReturnShippingCostType
from ebay_sell._runtime import ApiModel


class ReturnShippingCostDetailType(ApiModel):
    """ReturnShippingCostDetailType model."""

    itemized_return_shipping_cost: Optional[List[ItemizedReturnShippingCostType]] = Field(
        default=None, alias="itemizedReturnShippingCost"
    )
    total_amount: Optional[Amount] = Field(default=None, alias="totalAmount")
