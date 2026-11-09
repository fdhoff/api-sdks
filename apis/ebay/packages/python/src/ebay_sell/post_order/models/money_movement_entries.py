# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.money_movement_entry import MoneyMovementEntry
from ebay_sell._runtime import ApiModel


class MoneyMovementEntries(ApiModel):
    """MoneyMovementEntries model."""

    money_movement_entry_list: Optional[List[MoneyMovementEntry]] = Field(default=None, alias="moneyMovementEntryList")
