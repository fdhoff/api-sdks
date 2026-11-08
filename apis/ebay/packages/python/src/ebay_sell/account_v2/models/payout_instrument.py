# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class PayoutInstrument(ApiModel):
    """PayoutInstrument model."""

    account_last_four_digits: Optional[StrictStr] = Field(default=None, alias="accountLastFourDigits")
    instrument_id: Optional[StrictStr] = Field(default=None, alias="instrumentId")
    instrument_status: Optional[StrictStr] = Field(default=None, alias="instrumentStatus")
    instrument_type: Optional[StrictStr] = Field(default=None, alias="instrumentType")
    nickname: Optional[StrictStr] = None
    payout_percentage: Optional[StrictStr] = Field(default=None, alias="payoutPercentage")
