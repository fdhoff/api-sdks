# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class ProductFamilyProperties(ApiModel):
    """ProductFamilyProperties model."""

    engine: Optional[StrictStr] = None
    make: Optional[StrictStr] = None
    model: Optional[StrictStr] = None
    trim: Optional[StrictStr] = None
    year: Optional[StrictStr] = None
