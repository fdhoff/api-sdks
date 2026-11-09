# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OF54Response200ExtFileStructurePricesVolumePrices(ApiModel):
    """OF54Response200ExtFileStructurePricesVolumePrices model."""

    quantity_threshold: Optional[StrictInt] = None
    unit_discount_price: Optional[float] = None
    unit_origin_price: Optional[float] = None
