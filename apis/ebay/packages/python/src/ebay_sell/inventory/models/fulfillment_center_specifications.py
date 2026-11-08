# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.same_day_shipping_cut_off_times import SameDayShippingCutOffTimes
from ebay_sell._runtime import ApiModel


class FulfillmentCenterSpecifications(ApiModel):
    """FulfillmentCenterSpecifications model."""

    same_day_shipping_cut_off_times: Optional[SameDayShippingCutOffTimes] = Field(
        default=None, alias="sameDayShippingCutOffTimes"
    )
