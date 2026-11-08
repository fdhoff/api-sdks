# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ShippingCarrierRatePreferencesType(ApiModel):
    """ShippingCarrierRatePreferencesType model."""

    fedex_rate_option: Optional[StrictStr] = Field(default=None, alias="fedexRateOption")
    ups_rate_option: Optional[StrictStr] = Field(default=None, alias="upsRateOption")
