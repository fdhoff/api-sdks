# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.amount import Amount
from ebay_sell._runtime import ApiModel


class Budget(ApiModel):
    """Budget model."""

    amount: Optional[Amount] = None
    budget_status: Optional[StrictStr] = Field(default=None, alias="budgetStatus")
