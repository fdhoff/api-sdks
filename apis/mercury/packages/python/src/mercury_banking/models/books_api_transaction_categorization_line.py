# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_debit_credit import BooksDebitCredit
from mercury_banking._runtime import ApiModel


class BooksAPITransactionCategorizationLine(ApiModel):
    """BooksAPITransactionCategorizationLine model."""

    amount: float
    debit_credit: BooksDebitCredit = Field(alias="debitCredit")
    ledger_id: StrictStr = Field(alias="ledgerId")
    ledger_name: StrictStr = Field(alias="ledgerName")
    line_entry_id: StrictStr = Field(alias="lineEntryId")
