# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from uuid import UUID
from mercury_banking._runtime import ApiModel


class CreditAccountStatementPayload(ApiModel):
    """CreditAccountStatementPayload model."""

    credit_limit: float = Field(alias="creditLimit")
    credit_period_id: UUID = Field(alias="creditPeriodId")
    due_date: StrictStr = Field(alias="dueDate")
    starting_balance: float = Field(alias="startingBalance")
    total_autopay_payments: float = Field(alias="totalAutopayPayments")
    total_cashback_earned: float = Field(alias="totalCashbackEarned")
    total_one_time_payments: float = Field(alias="totalOneTimePayments")
    total_transactions: float = Field(alias="totalTransactions")
