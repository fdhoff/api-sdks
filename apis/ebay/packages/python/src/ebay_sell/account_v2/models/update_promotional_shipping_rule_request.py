# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account_v2.models.promotional_shipping_rule_type import PromotionalShippingRuleType
from ebay_sell._runtime import ApiModel


class UpdatePromotionalShippingRuleRequest(ApiModel):
    """UpdatePromotionalShippingRuleRequest model."""

    combined_duration: Optional[StrictStr] = Field(default=None, alias="combinedDuration")
    promotional_shipping_rule: Optional[PromotionalShippingRuleType] = Field(
        default=None, alias="promotionalShippingRule"
    )
