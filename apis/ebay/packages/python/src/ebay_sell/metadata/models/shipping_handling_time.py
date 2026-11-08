# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ShippingHandlingTime(ApiModel):
    """ShippingHandlingTime model."""

    description: Optional[StrictStr] = None
    extended_handling: Optional[StrictBool] = Field(default=None, alias="extendedHandling")
    max_handling_time: Optional[StrictInt] = Field(default=None, alias="maxHandlingTime")
