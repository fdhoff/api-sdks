# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.refund_amounts import RefundAmounts
from ebay_sell.post_order.models.refund_type import RefundType
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class CaseDetails(ApiModel):
    """CaseDetails model."""

    buyer_final_accept_resolution: Optional[StrictStr] = Field(default=None, alias="buyerFinalAcceptResolution")
    buyer_init_expect_resolution: Optional[StrictStr] = Field(default=None, alias="buyerInitExpectResolution")
    creation_date: Optional[Timestamp] = Field(default=None, alias="creationDate")
    escalation_date: Optional[Timestamp] = Field(default=None, alias="escalationDate")
    expiration_date: Optional[Timestamp] = Field(default=None, alias="expirationDate")
    last_buyer_resp_date: Optional[Timestamp] = Field(default=None, alias="lastBuyerRespDate")
    last_seller_resp_date: Optional[Timestamp] = Field(default=None, alias="lastSellerRespDate")
    paypal_paid: Optional[StrictBool] = Field(default=None, alias="paypalPaid")
    refund_amounts: Optional[RefundAmounts] = Field(default=None, alias="refundAmounts")
    refund_charge_amount: Optional[Amount] = Field(default=None, alias="refundChargeAmount")
    refund_deadline_date: Optional[Timestamp] = Field(default=None, alias="refundDeadlineDate")
    refund_type: Optional[RefundType] = Field(default=None, alias="refundType")
