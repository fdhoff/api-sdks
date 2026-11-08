# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account_v2.models.amount import Amount
from ebay_sell._runtime import ApiModel


class CalculatedHandlingRuleType(ApiModel):
    """CalculatedHandlingRuleType model."""

    combined_shipping_rule_type: Optional[StrictStr] = Field(default=None, alias="combinedShippingRuleType")
    each_additional_amount: Optional[Amount] = Field(default=None, alias="eachAdditionalAmount")
    each_additional_amount_off_shipping_cost: Optional[Amount] = Field(
        default=None, alias="eachAdditionalAmountOffShippingCost"
    )
    each_additional_percent_off_shipping_cost: Optional[float] = Field(
        default=None, alias="eachAdditionalPercentOffShippingCost"
    )
    order_handling_amount: Optional[Amount] = Field(default=None, alias="orderHandlingAmount")
