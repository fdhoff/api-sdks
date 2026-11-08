# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.refund_item import RefundItem
from ebay_sell.fulfillment.models.simple_amount import SimpleAmount
from ebay_sell._runtime import ApiModel


class IssueRefundRequest(ApiModel):
    """IssueRefundRequest model."""

    reason_for_refund: Optional[StrictStr] = Field(default=None, alias="reasonForRefund")
    comment: Optional[StrictStr] = None
    refund_items: Optional[List[RefundItem]] = Field(default=None, alias="refundItems")
    order_level_refund_amount: Optional[SimpleAmount] = Field(default=None, alias="orderLevelRefundAmount")
