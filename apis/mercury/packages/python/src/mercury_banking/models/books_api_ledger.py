# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_api_ledger_delete_blocked_reason import BooksAPILedgerDeleteBlockedReason
from mercury_banking.models.books_debit_credit import BooksDebitCredit
from mercury_banking.models.books_financial_account_type import BooksFinancialAccountType
from mercury_banking.models.books_ledger_sub_type import BooksLedgerSubType
from mercury_banking.models.books_ledger_type import BooksLedgerType
from mercury_banking.models.books_required_ledger_purpose import BooksRequiredLedgerPurpose
from mercury_banking._runtime import ApiModel


class BooksAPILedger(ApiModel):
    """BooksAPILedger model."""

    debit_credit: BooksDebitCredit = Field(alias="debitCredit")
    deletable: StrictBool
    delete_blocked_reason: Optional[BooksAPILedgerDeleteBlockedReason] = Field(
        default=None, alias="deleteBlockedReason"
    )
    editable: StrictBool
    financial_account_type: Optional[BooksFinancialAccountType] = Field(default=None, alias="financialAccountType")
    id: StrictStr
    is_required: StrictBool = Field(alias="isRequired")
    name: StrictStr
    opening_balance: Optional[float] = Field(default=None, alias="openingBalance")
    parent_id: Optional[StrictStr] = Field(default=None, alias="parentId")
    required_ledger_purpose: Optional[BooksRequiredLedgerPurpose] = Field(default=None, alias="requiredLedgerPurpose")
    sort_code: StrictStr = Field(alias="sortCode")
    sub_type: BooksLedgerSubType = Field(alias="subType")
    type: BooksLedgerType
