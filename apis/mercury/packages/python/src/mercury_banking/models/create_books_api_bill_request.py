# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.create_books_api_bill_line import CreateBooksAPIBillLine
from mercury_banking.models.create_books_api_bill_vendor import CreateBooksAPIBillVendor
from mercury_banking._runtime import ApiModel


class CreateBooksAPIBillRequest(ApiModel):
    """CreateBooksAPIBillRequest model."""

    due_date: date = Field(alias="dueDate")
    effective_date: date = Field(alias="effectiveDate")
    lines: Annotated[List[CreateBooksAPIBillLine], Field(min_length=1)]
    notes: Optional[StrictStr] = None
    reference_number: Optional[StrictStr] = Field(default=None, alias="referenceNumber")
    vendor: CreateBooksAPIBillVendor
