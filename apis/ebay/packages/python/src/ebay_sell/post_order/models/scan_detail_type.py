# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ScanDetailType(ApiModel):
    """ScanDetailType model."""

    event_city: Optional[StrictStr] = Field(default=None, alias="eventCity")
    event_code: Optional[StrictStr] = Field(default=None, alias="eventCode")
    event_desc: Optional[StrictStr] = Field(default=None, alias="eventDesc")
    event_postal_code: Optional[StrictStr] = Field(default=None, alias="eventPostalCode")
    event_state_or_province: Optional[StrictStr] = Field(default=None, alias="eventStateOrProvince")
    event_status: Optional[StrictStr] = Field(default=None, alias="eventStatus")
    event_time: Optional[Timestamp] = Field(default=None, alias="eventTime")
