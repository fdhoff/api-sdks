# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from mercury_banking.models.books_line_entry_line_payment_application import BooksLineEntryLinePaymentApplication
from mercury_banking.models.books_line_entry_payment_application_source import BooksLineEntryPaymentApplicationSource
from typing import Union

BooksLineEntryPaymentApplication = Union[BooksLineEntryLinePaymentApplication, BooksLineEntryPaymentApplicationSource]
