# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mercury_banking.models.create_books_api_ledger import CreateBooksAPILedger
from mercury_banking._runtime import ApiModel


class CreateBooksAPILedgersRequest(ApiModel):
    """CreateBooksAPILedgersRequest model."""

    ledgers: Annotated[List[CreateBooksAPILedger], Field(min_length=1)]
