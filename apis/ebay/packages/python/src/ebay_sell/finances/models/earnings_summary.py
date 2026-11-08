# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell.finances.models.expense import Expense
from ebay_sell._runtime import ApiModel


class EarningsSummary(ApiModel):
    """EarningsSummary model."""

    expenses: Optional[Expense] = None
    gross_amount: Optional[Amount] = Field(default=None, alias="grossAmount")
    order_earnings: Optional[Amount] = Field(default=None, alias="orderEarnings")
    refunds: Optional[Amount] = None
