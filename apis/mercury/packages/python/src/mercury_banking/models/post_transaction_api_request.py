# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.post_transaction_payment_method import PostTransactionPaymentMethod
from mercury_banking.models.post_transaction_send_money_purpose import PostTransactionSendMoneyPurpose
from mercury_banking._runtime import ApiModel


class PostTransactionAPIRequest(ApiModel):
    """PostTransactionAPIRequest model."""

    amount: Annotated[float, Field(ge=0.01)]
    duplicate_check_override: Optional[StrictBool] = Field(default=None, alias="duplicateCheckOverride")
    external_memo: Optional[Annotated[str, Field(strict=True, max_length=299)]] = Field(
        default=None, alias="externalMemo"
    )
    idempotency_key: StrictStr = Field(alias="idempotencyKey")
    note: Optional[StrictStr] = None
    payment_method: PostTransactionPaymentMethod = Field(alias="paymentMethod")
    purpose: Optional[PostTransactionSendMoneyPurpose] = None
    recipient_id: UUID = Field(alias="recipientId")
