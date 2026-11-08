# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.simple_amount import SimpleAmount
from ebay_sell._runtime import ApiModel


class PaymentDisputeSummary(ApiModel):
    """PaymentDisputeSummary model."""

    amount: Optional[SimpleAmount] = None
    buyer_username: Optional[StrictStr] = Field(default=None, alias="buyerUsername")
    closed_date: Optional[StrictStr] = Field(default=None, alias="closedDate")
    open_date: Optional[StrictStr] = Field(default=None, alias="openDate")
    order_id: Optional[StrictStr] = Field(default=None, alias="orderId")
    payment_dispute_id: Optional[StrictStr] = Field(default=None, alias="paymentDisputeId")
    payment_dispute_status: Optional[StrictStr] = Field(default=None, alias="paymentDisputeStatus")
    reason: Optional[StrictStr] = None
    respond_by_date: Optional[StrictStr] = Field(default=None, alias="respondByDate")
