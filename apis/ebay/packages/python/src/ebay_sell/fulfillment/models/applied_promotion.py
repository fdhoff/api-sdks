# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.amount import Amount
from ebay_sell._runtime import ApiModel


class AppliedPromotion(ApiModel):
    """AppliedPromotion model."""

    description: Optional[StrictStr] = None
    discount_amount: Optional[Amount] = Field(default=None, alias="discountAmount")
    promotion_id: Optional[StrictStr] = Field(default=None, alias="promotionId")
