# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.refund_detail_type import RefundDetailType
from ebay_sell.post_order.models.refund_funding_type import RefundFundingType
from ebay_sell.post_order.models.refund_money_movement_status_enum import RefundMoneyMovementStatusEnum
from ebay_sell.post_order.models.return_refund_initiator_enum import ReturnRefundInitiatorEnum
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ActualRefundDetailType(ApiModel):
    """ActualRefundDetailType model."""

    actual_refund: Optional[RefundDetailType] = Field(default=None, alias="actualRefund")
    fundings: Optional[List[RefundFundingType]] = None
    net_charge_amount: Optional[Amount] = Field(default=None, alias="netChargeAmount")
    outstanding_amount: Optional[Amount] = Field(default=None, alias="outstandingAmount")
    refund_initiation_type: Optional[ReturnRefundInitiatorEnum] = Field(default=None, alias="refundInitiationType")
    refund_issued_date: Optional[Timestamp] = Field(default=None, alias="refundIssuedDate")
    refund_status: Optional[RefundMoneyMovementStatusEnum] = Field(default=None, alias="refundStatus")
