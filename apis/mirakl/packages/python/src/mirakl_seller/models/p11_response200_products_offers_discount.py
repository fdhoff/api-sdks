# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.p11_response200_products_offers_discount_ranges import (
    P11Response200ProductsOffersDiscountRanges,
)
from mirakl_seller._runtime import ApiModel


class P11Response200ProductsOffersDiscount(ApiModel):
    """P11Response200ProductsOffersDiscount model."""

    discount_price: Optional[float] = None
    end_date: Optional[datetime] = None
    origin_price: Optional[float] = None
    ranges: Optional[List[P11Response200ProductsOffersDiscountRanges]] = None
    start_date: Optional[datetime] = None
