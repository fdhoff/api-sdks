# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.amount import Amount
from ebay_sell._runtime import ApiModel


class LineItemRefund(ApiModel):
    """LineItemRefund model."""

    amount: Optional[Amount] = None
    refund_date: Optional[StrictStr] = Field(default=None, alias="refundDate")
    refund_id: Optional[StrictStr] = Field(default=None, alias="refundId")
    refund_reference_id: Optional[StrictStr] = Field(default=None, alias="refundReferenceId")
