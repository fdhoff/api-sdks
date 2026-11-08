# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.amount import Amount
from ebay_sell.account.models.payment_method import PaymentMethod
from ebay_sell.account.models.time_duration import TimeDuration
from ebay_sell._runtime import ApiModel


class Deposit(ApiModel):
    """Deposit model."""

    amount: Optional[Amount] = None
    due_in: Optional[TimeDuration] = Field(default=None, alias="dueIn")
    payment_methods: Optional[List[PaymentMethod]] = Field(default=None, alias="paymentMethods")
