# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.update_books_api_journal_entry_request import UpdateBooksAPIJournalEntryRequest
from mercury_banking._runtime import ApiModel


class UpdateBooksAPIJournalEntriesRequest(ApiModel):
    """UpdateBooksAPIJournalEntriesRequest model."""

    updates: List[UpdateBooksAPIJournalEntryRequest]
