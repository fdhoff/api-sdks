# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.payment_policy import PaymentPolicy
from ebay_sell._runtime import ApiModel


class PaymentPolicyResponse(ApiModel):
    """PaymentPolicyResponse model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    payment_policies: Optional[List[PaymentPolicy]] = Field(default=None, alias="paymentPolicies")
    prev: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
