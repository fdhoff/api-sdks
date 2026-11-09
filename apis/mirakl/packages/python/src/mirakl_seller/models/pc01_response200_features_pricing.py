# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class PC01Response200FeaturesPricing(ApiModel):
    """PC01Response200FeaturesPricing model."""

    channel_pricing: StrictStr
    discount_period_required: StrictBool
    discount_price_creation_in_the_past_blocked: StrictBool
    scheduled_pricing: StrictBool
    volume_discount: StrictBool
    volume_pricing: StrictBool
