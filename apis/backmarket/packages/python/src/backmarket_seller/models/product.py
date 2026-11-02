# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.category3 import Category3
from backmarket_seller._runtime import ApiModel


class Product(ApiModel):
    """Product model."""

    product_id: Optional[StrictInt] = None
    category_3: Optional[Category3] = None
