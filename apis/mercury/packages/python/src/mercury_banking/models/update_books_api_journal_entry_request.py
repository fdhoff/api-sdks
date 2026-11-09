# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_api_update_journal_entry_changes import BooksAPIUpdateJournalEntryChanges
from mercury_banking.models.books_journal_entry_review_status import BooksJournalEntryReviewStatus
from mercury_banking._runtime import ApiModel


class UpdateBooksAPIJournalEntryRequest(ApiModel):
    """UpdateBooksAPIJournalEntryRequest model."""

    datetime: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    journal_entry_id: StrictStr = Field(alias="journalEntryId")
    line_entry_changes: Optional[BooksAPIUpdateJournalEntryChanges] = Field(default=None, alias="lineEntryChanges")
    review_status: Optional[BooksJournalEntryReviewStatus] = Field(default=None, alias="reviewStatus")
