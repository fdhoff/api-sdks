# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.money_movement_ref import MoneyMovementRef
from ebay_sell.post_order.models.refund_deduction_type import RefundDeductionType
from ebay_sell.post_order.models.return_address_type import ReturnAddressType
from ebay_sell.post_order.models.rlsp_type_enum import RlspTypeEnum
from ebay_sell._runtime import ApiModel


class ResponseHistoryAttributesType(ApiModel):
    """ResponseHistoryAttributesType model."""

    escalate_reason: Optional[StrictStr] = Field(default=None, alias="escalateReason")
    keep_original_item: Optional[StrictBool] = Field(default=None, alias="keepOriginalItem")
    money_movement_ref: Optional[MoneyMovementRef] = Field(default=None, alias="moneyMovementRef")
    partial_refund_amount: Optional[Amount] = Field(default=None, alias="partialRefundAmount")
    refund_deduction_type: Optional[RefundDeductionType] = Field(default=None, alias="refundDeductionType")
    rlsp_type: Optional[RlspTypeEnum] = Field(default=None, alias="rlspType")
    rma: Optional[StrictStr] = Field(default=None, alias="RMA")
    seller_return_address: Optional[ReturnAddressType] = Field(default=None, alias="sellerReturnAddress")
    to_email_address: Optional[StrictStr] = Field(default=None, alias="toEmailAddress")
    updated_tracking_number: Optional[StrictStr] = Field(default=None, alias="updatedTrackingNumber")
