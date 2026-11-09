# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.payment_provider_enum import PaymentProviderEnum
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class RetMoneyMovementDetailType(ApiModel):
    """RetMoneyMovementDetailType model."""

    actual_amount: Optional[Amount] = Field(default=None, alias="actualAmount")
    creation_date: Optional[Timestamp] = Field(default=None, alias="creationDate")
    external_payment_id: Optional[StrictStr] = Field(default=None, alias="externalPaymentId")
    money_movement_type: Optional[StrictStr] = Field(default=None, alias="moneyMovementType")
    payment_provider: Optional[PaymentProviderEnum] = Field(default=None, alias="paymentProvider")
    requested_amount: Optional[Amount] = Field(default=None, alias="requestedAmount")
    status: Optional[StrictStr] = None
