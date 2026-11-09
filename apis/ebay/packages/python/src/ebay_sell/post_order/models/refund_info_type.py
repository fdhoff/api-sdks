# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.actual_refund_detail_type import ActualRefundDetailType
from ebay_sell.post_order.models.estimated_refund_detail_type import EstimatedRefundDetailType
from ebay_sell.post_order.models.provisional_refund_type import ProvisionalRefundType
from ebay_sell._runtime import ApiModel


class RefundInfoType(ApiModel):
    """RefundInfoType model."""

    actual_refund_detail: Optional[ActualRefundDetailType] = Field(default=None, alias="actualRefundDetail")
    estimated_refund_detail: Optional[EstimatedRefundDetailType] = Field(default=None, alias="estimatedRefundDetail")
    provisional_refund: Optional[ProvisionalRefundType] = Field(default=None, alias="provisionalRefund")
