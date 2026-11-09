# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking._runtime import ApiModel


class BooksAccrualSourceLine(ApiModel):
    """BooksAccrualSourceLine model."""

    account_id: StrictStr = Field(alias="accountId")
    accrual_source_id: StrictStr = Field(alias="accrualSourceId")
    amount: float
    description: StrictStr
    external_id: Optional[StrictStr] = Field(default=None, alias="externalId")
    id: StrictStr
    line_number: Annotated[int, Field(le=9223372036854776000, strict=True, ge=-9223372036854776000)] = Field(
        alias="lineNumber"
    )
