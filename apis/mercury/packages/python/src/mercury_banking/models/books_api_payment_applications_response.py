# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_api_payment_application_accrual_source import BooksAPIPaymentApplicationAccrualSource
from mercury_banking.models.books_api_payment_application_line_entry import BooksAPIPaymentApplicationLineEntry
from mercury_banking._runtime import ApiModel


class BooksAPIPaymentApplicationsResponse(ApiModel):
    """BooksAPIPaymentApplicationsResponse model."""

    bills: List[BooksAPIPaymentApplicationAccrualSource]
    invoices: List[BooksAPIPaymentApplicationAccrualSource]
    line_entry: BooksAPIPaymentApplicationLineEntry = Field(alias="lineEntry")
