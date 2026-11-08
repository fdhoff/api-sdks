# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account_v2.models.amount import Amount
from ebay_sell._runtime import ApiModel


class PromotionalShippingRuleType(ApiModel):
    """PromotionalShippingRuleType model."""

    combined_shipping_rule_type: Optional[StrictStr] = Field(default=None, alias="combinedShippingRuleType")
    item_count: Optional[StrictInt] = Field(default=None, alias="itemCount")
    order_amount: Optional[Amount] = Field(default=None, alias="orderAmount")
    shipping_cost: Optional[Amount] = Field(default=None, alias="shippingCost")
