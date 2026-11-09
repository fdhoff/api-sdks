# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.money_movement_entries import MoneyMovementEntries
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell.post_order.models.user_party_enum import UserPartyEnum
from ebay_sell._runtime import ApiModel


class ClaimHistoryEventModel(ApiModel):
    """ClaimHistoryEventModel model."""

    action: Optional[StrictStr] = None
    actor: Optional[UserPartyEnum] = None
    var_date: Optional[Timestamp] = Field(default=None, alias="date")
    description: Optional[StrictStr] = None
    money_movement: Optional[MoneyMovementEntries] = Field(default=None, alias="moneyMovement")
