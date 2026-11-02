# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.product import Product
from backmarket_seller._runtime import ApiModel


class Snapshot(ApiModel):
    """Snapshot model."""

    id: Optional[StrictInt] = None
    product: Optional[Product] = None
    listing: Optional[StrictInt] = None
    sku: Optional[StrictStr] = None
    snowden: Optional[StrictBool] = None
    image: Optional[StrictStr] = None
