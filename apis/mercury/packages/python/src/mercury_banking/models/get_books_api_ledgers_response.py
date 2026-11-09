# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_api_ledger import BooksAPILedger
from mercury_banking._runtime import ApiModel


class GetBooksAPILedgersResponse(ApiModel):
    """GetBooksAPILedgersResponse model."""

    ledgers: List[BooksAPILedger]
    next_page_token: Optional[StrictStr] = Field(default=None, alias="nextPageToken")
    prev_page_token: Optional[StrictStr] = Field(default=None, alias="prevPageToken")
