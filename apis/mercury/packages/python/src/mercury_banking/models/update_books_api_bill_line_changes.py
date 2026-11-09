# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.create_books_api_bill_line import CreateBooksAPIBillLine
from mercury_banking.models.update_books_api_bill_line import UpdateBooksAPIBillLine
from mercury_banking._runtime import ApiModel


class UpdateBooksAPIBillLineChanges(ApiModel):
    """UpdateBooksAPIBillLineChanges model."""

    create: Optional[List[CreateBooksAPIBillLine]] = None
    delete: Optional[List[StrictStr]] = None
    update: Optional[List[UpdateBooksAPIBillLine]] = None
