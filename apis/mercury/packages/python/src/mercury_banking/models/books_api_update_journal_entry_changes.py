# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_api_update_journal_entry_le_create import BooksAPIUpdateJournalEntryLECreate
from mercury_banking.models.books_api_update_journal_entry_le_update import BooksAPIUpdateJournalEntryLEUpdate
from mercury_banking._runtime import ApiModel


class BooksAPIUpdateJournalEntryChanges(ApiModel):
    """BooksAPIUpdateJournalEntryChanges model."""

    create: Optional[List[BooksAPIUpdateJournalEntryLECreate]] = None
    delete: Optional[List[StrictStr]] = None
    update: Optional[List[BooksAPIUpdateJournalEntryLEUpdate]] = None
