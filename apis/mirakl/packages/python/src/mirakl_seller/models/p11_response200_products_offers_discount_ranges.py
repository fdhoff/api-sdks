# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class P11Response200ProductsOffersDiscountRanges(ApiModel):
    """P11Response200ProductsOffersDiscountRanges model."""

    price: float
    quantity_threshold: StrictInt
