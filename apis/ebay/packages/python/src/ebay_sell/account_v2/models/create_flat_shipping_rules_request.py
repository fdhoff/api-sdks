# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account_v2.models.flat_shipping_rule_type import FlatShippingRuleType
from ebay_sell._runtime import ApiModel


class CreateFlatShippingRulesRequest(ApiModel):
    """CreateFlatShippingRulesRequest model."""

    combined_duration: Optional[StrictStr] = Field(default=None, alias="combinedDuration")
    flat_shipping_rule: Optional[FlatShippingRuleType] = Field(default=None, alias="flatShippingRule")
