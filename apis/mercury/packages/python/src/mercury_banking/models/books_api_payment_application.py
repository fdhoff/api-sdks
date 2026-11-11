# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_api_payment_application_adjustment import BooksAPIPaymentApplicationAdjustment
from mercury_banking._runtime import ApiModel


class BooksAPIPaymentApplication(ApiModel):
    """BooksAPIPaymentApplication model."""

    adjustments: Optional[List[BooksAPIPaymentApplicationAdjustment]] = None
    amount: float
    bill_id: Optional[StrictStr] = Field(default=None, alias="billId")
    invoice_id: Optional[StrictStr] = Field(default=None, alias="invoiceId")
