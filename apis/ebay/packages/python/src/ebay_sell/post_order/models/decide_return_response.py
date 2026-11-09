# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.refund_money_movement_status_enum import RefundMoneyMovementStatusEnum
from ebay_sell._runtime import ApiModel


class DecideReturnResponse(ApiModel):
    """DecideReturnResponse model."""

    refund_status: Optional[RefundMoneyMovementStatusEnum] = Field(default=None, alias="refundStatus")
