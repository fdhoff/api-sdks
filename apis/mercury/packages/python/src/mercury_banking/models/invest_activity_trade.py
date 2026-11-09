# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.invest_activity_status import InvestActivityStatus
from mercury_banking.models.invest_activity_trade_action import InvestActivityTradeAction
from mercury_banking._runtime import ApiModel


class InvestActivityTrade(ApiModel):
    """InvestActivityTrade model."""

    action: InvestActivityTradeAction
    price: float
    quantity: StrictStr
    security: StrictStr
    status: InvestActivityStatus
    total: float
