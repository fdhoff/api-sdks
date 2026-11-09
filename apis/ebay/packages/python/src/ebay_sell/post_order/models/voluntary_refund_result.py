# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.refund_payment_type_enum import RefundPaymentTypeEnum
from ebay_sell.post_order.models.refund_status_enum import RefundStatusEnum
from ebay_sell._runtime import ApiModel


class VoluntaryRefundResult(ApiModel):
    """VoluntaryRefundResult model."""

    refund_source: Optional[RefundPaymentTypeEnum] = Field(default=None, alias="refundSource")
    refund_status: Optional[RefundStatusEnum] = Field(default=None, alias="refundStatus")
