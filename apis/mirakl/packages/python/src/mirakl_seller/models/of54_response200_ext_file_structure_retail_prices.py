# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OF54Response200ExtFileStructureRetailPrices(ApiModel):
    """OF54Response200ExtFileStructureRetailPrices model."""

    discount_end_date: Optional[StrictStr] = None
    discount_price: Optional[float] = None
    discount_start_date: Optional[StrictStr] = None
    origin_price: Optional[float] = None
