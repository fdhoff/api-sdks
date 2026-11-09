# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_api_ledger_balance import BooksAPILedgerBalance
from mercury_banking._runtime import ApiModel


class GetBooksAPILedgerBalancesResponse(ApiModel):
    """GetBooksAPILedgerBalancesResponse model."""

    ledger_balances: List[BooksAPILedgerBalance] = Field(alias="ledgerBalances")
