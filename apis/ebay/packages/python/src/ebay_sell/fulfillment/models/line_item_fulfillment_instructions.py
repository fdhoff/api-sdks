# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class LineItemFulfillmentInstructions(ApiModel):
    """LineItemFulfillmentInstructions model."""

    guaranteed_delivery: Optional[StrictBool] = Field(default=None, alias="guaranteedDelivery")
    max_estimated_delivery_date: Optional[StrictStr] = Field(default=None, alias="maxEstimatedDeliveryDate")
    min_estimated_delivery_date: Optional[StrictStr] = Field(default=None, alias="minEstimatedDeliveryDate")
    ship_by_date: Optional[StrictStr] = Field(default=None, alias="shipByDate")
