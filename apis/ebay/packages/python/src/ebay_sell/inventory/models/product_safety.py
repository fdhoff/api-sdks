# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ProductSafety(ApiModel):
    """ProductSafety model."""

    component: Optional[StrictStr] = None
    pictograms: Optional[List[StrictStr]] = None
    statements: Optional[List[StrictStr]] = None
