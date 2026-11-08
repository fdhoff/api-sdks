# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell._runtime import ApiModel


class OrderEarningsSummary(ApiModel):
    """OrderEarningsSummary model."""

    expenses: Optional[Amount] = None
    gross_amount: Optional[Amount] = Field(default=None, alias="grossAmount")
    order_count: Optional[StrictInt] = Field(default=None, alias="orderCount")
    order_earnings: Optional[Amount] = Field(default=None, alias="orderEarnings")
    refunds: Optional[Amount] = None
