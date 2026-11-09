# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mercury_banking.models.set_books_api_ledger_opening_balance import SetBooksAPILedgerOpeningBalance
from mercury_banking._runtime import ApiModel


class SetBooksAPILedgerOpeningBalancesRequest(ApiModel):
    """SetBooksAPILedgerOpeningBalancesRequest model."""

    opening_balances: Annotated[List[SetBooksAPILedgerOpeningBalance], Field(min_length=1)] = Field(
        alias="openingBalances"
    )
