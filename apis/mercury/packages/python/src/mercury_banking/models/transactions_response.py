# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mercury_banking.models.transaction import Transaction
from mercury_banking._runtime import ApiModel


class TransactionsResponse(ApiModel):
    """TransactionsResponse model."""

    total: Annotated[int, Field(le=9223372036854776000, strict=True, ge=-9223372036854776000)]
    transactions: List[Transaction]
