# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.inventory.models.dimension import Dimension
from ebay_sell.inventory.models.weight import Weight
from ebay_sell._runtime import ApiModel


class PackageWeightAndSize(ApiModel):
    """PackageWeightAndSize model."""

    dimensions: Optional[Dimension] = None
    package_type: Optional[StrictStr] = Field(default=None, alias="packageType")
    shipping_irregular: Optional[StrictBool] = Field(default=None, alias="shippingIrregular")
    weight: Optional[Weight] = None
