# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell.finances.models.balance_adjustment import BalanceAdjustment
from ebay_sell.finances.models.charge import Charge
from ebay_sell._runtime import ApiModel


class TransferDetail(ApiModel):
    """TransferDetail model."""

    balance_adjustment: Optional[BalanceAdjustment] = Field(default=None, alias="balanceAdjustment")
    charges: Optional[List[Charge]] = None
    total_charge_net_amount: Optional[Amount] = Field(default=None, alias="totalChargeNetAmount")
