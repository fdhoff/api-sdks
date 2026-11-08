# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from etsy_seller.models.money import Money
from etsy_seller._runtime import ApiModel


class ListingBuyerPrice(ApiModel):
    """ListingBuyerPrice model."""

    base_price: Optional[Money] = None
    shipping_cost: Optional[Money] = None
    is_free_shipping: Optional[StrictBool] = None
    original_price: Optional[Money] = None
    discounted_price: Optional[Money] = None
    discount_amount: Optional[Money] = None
    discount_percentage: Optional[StrictInt] = None
    has_discount: Optional[StrictBool] = None
    discount_start_epoch: Optional[StrictInt] = None
    discount_end_epoch: Optional[StrictInt] = None
