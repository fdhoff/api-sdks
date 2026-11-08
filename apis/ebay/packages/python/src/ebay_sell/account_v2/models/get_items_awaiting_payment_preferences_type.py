# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class GetItemsAwaitingPaymentPreferencesType(ApiModel):
    """GetItemsAwaitingPaymentPreferencesType model."""

    auto_relist: Optional[StrictBool] = Field(default=None, alias="autoRelist")
    delay_before_cancelling_commitment: Optional[StrictInt] = Field(
        default=None, alias="delayBeforeCancellingCommitment"
    )
    excluded_users: Optional[List[StrictStr]] = Field(default=None, alias="excludedUsers")
    opt_in_status: Optional[StrictBool] = Field(default=None, alias="optInStatus")
