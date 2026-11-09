# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.return_item_type import ReturnItemType
from ebay_sell.post_order.models.return_reason_type_enum import ReturnReasonTypeEnum
from ebay_sell.post_order.models.return_type_enum import ReturnTypeEnum
from ebay_sell.post_order.models.text import Text
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class ReturnCreationInfoType(ApiModel):
    """ReturnCreationInfoType model."""

    comments: Optional[Text] = None
    creation_date: Optional[Timestamp] = Field(default=None, alias="creationDate")
    item: Optional[ReturnItemType] = None
    reason: Optional[StrictStr] = None
    reason_type: Optional[ReturnReasonTypeEnum] = Field(default=None, alias="reasonType")
    type: Optional[ReturnTypeEnum] = None
