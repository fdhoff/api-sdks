# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.treasury_txn import TreasuryTxn
from mercury_banking._runtime import ApiModel


class TreasuryTransactionsResponse(ApiModel):
    """TreasuryTransactionsResponse model."""

    cursor: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    transactions: List[TreasuryTxn]
