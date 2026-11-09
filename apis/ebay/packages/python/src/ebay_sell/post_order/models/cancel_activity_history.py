# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.party_enum import PartyEnum
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class CancelActivityHistory(ApiModel):
    """CancelActivityHistory model."""

    action_date: Optional[Timestamp] = Field(default=None, alias="actionDate")
    activity_party: Optional[PartyEnum] = Field(default=None, alias="activityParty")
    activity_type: Optional[StrictStr] = Field(default=None, alias="activityType")
    state_from: Optional[StrictStr] = Field(default=None, alias="stateFrom")
    state_to: Optional[StrictStr] = Field(default=None, alias="stateTo")
