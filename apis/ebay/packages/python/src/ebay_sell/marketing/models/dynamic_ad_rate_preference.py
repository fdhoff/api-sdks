# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class DynamicAdRatePreference(ApiModel):
    """DynamicAdRatePreference model."""

    ad_rate_adjustment_percent: Optional[StrictStr] = Field(default=None, alias="adRateAdjustmentPercent")
    ad_rate_cap_percent: Optional[StrictStr] = Field(default=None, alias="adRateCapPercent")
