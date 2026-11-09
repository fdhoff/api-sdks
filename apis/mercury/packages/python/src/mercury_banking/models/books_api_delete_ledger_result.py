# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_api_ledger_write_error import BooksAPILedgerWriteError
from mercury_banking._runtime import ApiModel


class BooksAPIDeleteLedgerResult(ApiModel):
    """BooksAPIDeleteLedgerResult model."""

    deleted: StrictBool
    error: Optional[BooksAPILedgerWriteError] = None
    ledger_id: StrictStr = Field(alias="ledgerId")
