# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_api_source_account_origin import BooksAPISourceAccountOrigin
from mercury_banking.models.books_api_source_account_usage import BooksAPISourceAccountUsage
from mercury_banking.models.books_debit_credit import BooksDebitCredit
from mercury_banking._runtime import ApiModel


class BooksAPISourceAccount(ApiModel):
    """BooksAPISourceAccount model."""

    business_personal: BooksAPISourceAccountUsage = Field(alias="businessPersonal")
    debit_credit: BooksDebitCredit = Field(alias="debitCredit")
    id: StrictStr
    ledger_id: StrictStr = Field(alias="ledgerId")
    name: StrictStr
    origin: BooksAPISourceAccountOrigin
