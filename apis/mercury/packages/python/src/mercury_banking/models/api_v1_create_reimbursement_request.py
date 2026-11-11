# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking._runtime import ApiModel


class ApiV1CreateReimbursementRequest(ApiModel):
    """ApiV1CreateReimbursementRequest model."""

    amount: Annotated[float, Field(multiple_of=0.01)]
    category_id: Optional[UUID] = Field(default=None, alias="categoryId")
    currency: StrictStr
    date_paid_for: date = Field(alias="datePaidFor")
    merchant_name: Annotated[str, Field(min_length=1, strict=True, max_length=299)] = Field(alias="merchantName")
    notes: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=5000)]] = None
