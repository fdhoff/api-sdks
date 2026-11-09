# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mercury_banking.models.treasury_dividend import TreasuryDividend
from mercury_banking.models.treasury_net_return_status import TreasuryNetReturnStatus
from mercury_banking._runtime import ApiModel


class TreasuryNetReturn(ApiModel):
    """TreasuryNetReturn model."""

    dividends: List[TreasuryDividend]
    month: date
    net_amount: Annotated[float, Field(multiple_of=0.01)] = Field(alias="netAmount")
    status: TreasuryNetReturnStatus
    treasury_fee: Annotated[float, Field(multiple_of=0.01)] = Field(alias="treasuryFee")
