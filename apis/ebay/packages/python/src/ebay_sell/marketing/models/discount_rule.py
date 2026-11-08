# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.amount import Amount
from ebay_sell.marketing.models.discount_benefit import DiscountBenefit
from ebay_sell.marketing.models.discount_specification import DiscountSpecification
from ebay_sell._runtime import ApiModel


class DiscountRule(ApiModel):
    """DiscountRule model."""

    discount_benefit: Optional[DiscountBenefit] = Field(default=None, alias="discountBenefit")
    discount_specification: Optional[DiscountSpecification] = Field(default=None, alias="discountSpecification")
    max_discount_amount: Optional[Amount] = Field(default=None, alias="maxDiscountAmount")
    rule_order: Optional[StrictInt] = Field(default=None, alias="ruleOrder")
