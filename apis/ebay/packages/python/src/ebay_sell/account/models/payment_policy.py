# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.category_type import CategoryType
from ebay_sell.account.models.deposit import Deposit
from ebay_sell.account.models.payment_method import PaymentMethod
from ebay_sell.account.models.time_duration import TimeDuration
from ebay_sell._runtime import ApiModel


class PaymentPolicy(ApiModel):
    """PaymentPolicy model."""

    category_types: Optional[List[CategoryType]] = Field(default=None, alias="categoryTypes")
    deposit: Optional[Deposit] = None
    description: Optional[StrictStr] = None
    full_payment_due_in: Optional[TimeDuration] = Field(default=None, alias="fullPaymentDueIn")
    immediate_pay: Optional[StrictBool] = Field(default=None, alias="immediatePay")
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    name: Optional[StrictStr] = None
    payment_instructions: Optional[StrictStr] = Field(default=None, alias="paymentInstructions")
    payment_methods: Optional[List[PaymentMethod]] = Field(default=None, alias="paymentMethods")
    payment_policy_id: Optional[StrictStr] = Field(default=None, alias="paymentPolicyId")
