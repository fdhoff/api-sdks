# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feed.models.user_schedule_response import UserScheduleResponse
from ebay_sell._runtime import ApiModel


class UserScheduleCollection(ApiModel):
    """UserScheduleCollection model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    schedules: Optional[List[UserScheduleResponse]] = None
    total: Optional[StrictInt] = None
