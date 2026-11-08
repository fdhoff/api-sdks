# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell.finances.models.order_earning_fee import OrderEarningFee
from ebay_sell._runtime import ApiModel


class Expense(ApiModel):
    """Expense model."""

    currency: Optional[StrictStr] = None
    donations: Optional[List[OrderEarningFee]] = None
    marketplace_fees: Optional[List[OrderEarningFee]] = Field(default=None, alias="marketplaceFees")
    shipping_labels: Optional[Amount] = Field(default=None, alias="shippingLabels")
    value: Optional[StrictStr] = None
