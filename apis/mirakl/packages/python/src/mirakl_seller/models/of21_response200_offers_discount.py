# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.of21_response200_offers_discount_ranges import OF21Response200OffersDiscountRanges
from mirakl_seller._runtime import ApiModel


class OF21Response200OffersDiscount(ApiModel):
    """OF21Response200OffersDiscount model."""

    discount_price: Optional[float] = None
    end_date: Optional[datetime] = None
    origin_price: Optional[float] = None
    ranges: Optional[List[OF21Response200OffersDiscountRanges]] = None
    start_date: Optional[datetime] = None
