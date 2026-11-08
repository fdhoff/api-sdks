# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account_v2.models.amount import Amount
from ebay_sell.account_v2.models.measure_type import MeasureType
from ebay_sell._runtime import ApiModel


class CombinedShippingRule(ApiModel):
    """CombinedShippingRule model."""

    combined_shipping_rule_id: Optional[StrictStr] = Field(default=None, alias="combinedShippingRuleId")
    combined_shipping_rule_name: Optional[StrictStr] = Field(default=None, alias="combinedShippingRuleName")
    each_additional_amount: Optional[Amount] = Field(default=None, alias="eachAdditionalAmount")
    each_additional_amount_off_shipping_cost: Optional[Amount] = Field(
        default=None, alias="eachAdditionalAmountOffShippingCost"
    )
    each_additional_percent_off_shipping_cost: Optional[float] = Field(
        default=None, alias="eachAdditionalPercentOffShippingCost"
    )
    mapped_combined_shipping_rule_id: Optional[StrictStr] = Field(default=None, alias="mappedCombinedShippingRuleId")
    weight_off_total_weight: Optional[MeasureType] = Field(default=None, alias="weightOffTotalWeight")
