# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.treasury_transaction_details import TreasuryTransactionDetails
from mercury_banking.models.treasury_transaction_type import TreasuryTransactionType
from mercury_banking._runtime import ApiModel


class TreasuryTxn(ApiModel):
    """TreasuryTxn model."""

    account_id: UUID = Field(alias="accountId")
    additional_details: Optional[StrictStr] = Field(default=None, alias="additionalDetails")
    amount: Annotated[float, Field(multiple_of=0.01)]
    balance: Annotated[float, Field(multiple_of=0.01)]
    canonical_day: date = Field(alias="canonicalDay")
    description: StrictStr
    details: Optional[TreasuryTransactionDetails] = None
    id: UUID
    security: Optional[StrictStr] = None
    type: TreasuryTransactionType
