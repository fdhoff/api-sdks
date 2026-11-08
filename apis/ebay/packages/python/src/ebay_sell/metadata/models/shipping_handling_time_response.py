# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.shipping_handling_time import ShippingHandlingTime
from ebay_sell._runtime import ApiModel


class ShippingHandlingTimeResponse(ApiModel):
    """ShippingHandlingTimeResponse model."""

    handling_times: Optional[List[ShippingHandlingTime]] = Field(default=None, alias="handlingTimes")
