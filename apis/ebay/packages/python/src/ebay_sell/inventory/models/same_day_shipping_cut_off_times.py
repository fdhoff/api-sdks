# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.overrides import Overrides
from ebay_sell.inventory.models.weekly_schedule import WeeklySchedule
from ebay_sell._runtime import ApiModel


class SameDayShippingCutOffTimes(ApiModel):
    """SameDayShippingCutOffTimes model."""

    overrides: Optional[List[Overrides]] = None
    weekly_schedule: Optional[List[WeeklySchedule]] = Field(default=None, alias="weeklySchedule")
