# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.activity_option_enum import ActivityOptionEnum
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ReturnResponseDueType(ApiModel):
    """ReturnResponseDueType model."""

    activity_due: Optional[ActivityOptionEnum] = Field(default=None, alias="activityDue")
    respond_by_date: Optional[Timestamp] = Field(default=None, alias="respondByDate")
