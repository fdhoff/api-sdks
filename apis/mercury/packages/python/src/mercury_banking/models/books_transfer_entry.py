# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_line_entry import BooksLineEntry
from mercury_banking._runtime import ApiModel


class BooksTransferEntry(ApiModel):
    """BooksTransferEntry model."""

    datetime: StrictStr
    description: StrictStr
    journal_entry_id: StrictStr = Field(alias="journalEntryId")
    line_entries: List[BooksLineEntry] = Field(alias="lineEntries")
