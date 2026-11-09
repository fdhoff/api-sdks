# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_debit_credit import BooksDebitCredit
from mercury_banking.models.books_ledger_sub_type import BooksLedgerSubType
from mercury_banking.models.books_ledger_type import BooksLedgerType
from mercury_banking.models.books_required_ledger_purpose import BooksRequiredLedgerPurpose
from mercury_banking._runtime import ApiModel


class BooksAPILedgerBalance(ApiModel):
    """BooksAPILedgerBalance model."""

    closing_balance: float = Field(alias="closingBalance")
    debit_credit: BooksDebitCredit = Field(alias="debitCredit")
    ledger_id: StrictStr = Field(alias="ledgerId")
    name: StrictStr
    net_activity: float = Field(alias="netActivity")
    opening_balance: float = Field(alias="openingBalance")
    special_type: Optional[BooksRequiredLedgerPurpose] = Field(default=None, alias="specialType")
    sub_type: BooksLedgerSubType = Field(alias="subType")
    type: BooksLedgerType
