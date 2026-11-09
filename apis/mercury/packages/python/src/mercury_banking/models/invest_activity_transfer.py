# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking.models.invest_activity_status import InvestActivityStatus
from mercury_banking.models.invest_activity_transfer_kind import InvestActivityTransferKind
from mercury_banking._runtime import ApiModel


class InvestActivityTransfer(ApiModel):
    """InvestActivityTransfer model."""

    amount: float
    counterparty_id: UUID = Field(alias="counterpartyId")
    counterparty_name: StrictStr = Field(alias="counterpartyName")
    is_automated: StrictBool = Field(alias="isAutomated")
    kind: InvestActivityTransferKind
    posted_at: Optional[StrictStr] = Field(default=None, alias="postedAt")
    status: InvestActivityStatus
    transaction_id: UUID = Field(alias="transactionId")
