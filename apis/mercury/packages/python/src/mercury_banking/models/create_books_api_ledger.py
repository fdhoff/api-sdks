# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_debit_credit import BooksDebitCredit
from mercury_banking.models.books_ledger_sub_type import BooksLedgerSubType
from mercury_banking.models.books_ledger_type import BooksLedgerType
from mercury_banking._runtime import ApiModel


class CreateBooksAPILedger(ApiModel):
    """CreateBooksAPILedger model."""

    debit_credit: BooksDebitCredit = Field(alias="debitCredit")
    name: StrictStr
    parent_id: Optional[StrictStr] = Field(default=None, alias="parentId")
    sort_code: StrictStr = Field(alias="sortCode")
    sub_type: BooksLedgerSubType = Field(alias="subType")
    type: BooksLedgerType
