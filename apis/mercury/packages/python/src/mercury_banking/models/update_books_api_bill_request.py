# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking.models.update_books_api_bill_line_changes import UpdateBooksAPIBillLineChanges
from mercury_banking._runtime import ApiModel


class UpdateBooksAPIBillRequest(ApiModel):
    """UpdateBooksAPIBillRequest model."""

    due_date: Optional[date] = Field(default=None, alias="dueDate")
    effective_date: Optional[date] = Field(default=None, alias="effectiveDate")
    line_changes: Optional[UpdateBooksAPIBillLineChanges] = Field(default=None, alias="lineChanges")
    notes: Optional[StrictStr] = None
    reference_number: Optional[StrictStr] = Field(default=None, alias="referenceNumber")
    vendor: Optional[UUID] = None
