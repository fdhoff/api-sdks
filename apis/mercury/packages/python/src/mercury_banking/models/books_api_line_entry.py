# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_debit_credit import BooksDebitCredit
from mercury_banking.models.books_tag import BooksTag
from mercury_banking._runtime import ApiModel


class BooksAPILineEntry(ApiModel):
    """BooksAPILineEntry model."""

    amount: float
    datetime: StrictStr
    debit_credit: BooksDebitCredit = Field(alias="debitCredit")
    description: Optional[StrictStr] = None
    id: StrictStr
    journal_entry_description: StrictStr = Field(alias="journalEntryDescription")
    journal_entry_id: StrictStr = Field(alias="journalEntryId")
    ledger_id: StrictStr = Field(alias="ledgerId")
    ledger_name: StrictStr = Field(alias="ledgerName")
    opposing_ledger_ids: List[StrictStr] = Field(alias="opposingLedgerIds")
    tags: List[BooksTag]
