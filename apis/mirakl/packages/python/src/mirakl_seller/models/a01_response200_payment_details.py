# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.a01_response200_payment_details_sub_balances import A01Response200PaymentDetailsSubBalances
from mirakl_seller._runtime import ApiModel


class A01Response200PaymentDetails(ApiModel):
    """A01Response200PaymentDetails model."""

    paid_balance: float
    payable_balance: float
    pending_balance: float
    reserve_balance: Optional[float] = None
    reserve_target: Optional[float] = None
    sub_balances: Optional[List[A01Response200PaymentDetailsSubBalances]] = None
