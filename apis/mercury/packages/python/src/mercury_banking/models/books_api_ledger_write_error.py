# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_api_ledger_write_error_code import BooksAPILedgerWriteErrorCode
from mercury_banking._runtime import ApiModel


class BooksAPILedgerWriteError(ApiModel):
    """BooksAPILedgerWriteError model."""

    code: BooksAPILedgerWriteErrorCode
    message: StrictStr
