# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ProposedBid(ApiModel):
    """ProposedBid model."""

    currency: Optional[StrictStr] = None
    range_end: Optional[StrictStr] = Field(default=None, alias="rangeEnd")
    range_start: Optional[StrictStr] = Field(default=None, alias="rangeStart")
    value: Optional[StrictStr] = None
