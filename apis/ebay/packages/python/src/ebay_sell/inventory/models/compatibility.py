# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.compatible_product import CompatibleProduct
from ebay_sell._runtime import ApiModel


class Compatibility(ApiModel):
    """Compatibility model."""

    compatible_products: Optional[List[CompatibleProduct]] = Field(default=None, alias="compatibleProducts")
    sku: Optional[StrictStr] = None
