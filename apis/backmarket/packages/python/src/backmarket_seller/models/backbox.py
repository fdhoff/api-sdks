# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from backmarket_seller.models.product_condition import ProductCondition
from backmarket_seller._runtime import ApiModel


class Backbox(ApiModel):
    """Backbox model."""

    product: StrictInt
    sku: StrictStr
    price: float
    quantity: StrictInt
    buybox: StrictBool
    price_for_buybox: float
    currency: StrictStr
    condition: ProductCondition
    same_merchant_winner: StrictBool
