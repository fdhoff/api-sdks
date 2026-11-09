# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking._runtime import ApiModel


class BooksAccrualSourcePaymentApplicationLineEntry(ApiModel):
    """BooksAccrualSourcePaymentApplicationLineEntry model."""

    journal_entry_description: StrictStr = Field(alias="journalEntryDescription")
    journal_entry_id: StrictStr = Field(alias="journalEntryId")
    line_entry_amount: float = Field(alias="lineEntryAmount")
    line_entry_description: StrictStr = Field(alias="lineEntryDescription")
    line_entry_id: StrictStr = Field(alias="lineEntryId")
