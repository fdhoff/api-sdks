# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking._runtime import ApiModel


class BooksAPICashFlowLedgerRow(ApiModel):
    """BooksAPICashFlowLedgerRow model."""

    children: List[BooksAPICashFlowLedgerRow]
    ledger_id: StrictStr = Field(alias="ledgerId")
    name: StrictStr
    net_cash_flows: List[float] = Field(alias="netCashFlows")
    parent_id: Optional[StrictStr] = Field(default=None, alias="parentId")
    total_net_cash_flows: List[float] = Field(alias="totalNetCashFlows")


BooksAPICashFlowLedgerRow.model_rebuild(raise_errors=False)
