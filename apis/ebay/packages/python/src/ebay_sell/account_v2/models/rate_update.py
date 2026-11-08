# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.account_v2.models.amount import Amount
from ebay_sell._runtime import ApiModel


class RateUpdate(ApiModel):
    """RateUpdate model."""

    additional_cost: Optional[Amount] = Field(default=None, alias="additionalCost")
    rate_id: Optional[StrictStr] = Field(default=None, alias="rateId")
    shipping_cost: Optional[Amount] = Field(default=None, alias="shippingCost")
