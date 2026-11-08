# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class FormatAllocation(ApiModel):
    """FormatAllocation model."""

    auction: Optional[StrictInt] = None
    fixed_price: Optional[StrictInt] = Field(default=None, alias="fixedPrice")
