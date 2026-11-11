# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_api_invoice import BooksAPIInvoice
from mercury_banking._runtime import ApiModel


class GetBooksAPIInvoiceResponse(ApiModel):
    """GetBooksAPIInvoiceResponse model."""

    invoice: BooksAPIInvoice
