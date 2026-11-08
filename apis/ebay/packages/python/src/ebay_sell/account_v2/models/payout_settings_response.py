# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account_v2.models.payout_instrument import PayoutInstrument
from ebay_sell._runtime import ApiModel


class PayoutSettingsResponse(ApiModel):
    """PayoutSettingsResponse model."""

    payout_instruments: Optional[List[PayoutInstrument]] = Field(default=None, alias="payoutInstruments")
