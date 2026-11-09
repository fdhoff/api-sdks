# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.appeal_details import AppealDetails
from ebay_sell.post_order.models.provisional_refund import ProvisionalRefund
from ebay_sell.post_order.models.refund_amounts import RefundAmounts
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class InquiryDetails(ApiModel):
    """InquiryDetails model."""

    appeal_details: Optional[AppealDetails] = Field(default=None, alias="appealDetails")
    creation_date: Optional[Timestamp] = Field(default=None, alias="creationDate")
    escalation_date: Optional[Timestamp] = Field(default=None, alias="escalationDate")
    expiration_date: Optional[Timestamp] = Field(default=None, alias="expirationDate")
    last_buyer_resp_date: Optional[Timestamp] = Field(default=None, alias="lastBuyerRespDate")
    provisional_refund: Optional[ProvisionalRefund] = Field(default=None, alias="provisionalRefund")
    refund_amounts: Optional[RefundAmounts] = Field(default=None, alias="refundAmounts")
    refund_charge_amount: Optional[Amount] = Field(default=None, alias="refundChargeAmount")
    refund_deadline_date: Optional[Timestamp] = Field(default=None, alias="refundDeadlineDate")
    total_amount: Optional[Amount] = Field(default=None, alias="totalAmount")
