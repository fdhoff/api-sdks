# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_line_entry_payment_application_accrual_source import (
    BooksLineEntryPaymentApplicationAccrualSource,
)
from mercury_banking.models.books_payment_application_accrual_adjustment import BooksPaymentApplicationAccrualAdjustment
from mercury_banking._runtime import ApiModel


class BooksLineEntryPaymentApplicationSource(ApiModel):
    """BooksLineEntryPaymentApplicationSource model."""

    accrual_source: Optional[BooksLineEntryPaymentApplicationAccrualSource] = Field(default=None, alias="accrualSource")
    adjustments: List[BooksPaymentApplicationAccrualAdjustment]
    matched_amount: float = Field(alias="matchedAmount")
    payment_application_id: StrictStr = Field(alias="paymentApplicationId")
    source_type: StrictStr = Field(alias="sourceType")
    status: StrictStr
