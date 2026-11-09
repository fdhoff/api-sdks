# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_autocat_method import BooksAutocatMethod
from mercury_banking._runtime import ApiModel


class BooksAutocatResult(ApiModel):
    """BooksAutocatResult model."""

    confidence: float
    created_at: StrictStr = Field(alias="createdAt")
    id: StrictStr
    ledger_id: StrictStr = Field(alias="ledgerId")
    method: BooksAutocatMethod
    rule_id: Optional[StrictStr] = Field(default=None, alias="ruleId")
