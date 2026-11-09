# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.partial_order_type_enum import PartialOrderTypeEnum
from ebay_sell.post_order.models.party_enum import PartyEnum
from ebay_sell.post_order.models.payment_status_enum import PaymentStatusEnum
from ebay_sell.post_order.models.payout_recoup_info import PayoutRecoupInfo
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class CancelSummary(ApiModel):
    """CancelSummary model."""

    buyer_login_name: Optional[StrictStr] = Field(default=None, alias="buyerLoginName")
    buyer_response_due_date: Optional[Timestamp] = Field(default=None, alias="buyerResponseDueDate")
    cancel_close_date: Optional[Timestamp] = Field(default=None, alias="cancelCloseDate")
    cancel_close_reason: Optional[StrictStr] = Field(default=None, alias="cancelCloseReason")
    cancel_id: Optional[StrictStr] = Field(default=None, alias="cancelId")
    cancel_reason: Optional[StrictStr] = Field(default=None, alias="cancelReason")
    cancel_request_date: Optional[Timestamp] = Field(default=None, alias="cancelRequestDate")
    cancel_state: Optional[StrictStr] = Field(default=None, alias="cancelState")
    cancel_status: Optional[StrictStr] = Field(default=None, alias="cancelStatus")
    legacy_order_id: Optional[StrictStr] = Field(default=None, alias="legacyOrderId")
    marketplace_id: Optional[StrictStr] = Field(default=None, alias="marketplaceId")
    partial_order_type: Optional[PartialOrderTypeEnum] = Field(default=None, alias="partialOrderType")
    payment_status: Optional[PaymentStatusEnum] = Field(default=None, alias="paymentStatus")
    payout_recoup_info: Optional[PayoutRecoupInfo] = Field(default=None, alias="payoutRecoupInfo")
    requestor_type: Optional[PartyEnum] = Field(default=None, alias="requestorType")
    request_refund_amount: Optional[Amount] = Field(default=None, alias="requestRefundAmount")
    seller_login_name: Optional[StrictStr] = Field(default=None, alias="sellerLoginName")
    seller_response_due_date: Optional[Timestamp] = Field(default=None, alias="sellerResponseDueDate")
    shipment_date: Optional[Timestamp] = Field(default=None, alias="shipmentDate")
