# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.activity_option_enum import ActivityOptionEnum
from ebay_sell.post_order.models.response_history_attributes_type import ResponseHistoryAttributesType
from ebay_sell.post_order.models.return_state_enum import ReturnStateEnum
from ebay_sell.post_order.models.return_user_role_enum import ReturnUserRoleEnum
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ReturnResponseHistoryType(ApiModel):
    """ReturnResponseHistoryType model."""

    activity: Optional[ActivityOptionEnum] = None
    attributes: Optional[ResponseHistoryAttributesType] = None
    author: Optional[ReturnUserRoleEnum] = None
    creation_date: Optional[Timestamp] = Field(default=None, alias="creationDate")
    from_state: Optional[ReturnStateEnum] = Field(default=None, alias="fromState")
    notes: Optional[StrictStr] = None
    to_state: Optional[ReturnStateEnum] = Field(default=None, alias="toState")
