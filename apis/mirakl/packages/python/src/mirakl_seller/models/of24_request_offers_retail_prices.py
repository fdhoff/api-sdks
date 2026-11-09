# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OF24RequestOffersRetailPrices(ApiModel):
    """OF24RequestOffersRetailPrices model."""

    discount_end_date: Optional[StrictStr] = None
    discount_start_date: Optional[StrictStr] = None
    unit_discount_price: Optional[float] = None
    unit_origin_price: Optional[float] = None
