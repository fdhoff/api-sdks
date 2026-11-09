# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_debit_credit import BooksDebitCredit
from mercury_banking.models.books_ledger_clear_field import BooksLedgerClearField
from mercury_banking.models.books_ledger_sub_type import BooksLedgerSubType
from mercury_banking.models.books_ledger_type import BooksLedgerType
from mercury_banking._runtime import ApiModel


class UpdateBooksAPILedger(ApiModel):
    """UpdateBooksAPILedger model."""

    clear_fields: Optional[List[BooksLedgerClearField]] = Field(default=None, alias="clearFields")
    debit_credit: Optional[BooksDebitCredit] = Field(default=None, alias="debitCredit")
    ledger_id: StrictStr = Field(alias="ledgerId")
    name: Optional[StrictStr] = None
    parent_id: Optional[StrictStr] = Field(default=None, alias="parentId")
    sort_code: Optional[StrictStr] = Field(default=None, alias="sortCode")
    sub_type: Optional[BooksLedgerSubType] = Field(default=None, alias="subType")
    type: Optional[BooksLedgerType] = None
