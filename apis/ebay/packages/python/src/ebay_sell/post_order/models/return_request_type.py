# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.request_type_enum import RequestTypeEnum
from ebay_sell.post_order.models.return_type_enum import ReturnTypeEnum
from ebay_sell.post_order.models.text import Text
from ebay_sell._runtime import ApiModel


class ReturnRequestType(ApiModel):
    """ReturnRequestType model."""

    carrier: Optional[StrictStr] = None
    comments: Optional[Text] = None
    item_id: Optional[StrictStr] = Field(default=None, alias="itemId")
    reason: Optional[StrictStr] = None
    request_type: Optional[RequestTypeEnum] = Field(default=None, alias="requestType")
    return_quantity: Optional[StrictInt] = Field(default=None, alias="returnQuantity")
    transaction_id: Optional[StrictStr] = Field(default=None, alias="transactionId")
    type: Optional[ReturnTypeEnum] = None
