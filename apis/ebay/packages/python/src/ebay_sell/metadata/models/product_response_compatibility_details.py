# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.property_filter_inner import PropertyFilterInner
from ebay_sell.metadata.models.property_values import PropertyValues
from ebay_sell._runtime import ApiModel


class ProductResponseCompatibilityDetails(ApiModel):
    """ProductResponseCompatibilityDetails model."""

    note_details: Optional[List[PropertyFilterInner]] = Field(default=None, alias="noteDetails")
    product_details: Optional[List[PropertyValues]] = Field(default=None, alias="productDetails")
