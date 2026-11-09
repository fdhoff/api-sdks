# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.post_transaction_send_money_purpose import PostTransactionSendMoneyPurpose
from mercury_banking.models.request_send_money_payment_method import RequestSendMoneyPaymentMethod
from mercury_banking._runtime import ApiModel


class SendMoneyAPIRequest(ApiModel):
    """SendMoneyAPIRequest model."""

    amount: Annotated[float, Field(ge=0.01)]
    charge_type: Optional[StrictStr] = Field(default=None, alias="chargeType")
    external_memo: Optional[StrictStr] = Field(default=None, alias="externalMemo")
    idempotency_key: StrictStr = Field(alias="idempotencyKey")
    note: Optional[StrictStr] = None
    payment_method: RequestSendMoneyPaymentMethod = Field(alias="paymentMethod")
    purpose: Optional[PostTransactionSendMoneyPurpose] = None
    recipient_id: UUID = Field(alias="recipientId")
