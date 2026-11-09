# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.buyer_close_reason_enum import BuyerCloseReasonEnum
from ebay_sell.post_order.models.text import Text
from ebay_sell._runtime import ApiModel


class BuyerCloseInquiryRequest(ApiModel):
    """BuyerCloseInquiryRequest model."""

    close_reason: Optional[BuyerCloseReasonEnum] = Field(default=None, alias="closeReason")
    comments: Optional[Text] = None
