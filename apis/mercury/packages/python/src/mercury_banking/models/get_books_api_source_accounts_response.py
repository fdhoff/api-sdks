# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_api_source_account import BooksAPISourceAccount
from mercury_banking._runtime import ApiModel


class GetBooksAPISourceAccountsResponse(ApiModel):
    """GetBooksAPISourceAccountsResponse model."""

    source_accounts: List[BooksAPISourceAccount] = Field(alias="sourceAccounts")
