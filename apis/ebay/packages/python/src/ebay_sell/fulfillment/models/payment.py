# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.amount import Amount
from ebay_sell.fulfillment.models.payment_hold import PaymentHold
from ebay_sell._runtime import ApiModel


class Payment(ApiModel):
    """Payment model."""

    amount: Optional[Amount] = None
    payment_date: Optional[StrictStr] = Field(default=None, alias="paymentDate")
    payment_holds: Optional[List[PaymentHold]] = Field(default=None, alias="paymentHolds")
    payment_method: Optional[StrictStr] = Field(default=None, alias="paymentMethod")
    payment_reference_id: Optional[StrictStr] = Field(default=None, alias="paymentReferenceId")
    payment_status: Optional[StrictStr] = Field(default=None, alias="paymentStatus")
