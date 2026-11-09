# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_api_bill import BooksAPIBill
from mercury_banking._runtime import ApiModel


class GetBooksAPIBillResponse(ApiModel):
    """GetBooksAPIBillResponse model."""

    bill: BooksAPIBill
