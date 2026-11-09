# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_accrual_source_display_status import BooksAccrualSourceDisplayStatus
from mercury_banking.models.books_accrual_source_line import BooksAccrualSourceLine
from mercury_banking.models.books_accrual_source_status import BooksAccrualSourceStatus
from mercury_banking.models.books_external_party_id import BooksExternalPartyId
from mercury_banking._runtime import ApiModel


class BooksAccrualSourceBaseResponse(ApiModel):
    """BooksAccrualSourceBaseResponse model."""

    amount_outstanding: float = Field(alias="amountOutstanding")
    amount_paid: float = Field(alias="amountPaid")
    display_status: BooksAccrualSourceDisplayStatus = Field(alias="displayStatus")
    due_date: Optional[date] = Field(default=None, alias="dueDate")
    effective_date: date = Field(alias="effectiveDate")
    external_id: Optional[StrictStr] = Field(default=None, alias="externalId")
    external_party_id: Optional[BooksExternalPartyId] = Field(default=None, alias="externalPartyId")
    gross_amount: float = Field(alias="grossAmount")
    id: StrictStr
    lines: Optional[List[BooksAccrualSourceLine]] = None
    notes: Optional[StrictStr] = None
    reference_number: Optional[StrictStr] = Field(default=None, alias="referenceNumber")
    status: BooksAccrualSourceStatus
    type: StrictStr
