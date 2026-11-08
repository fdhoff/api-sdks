# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.amount import Amount
from ebay_sell.fulfillment.models.order_refund import OrderRefund
from ebay_sell.fulfillment.models.payment import Payment
from ebay_sell._runtime import ApiModel


class PaymentSummary(ApiModel):
    """PaymentSummary model."""

    payments: Optional[List[Payment]] = None
    refunds: Optional[List[OrderRefund]] = None
    total_due_seller: Optional[Amount] = Field(default=None, alias="totalDueSeller")
