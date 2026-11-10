# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_accrual_source_display_status import BooksAccrualSourceDisplayStatus
from mercury_banking.models.books_accrual_source_status import BooksAccrualSourceStatus
from mercury_banking.models.books_api_invoice_customer import BooksAPIInvoiceCustomer
from mercury_banking.models.books_api_invoice_line import BooksAPIInvoiceLine
from mercury_banking.models.books_api_invoice_payment_application import BooksAPIInvoicePaymentApplication
from mercury_banking._runtime import ApiModel


class BooksAPIInvoice(ApiModel):
    """BooksAPIInvoice model."""

    amount_remaining: float = Field(alias="amountRemaining")
    customer: Optional[BooksAPIInvoiceCustomer] = None
    display_status: BooksAccrualSourceDisplayStatus = Field(alias="displayStatus")
    due_date: Optional[date] = Field(default=None, alias="dueDate")
    effective_date: date = Field(alias="effectiveDate")
    gross_amount: float = Field(alias="grossAmount")
    id: StrictStr
    lines: List[BooksAPIInvoiceLine]
    notes: Optional[StrictStr] = None
    payment_applications: List[BooksAPIInvoicePaymentApplication] = Field(alias="paymentApplications")
    reference_number: Optional[StrictStr] = Field(default=None, alias="referenceNumber")
    status: BooksAccrualSourceStatus
