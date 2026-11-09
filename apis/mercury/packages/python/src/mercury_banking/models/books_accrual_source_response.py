# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.books_accrual_source_display_status import BooksAccrualSourceDisplayStatus
from mercury_banking.models.books_accrual_source_file import BooksAccrualSourceFile
from mercury_banking.models.books_accrual_source_line import BooksAccrualSourceLine
from mercury_banking.models.books_accrual_source_payment_application import BooksAccrualSourcePaymentApplication
from mercury_banking.models.books_accrual_source_status import BooksAccrualSourceStatus
from mercury_banking.models.books_accrual_source_unapplied_payment import BooksAccrualSourceUnappliedPayment
from mercury_banking.models.books_bill_pay_invoice_attachment import BooksBillPayInvoiceAttachment
from mercury_banking.models.books_external_party_id import BooksExternalPartyId
from mercury_banking.models.books_needs_action_reason import BooksNeedsActionReason
from mercury_banking._runtime import ApiModel


class BooksAccrualSourceResponse(ApiModel):
    """BooksAccrualSourceResponse model."""

    amount_outstanding: float = Field(alias="amountOutstanding")
    amount_paid: float = Field(alias="amountPaid")
    bill_pay_invoice_attachment: Optional[BooksBillPayInvoiceAttachment] = Field(
        default=None, alias="billPayInvoiceAttachment"
    )
    display_status: BooksAccrualSourceDisplayStatus = Field(alias="displayStatus")
    due_date: Optional[date] = Field(default=None, alias="dueDate")
    effective_date: date = Field(alias="effectiveDate")
    external_id: Optional[StrictStr] = Field(default=None, alias="externalId")
    external_party_id: Optional[BooksExternalPartyId] = Field(default=None, alias="externalPartyId")
    files: Optional[List[BooksAccrualSourceFile]] = None
    gross_amount: float = Field(alias="grossAmount")
    id: Optional[StrictStr] = None
    journal_entry_ids: List[StrictStr] = Field(alias="journalEntryIds")
    lines: Optional[List[BooksAccrualSourceLine]] = None
    needs_action_reason: Optional[BooksNeedsActionReason] = Field(default=None, alias="needsActionReason")
    notes: Optional[StrictStr] = None
    payment_applications: Optional[List[BooksAccrualSourcePaymentApplication]] = Field(
        default=None, alias="paymentApplications"
    )
    reference_number: Optional[StrictStr] = Field(default=None, alias="referenceNumber")
    status: BooksAccrualSourceStatus
    type: StrictStr
    unapplied_payments: Optional[Annotated[List[BooksAccrualSourceUnappliedPayment], Field(min_length=1)]] = Field(
        default=None, alias="unappliedPayments"
    )
