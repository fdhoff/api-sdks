# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell._runtime import ApiModel


class ItemizedRefundDetailType(ApiModel):
    """ItemizedRefundDetailType model."""

    refund_amount: Optional[Amount] = Field(default=None, alias="refundAmount")
    refund_fee_type: Optional[StrictStr] = Field(default=None, alias="refundFeeType")
    restocking_fee_percentage: Optional[StrictStr] = Field(default=None, alias="restockingFeePercentage")
