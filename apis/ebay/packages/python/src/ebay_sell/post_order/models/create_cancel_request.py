# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.relist_line_item import RelistLineItem
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class CreateCancelRequest(ApiModel):
    """CreateCancelRequest model."""

    buyer_paid: Optional[StrictBool] = Field(default=None, alias="buyerPaid")
    buyer_paid_date: Optional[Timestamp] = Field(default=None, alias="buyerPaidDate")
    cancel_reason: Optional[StrictStr] = Field(default=None, alias="cancelReason")
    legacy_order_id: Optional[StrictStr] = Field(default=None, alias="legacyOrderId")
    relist_line_item: Optional[List[RelistLineItem]] = Field(default=None, alias="relistLineItem")
