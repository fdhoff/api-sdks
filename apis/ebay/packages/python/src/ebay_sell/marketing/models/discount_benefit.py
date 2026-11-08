# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.amount import Amount
from ebay_sell._runtime import ApiModel


class DiscountBenefit(ApiModel):
    """DiscountBenefit model."""

    amount_off_item: Optional[Amount] = Field(default=None, alias="amountOffItem")
    amount_off_order: Optional[Amount] = Field(default=None, alias="amountOffOrder")
    percentage_off_item: Optional[StrictStr] = Field(default=None, alias="percentageOffItem")
    percentage_off_order: Optional[StrictStr] = Field(default=None, alias="percentageOffOrder")
