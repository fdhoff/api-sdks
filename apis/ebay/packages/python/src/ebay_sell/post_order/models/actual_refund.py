# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell._runtime import ApiModel


class ActualRefund(ApiModel):
    """ActualRefund model."""

    total_amount: Optional[Amount] = Field(default=None, alias="totalAmount")
    fee_credit_amount: Optional[Amount] = Field(default=None, alias="feeCreditAmount")
    donation_amount: Optional[Amount] = Field(default=None, alias="donationAmount")
