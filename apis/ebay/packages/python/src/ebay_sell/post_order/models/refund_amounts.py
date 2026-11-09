# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell._runtime import ApiModel


class RefundAmounts(ApiModel):
    """RefundAmounts model."""

    buyer_final_accept_refund_amt: Optional[Amount] = Field(default=None, alias="buyerFinalAcceptRefundAmt")
    buyer_init_expect_refund_amt: Optional[Amount] = Field(default=None, alias="buyerInitExpectRefundAmt")
    donation_amount: Optional[Amount] = Field(default=None, alias="donationAmount")
    fee_credit_amount: Optional[Amount] = Field(default=None, alias="feeCreditAmount")
    international_refund_amount: Optional[Amount] = Field(default=None, alias="internationalRefundAmount")
    refund_amount: Optional[Amount] = Field(default=None, alias="refundAmount")
