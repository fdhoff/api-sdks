# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.refund_detail_type import RefundDetailType
from ebay_sell.post_order.models.text import Text
from ebay_sell._runtime import ApiModel


class IssueRefundRequest(ApiModel):
    """IssueRefundRequest model."""

    comments: Optional[Text] = None
    refund_detail: Optional[RefundDetailType] = Field(default=None, alias="refundDetail")
    relist_item: Optional[StrictBool] = Field(default=None, alias="relistItem")
