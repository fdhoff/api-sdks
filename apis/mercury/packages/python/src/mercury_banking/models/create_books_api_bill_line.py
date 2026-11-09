# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking._runtime import ApiModel


class CreateBooksAPIBillLine(ApiModel):
    """CreateBooksAPIBillLine model."""

    amount: float
    description: StrictStr
    ledger_id: StrictStr = Field(alias="ledgerId")
