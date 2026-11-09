# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.books_debit_credit import BooksDebitCredit
from mercury_banking._runtime import ApiModel


class BooksAPIUpdateJournalEntryLECreate(ApiModel):
    """BooksAPIUpdateJournalEntryLECreate model."""

    amount: float
    debit_credit: BooksDebitCredit = Field(alias="debitCredit")
    description: StrictStr
    ledger_id: StrictStr = Field(alias="ledgerId")
    sort_order: Optional[Annotated[int, Field(le=9223372036854776000, strict=True, ge=-9223372036854776000)]] = Field(
        default=None, alias="sortOrder"
    )
    tag_ids: Optional[List[StrictStr]] = Field(default=None, alias="tagIds")
