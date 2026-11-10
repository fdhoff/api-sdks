# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.create_books_api_invoice_line import CreateBooksAPIInvoiceLine
from mercury_banking._runtime import ApiModel


class CreateBooksAPIInvoiceRequest(ApiModel):
    """CreateBooksAPIInvoiceRequest model."""

    customer: UUID
    due_date: date = Field(alias="dueDate")
    effective_date: date = Field(alias="effectiveDate")
    lines: Annotated[List[CreateBooksAPIInvoiceLine], Field(min_length=1)]
    notes: Optional[StrictStr] = None
    reference_number: StrictStr = Field(alias="referenceNumber")
