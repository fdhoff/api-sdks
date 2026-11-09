# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_accrual_source_display_status import BooksAccrualSourceDisplayStatus
from mercury_banking.models.books_accrual_source_status import BooksAccrualSourceStatus
from mercury_banking.models.books_api_bill_line import BooksAPIBillLine
from mercury_banking.models.books_api_bill_payment_application import BooksAPIBillPaymentApplication
from mercury_banking.models.books_api_bill_vendor import BooksAPIBillVendor
from mercury_banking._runtime import ApiModel


class BooksAPIBill(ApiModel):
    """BooksAPIBill model."""

    amount_remaining: float = Field(alias="amountRemaining")
    display_status: BooksAccrualSourceDisplayStatus = Field(alias="displayStatus")
    due_date: Optional[date] = Field(default=None, alias="dueDate")
    effective_date: date = Field(alias="effectiveDate")
    gross_amount: float = Field(alias="grossAmount")
    id: StrictStr
    lines: List[BooksAPIBillLine]
    notes: Optional[StrictStr] = None
    payment_applications: List[BooksAPIBillPaymentApplication] = Field(alias="paymentApplications")
    reference_number: Optional[StrictStr] = Field(default=None, alias="referenceNumber")
    status: BooksAccrualSourceStatus
    vendor: Optional[BooksAPIBillVendor] = None
