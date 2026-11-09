# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking._runtime import ApiModel


class BooksPaymentApplicationAccrualAdjustment(ApiModel):
    """BooksPaymentApplicationAccrualAdjustment model."""

    accrual_adjustment_id: StrictStr = Field(alias="accrualAdjustmentId")
    amount: float
    credit_account_id: StrictStr = Field(alias="creditAccountId")
    debit_account_id: StrictStr = Field(alias="debitAccountId")
