# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.buyer_with_id import BuyerWithId
from ebay_sell.finances.models.earnings_summary import EarningsSummary
from ebay_sell.finances.models.order_summary import OrderSummary
from ebay_sell._runtime import ApiModel


class OrderEarning(ApiModel):
    """OrderEarning model."""

    buyer: Optional[BuyerWithId] = None
    order_creation_date: Optional[StrictStr] = Field(default=None, alias="orderCreationDate")
    order_earnings_summary: Optional[EarningsSummary] = Field(default=None, alias="orderEarningsSummary")
    order_id: Optional[StrictStr] = Field(default=None, alias="orderId")
    order_last_modified_date: Optional[StrictStr] = Field(default=None, alias="orderLastModifiedDate")
    order_summary: Optional[OrderSummary] = Field(default=None, alias="orderSummary")
