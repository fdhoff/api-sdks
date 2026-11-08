# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class Rate(ApiModel):
    """Rate model."""

    count: Optional[StrictInt] = None
    limit: Optional[StrictInt] = None
    remaining: Optional[StrictInt] = None
    reset: Optional[StrictStr] = None
    time_window: Optional[StrictInt] = Field(default=None, alias="timeWindow")
