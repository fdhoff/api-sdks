# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_accrual_source_response import BooksAccrualSourceResponse
from mercury_banking.models.books_autocat_result import BooksAutocatResult
from mercury_banking.models.books_journal_entry_categorization_status import BooksJournalEntryCategorizationStatus
from mercury_banking.models.books_journal_entry_creation_source import BooksJournalEntryCreationSource
from mercury_banking.models.books_journal_entry_review_status import BooksJournalEntryReviewStatus
from mercury_banking.models.books_line_entry import BooksLineEntry
from mercury_banking.models.books_transfer import BooksTransfer
from mercury_banking._runtime import ApiModel


class BooksJournalEntry(ApiModel):
    """BooksJournalEntry model."""

    accrual_source: Optional[BooksAccrualSourceResponse] = Field(default=None, alias="accrualSource")
    autocat_result: Optional[BooksAutocatResult] = Field(default=None, alias="autocatResult")
    categorization_status: BooksJournalEntryCategorizationStatus = Field(alias="categorizationStatus")
    creation_date: StrictStr = Field(alias="creationDate")
    creation_source: BooksJournalEntryCreationSource = Field(alias="creationSource")
    datetime: StrictStr
    description: StrictStr
    id: StrictStr
    is_opening_balance: StrictBool = Field(alias="isOpeningBalance")
    line_entries: Optional[List[BooksLineEntry]] = Field(default=None, alias="lineEntries")
    line_entry_ids: Optional[List[StrictStr]] = Field(default=None, alias="lineEntryIds")
    review_status: BooksJournalEntryReviewStatus = Field(alias="reviewStatus")
    review_status_set_at: Optional[StrictStr] = Field(default=None, alias="reviewStatusSetAt")
    transfer: Optional[BooksTransfer] = None
