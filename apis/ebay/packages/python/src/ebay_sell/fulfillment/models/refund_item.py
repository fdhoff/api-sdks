# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.legacy_reference import LegacyReference
from ebay_sell.fulfillment.models.simple_amount import SimpleAmount
from ebay_sell._runtime import ApiModel


class RefundItem(ApiModel):
    """RefundItem model."""

    refund_amount: Optional[SimpleAmount] = Field(default=None, alias="refundAmount")
    line_item_id: Optional[StrictStr] = Field(default=None, alias="lineItemId")
    legacy_reference: Optional[LegacyReference] = Field(default=None, alias="legacyReference")
