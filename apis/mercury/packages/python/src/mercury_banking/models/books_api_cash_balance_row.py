# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking._runtime import ApiModel


class BooksAPICashBalanceRow(ApiModel):
    """BooksAPICashBalanceRow model."""

    balances: List[float]
    children: List[BooksAPICashBalanceRow]
    ledger_id: StrictStr = Field(alias="ledgerId")
    name: StrictStr
    parent_id: Optional[StrictStr] = Field(default=None, alias="parentId")
    sort_code: StrictStr = Field(alias="sortCode")
    total_balances: List[float] = Field(alias="totalBalances")


BooksAPICashBalanceRow.model_rebuild(raise_errors=False)
