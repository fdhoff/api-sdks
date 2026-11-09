# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_line_entry_line_payment_application_accrual_source import (
    BooksLineEntryLinePaymentApplicationAccrualSource,
)
from mercury_banking._runtime import ApiModel


class BooksLineEntryLinePaymentApplication(ApiModel):
    """BooksLineEntryLinePaymentApplication model."""

    accrual_source: BooksLineEntryLinePaymentApplicationAccrualSource = Field(alias="accrualSource")
    line_payment_application_id: StrictStr = Field(alias="linePaymentApplicationId")
    matched_amount: float = Field(alias="matchedAmount")
    source_type: StrictStr = Field(alias="sourceType")
    status: StrictStr
