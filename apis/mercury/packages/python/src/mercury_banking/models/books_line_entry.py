# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.books_accrual_source_base_response import BooksAccrualSourceBaseResponse
from mercury_banking.models.books_debit_credit import BooksDebitCredit
from mercury_banking.models.books_journal_entry_categorization_status import BooksJournalEntryCategorizationStatus
from mercury_banking.models.books_line_entry_payment_application import BooksLineEntryPaymentApplication
from mercury_banking.models.books_tag import BooksTag
from mercury_banking.models.books_transaction import BooksTransaction
from mercury_banking._runtime import ApiModel


class BooksLineEntry(ApiModel):
    """BooksLineEntry model."""

    accrual_source: Optional[BooksAccrualSourceBaseResponse] = Field(default=None, alias="accrualSource")
    amount: float
    categorization_status: BooksJournalEntryCategorizationStatus = Field(alias="categorizationStatus")
    datetime: StrictStr
    debit_credit: BooksDebitCredit = Field(alias="debitCredit")
    description: Optional[StrictStr] = None
    editable: StrictBool
    id: StrictStr
    journal_entry_description: StrictStr = Field(alias="journalEntryDescription")
    journal_entry_id: StrictStr = Field(alias="journalEntryId")
    ledger_id: StrictStr = Field(alias="ledgerId")
    ledger_name: StrictStr = Field(alias="ledgerName")
    opposing_ledger_ids: Optional[List[StrictStr]] = Field(default=None, alias="opposingLedgerIds")
    payment_applications: Optional[List[BooksLineEntryPaymentApplication]] = Field(
        default=None, alias="paymentApplications"
    )
    related_line_entry_id: Optional[StrictStr] = Field(default=None, alias="relatedLineEntryId")
    sort_order: Optional[Annotated[int, Field(le=9223372036854776000, strict=True, ge=-9223372036854776000)]] = Field(
        default=None, alias="sortOrder"
    )
    tags: Optional[List[BooksTag]] = None
    transaction: Optional[BooksTransaction] = None
    transaction_id: Optional[StrictStr] = Field(default=None, alias="transactionId")
