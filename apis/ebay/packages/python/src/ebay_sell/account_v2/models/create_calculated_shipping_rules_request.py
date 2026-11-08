# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account_v2.models.calculated_handling_rule_type import CalculatedHandlingRuleType
from ebay_sell.account_v2.models.calculated_shipping_rule_type import CalculatedShippingRuleType
from ebay_sell._runtime import ApiModel


class CreateCalculatedShippingRulesRequest(ApiModel):
    """CreateCalculatedShippingRulesRequest model."""

    calculated_handling_rule: Optional[CalculatedHandlingRuleType] = Field(default=None, alias="calculatedHandlingRule")
    calculated_shipping_rule: Optional[CalculatedShippingRuleType] = Field(default=None, alias="calculatedShippingRule")
    combined_duration: Optional[StrictStr] = Field(default=None, alias="combinedDuration")
