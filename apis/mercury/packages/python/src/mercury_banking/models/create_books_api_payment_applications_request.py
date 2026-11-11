# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.books_api_payment_application import BooksAPIPaymentApplication
from mercury_banking.models.books_api_payment_application_adjustment import BooksAPIPaymentApplicationAdjustment
from mercury_banking._runtime import ApiModel


class CreateBooksAPIPaymentApplicationsRequest(ApiModel):
    """CreateBooksAPIPaymentApplicationsRequest model."""

    adjustments: Optional[List[BooksAPIPaymentApplicationAdjustment]] = None
    applications: Annotated[List[BooksAPIPaymentApplication], Field(min_length=1)]
