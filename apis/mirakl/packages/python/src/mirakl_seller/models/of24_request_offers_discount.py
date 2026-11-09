# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.of24_request_offers_discount_ranges import OF24RequestOffersDiscountRanges
from mirakl_seller._runtime import ApiModel


class OF24RequestOffersDiscount(ApiModel):
    """OF24RequestOffersDiscount model."""

    end_date: Optional[StrictStr] = None
    price: Optional[float] = None
    ranges: Optional[List[OF24RequestOffersDiscountRanges]] = None
    start_date: Optional[StrictStr] = None
