# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_accrual_source_payment_application_line_entry import (
    BooksAccrualSourcePaymentApplicationLineEntry,
)
from mercury_banking.models.books_payment_application_accrual_adjustment import BooksPaymentApplicationAccrualAdjustment
from mercury_banking._runtime import ApiModel


class BooksAccrualSourcePaymentApplication(ApiModel):
    """BooksAccrualSourcePaymentApplication model."""

    adjustments: List[BooksPaymentApplicationAccrualAdjustment]
    line_entry: BooksAccrualSourcePaymentApplicationLineEntry = Field(alias="lineEntry")
    matched_amount: float = Field(alias="matchedAmount")
    payment_application_id: StrictStr = Field(alias="paymentApplicationId")
    source_type: StrictStr = Field(alias="sourceType")
    status: StrictStr
