# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_api_categorized_transaction import BooksAPICategorizedTransaction
from mercury_banking._runtime import ApiModel


class CategorizeBooksAPITransactionsResponse(ApiModel):
    """CategorizeBooksAPITransactionsResponse model."""

    items: List[BooksAPICategorizedTransaction]
