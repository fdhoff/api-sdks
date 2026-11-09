# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.decision_enum import DecisionEnum
from ebay_sell.post_order.models.text import Text
from ebay_sell._runtime import ApiModel


class DecideReturnRequest(ApiModel):
    """DecideReturnRequest model."""

    comments: Optional[Text] = None
    decision: Optional[DecisionEnum] = None
    keep_original_item: Optional[StrictBool] = Field(default=None, alias="keepOriginalItem")
    partial_refund_amount: Optional[Amount] = Field(default=None, alias="partialRefundAmount")
    rma_number: Optional[StrictStr] = Field(default=None, alias="RMANumber")
    r_ma_provided: Optional[StrictBool] = Field(default=None, alias="rMAProvided")
