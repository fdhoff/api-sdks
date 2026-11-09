# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_api_transaction_categorization_line import BooksAPITransactionCategorizationLine
from mercury_banking._runtime import ApiModel


class BooksAPICategorizedTransaction(ApiModel):
    """BooksAPICategorizedTransaction model."""

    categorization_lines: List[BooksAPITransactionCategorizationLine] = Field(alias="categorizationLines")
    journal_entry_id: StrictStr = Field(alias="journalEntryId")
