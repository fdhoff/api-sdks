# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account_v2.models.update_payout_percentage import UpdatePayoutPercentage
from ebay_sell._runtime import ApiModel


class UpdatePayoutPercentageRequest(ApiModel):
    """UpdatePayoutPercentageRequest model."""

    payout_instruments: Optional[List[UpdatePayoutPercentage]] = Field(default=None, alias="payoutInstruments")
