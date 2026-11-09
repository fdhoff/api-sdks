# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.of22_response200_all_prices_context import OF22Response200AllPricesContext
from mirakl_seller.models.of22_response200_all_prices_volume_prices import OF22Response200AllPricesVolumePrices
from mirakl_seller._runtime import ApiModel


class OF22Response200AllPrices(ApiModel):
    """OF22Response200AllPrices model."""

    channel_code: Optional[StrictStr] = None
    context: Optional[OF22Response200AllPricesContext] = None
    discount_end_date: Optional[datetime] = None
    discount_start_date: Optional[datetime] = None
    price: float
    unit_discount_price: Optional[float] = None
    unit_origin_price: float
    volume_prices: List[OF22Response200AllPricesVolumePrices]
