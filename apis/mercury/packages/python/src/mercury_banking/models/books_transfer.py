# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_transfer_entry import BooksTransferEntry
from mercury_banking._runtime import ApiModel


class BooksTransfer(ApiModel):
    """BooksTransfer model."""

    from_entry: BooksTransferEntry = Field(alias="fromEntry")
    to_entry: BooksTransferEntry = Field(alias="toEntry")
