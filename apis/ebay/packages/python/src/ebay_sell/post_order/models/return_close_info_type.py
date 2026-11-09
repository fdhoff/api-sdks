# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.buyer_close_return_reason_enum import BuyerCloseReturnReasonEnum
from ebay_sell.post_order.models.close_return_reason_enum import CloseReturnReasonEnum
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ReturnCloseInfoType(ApiModel):
    """ReturnCloseInfoType model."""

    buyer_close_comment: Optional[StrictStr] = Field(default=None, alias="buyerCloseComment")
    buyer_close_reason: Optional[BuyerCloseReturnReasonEnum] = Field(default=None, alias="buyerCloseReason")
    return_close_date: Optional[Timestamp] = Field(default=None, alias="returnCloseDate")
    return_close_reason: Optional[CloseReturnReasonEnum] = Field(default=None, alias="returnCloseReason")
