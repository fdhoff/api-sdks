# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.activity_option_enum import ActivityOptionEnum
from ebay_sell._runtime import ApiModel


class AvailableOptionType(ApiModel):
    """AvailableOptionType model."""

    action_type: Optional[ActivityOptionEnum] = Field(default=None, alias="actionType")
    action_url: Optional[StrictStr] = Field(default=None, alias="actionURL")
