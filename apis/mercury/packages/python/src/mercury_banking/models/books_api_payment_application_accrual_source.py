# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_accrual_source_display_status import BooksAccrualSourceDisplayStatus
from mercury_banking.models.books_accrual_source_status import BooksAccrualSourceStatus
from mercury_banking._runtime import ApiModel


class BooksAPIPaymentApplicationAccrualSource(ApiModel):
    """BooksAPIPaymentApplicationAccrualSource model."""

    amount_adjusted: float = Field(alias="amountAdjusted")
    amount_outstanding: float = Field(alias="amountOutstanding")
    amount_paid: float = Field(alias="amountPaid")
    display_status: BooksAccrualSourceDisplayStatus = Field(alias="displayStatus")
    id: StrictStr
    status: BooksAccrualSourceStatus
