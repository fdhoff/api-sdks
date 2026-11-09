# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_journal_entry import BooksJournalEntry
from mercury_banking._runtime import ApiModel


class GetBooksAPIJournalEntryResponse(ApiModel):
    """GetBooksAPIJournalEntryResponse model."""

    journal_entry: BooksJournalEntry = Field(alias="journalEntry")
