# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking._runtime import ApiModel


class TreasuryTransactionDetails(ApiModel):
    """TreasuryTransactionDetails model."""

    credit_description: Optional[StrictStr] = Field(default=None, alias="creditDescription")
    deposit_counterparty_id: Optional[UUID] = Field(default=None, alias="depositCounterpartyId")
    fee_description: Optional[StrictStr] = Field(default=None, alias="feeDescription")
    manual_amendment_description: Optional[StrictStr] = Field(default=None, alias="manualAmendmentDescription")
    security: Optional[StrictStr] = None
    sweep_direction: Optional[StrictStr] = Field(default=None, alias="sweepDirection")
    trade_action: Optional[StrictStr] = Field(default=None, alias="tradeAction")
    withdrawal_counterparty_id: Optional[UUID] = Field(default=None, alias="withdrawalCounterpartyId")
