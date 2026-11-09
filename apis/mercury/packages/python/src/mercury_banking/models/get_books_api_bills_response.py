# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_api_bill import BooksAPIBill
from mercury_banking._runtime import ApiModel


class GetBooksAPIBillsResponse(ApiModel):
    """GetBooksAPIBillsResponse model."""

    bills: List[BooksAPIBill]
    next_page_token: Optional[StrictStr] = Field(default=None, alias="nextPageToken")
    prev_page_token: Optional[StrictStr] = Field(default=None, alias="prevPageToken")
