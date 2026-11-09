# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ConfirmRefundRequest(ApiModel):
    """ConfirmRefundRequest model."""

    refund_date: Optional[Timestamp] = Field(default=None, alias="refundDate")
    unpaid_order: Optional[StrictBool] = Field(default=None, alias="unpaidOrder")
