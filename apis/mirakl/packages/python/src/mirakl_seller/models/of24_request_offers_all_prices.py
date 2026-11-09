# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.of24_request_offers_all_prices_volume_prices import OF24RequestOffersAllPricesVolumePrices
from mirakl_seller._runtime import ApiModel


class OF24RequestOffersAllPrices(ApiModel):
    """OF24RequestOffersAllPrices model."""

    channel_code: Optional[StrictStr] = None
    discount_end_date: Optional[StrictStr] = None
    discount_start_date: Optional[StrictStr] = None
    unit_discount_price: Optional[float] = None
    unit_origin_price: Optional[float] = None
    volume_prices: Optional[List[OF24RequestOffersAllPricesVolumePrices]] = None
