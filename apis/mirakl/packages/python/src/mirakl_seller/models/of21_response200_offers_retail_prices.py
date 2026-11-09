# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OF21Response200OffersRetailPrices(ApiModel):
    """OF21Response200OffersRetailPrices model."""

    discount_end_date: Optional[datetime] = None
    discount_start_date: Optional[datetime] = None
    price: float
    unit_discount_price: Optional[float] = None
    unit_origin_price: float
