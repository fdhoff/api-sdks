# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account.models.recipient_account_reference import RecipientAccountReference
from ebay_sell._runtime import ApiModel


class PaymentMethod(ApiModel):
    """PaymentMethod model."""

    brands: Optional[List[StrictStr]] = None
    payment_method_type: Optional[StrictStr] = Field(default=None, alias="paymentMethodType")
    recipient_account_reference: Optional[RecipientAccountReference] = Field(
        default=None, alias="recipientAccountReference"
    )
