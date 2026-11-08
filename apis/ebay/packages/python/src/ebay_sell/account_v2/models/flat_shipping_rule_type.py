# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account_v2.models.combined_shipping_rule import CombinedShippingRule
from ebay_sell._runtime import ApiModel


class FlatShippingRuleType(ApiModel):
    """FlatShippingRuleType model."""

    combined_shipping_rules: Optional[List[CombinedShippingRule]] = Field(default=None, alias="combinedShippingRules")
    combined_shipping_rule_type: Optional[StrictStr] = Field(default=None, alias="combinedShippingRuleType")
