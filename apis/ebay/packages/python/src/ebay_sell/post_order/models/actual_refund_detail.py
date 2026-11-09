# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.actual_refund import ActualRefund
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.refund_funding_type import RefundFundingType
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ActualRefundDetail(ApiModel):
    """ActualRefundDetail model."""

    actual_refund: Optional[ActualRefund] = Field(default=None, alias="actualRefund")
    net_charge_amount: Optional[Amount] = Field(default=None, alias="netChargeAmount")
    refund_issued_date: Optional[Timestamp] = Field(default=None, alias="refundIssuedDate")
    refund_status: Optional[StrictStr] = Field(default=None, alias="refundStatus")
    outstanding_amount: Optional[Amount] = Field(default=None, alias="outstandingAmount")
    fundings: Optional[List[RefundFundingType]] = None
