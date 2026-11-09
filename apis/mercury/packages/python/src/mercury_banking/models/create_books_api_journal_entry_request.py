# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_api_create_journal_entry_line_entry import BooksAPICreateJournalEntryLineEntry
from mercury_banking._runtime import ApiModel


class CreateBooksAPIJournalEntryRequest(ApiModel):
    """CreateBooksAPIJournalEntryRequest model."""

    datetime: StrictStr
    description: StrictStr
    line_entries: List[BooksAPICreateJournalEntryLineEntry] = Field(alias="lineEntries")
