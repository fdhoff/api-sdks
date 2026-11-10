# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_api_invoice_customer import BooksAPIInvoiceCustomer
from mercury_banking.models.books_api_invoice_sync_status import BooksAPIInvoiceSyncStatus
from mercury_banking._runtime import ApiModel


class BooksAPIPendingInvoice(ApiModel):
    """BooksAPIPendingInvoice model."""

    customer: BooksAPIInvoiceCustomer
    due_date: date = Field(alias="dueDate")
    effective_date: date = Field(alias="effectiveDate")
    gross_amount: float = Field(alias="grossAmount")
    message: StrictStr
    reference_number: StrictStr = Field(alias="referenceNumber")
    sync_status: BooksAPIInvoiceSyncStatus = Field(alias="syncStatus")
