# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking._runtime import ApiModel


class BooksAPIPaymentApplicationLineEntry(ApiModel):
    """BooksAPIPaymentApplicationLineEntry model."""

    amount: float
    amount_adjusted: float = Field(alias="amountAdjusted")
    amount_applied: float = Field(alias="amountApplied")
    id: StrictStr
    journal_entry_id: StrictStr = Field(alias="journalEntryId")
    transaction_id: Optional[StrictStr] = Field(default=None, alias="transactionId")
