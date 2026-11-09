# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mercury_banking.models.books_api_categorization_split import BooksAPICategorizationSplit
from mercury_banking._runtime import ApiModel


class BooksAPICategorizeTransactionItem(ApiModel):
    """BooksAPICategorizeTransactionItem model."""

    journal_entry_id: StrictStr = Field(alias="journalEntryId")
    splits: Annotated[List[BooksAPICategorizationSplit], Field(min_length=1)]
