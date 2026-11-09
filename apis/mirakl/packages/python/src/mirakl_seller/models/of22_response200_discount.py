# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.of22_response200_discount_ranges import OF22Response200DiscountRanges
from mirakl_seller._runtime import ApiModel


class OF22Response200Discount(ApiModel):
    """OF22Response200Discount model."""

    discount_price: Optional[float] = None
    end_date: Optional[datetime] = None
    origin_price: Optional[float] = None
    ranges: Optional[List[OF22Response200DiscountRanges]] = None
    start_date: Optional[datetime] = None
