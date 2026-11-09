# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.appeal_grant_status_enum import AppealGrantStatusEnum
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell._runtime import ApiModel


class AppealDetails(ApiModel):
    """AppealDetails model."""

    appeal_close_reason_enum: Optional[StrictStr] = Field(default=None, alias="appealCloseReasonEnum")
    appeal_date: Optional[Timestamp] = Field(default=None, alias="appealDate")
    appeal_reason_code: Optional[StrictStr] = Field(default=None, alias="appealReasonCode")
    appeal_refund_amount: Optional[Amount] = Field(default=None, alias="appealRefundAmount")
    appeal_status: Optional[AppealGrantStatusEnum] = Field(default=None, alias="appealStatus")
    appeal_status_enum: Optional[StrictStr] = Field(default=None, alias="appealStatusEnum")
    eligible_for_appeal: Optional[StrictBool] = Field(default=None, alias="eligibleForAppeal")
