# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.amount import Amount
from ebay_sell._runtime import ApiModel


class Fee(ApiModel):
    """Fee model."""

    amount: Optional[Amount] = None
    fee_type: Optional[StrictStr] = Field(default=None, alias="feeType")
    promotional_discount: Optional[Amount] = Field(default=None, alias="promotionalDiscount")
