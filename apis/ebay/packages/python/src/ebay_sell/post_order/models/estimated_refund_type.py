# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.refund_fee_type_enum import RefundFeeTypeEnum
from ebay_sell._runtime import ApiModel


class EstimatedRefundType(ApiModel):
    """EstimatedRefundType model."""

    estimated_amount: Optional[Amount] = Field(default=None, alias="estimatedAmount")
    max_amount: Optional[Amount] = Field(default=None, alias="maxAmount")
    min_amount: Optional[Amount] = Field(default=None, alias="minAmount")
    purchase_price_deducted_percentage_list: Optional[List[StrictInt]] = Field(
        default=None, alias="purchasePriceDeductedPercentageList"
    )
    refund_fee_type: Optional[RefundFeeTypeEnum] = Field(default=None, alias="refundFeeType")
    restocking_fee_percentage: Optional[StrictStr] = Field(default=None, alias="restockingFeePercentage")
