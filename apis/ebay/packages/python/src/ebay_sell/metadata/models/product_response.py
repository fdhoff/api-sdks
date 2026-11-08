# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.metadata.models.pagination import Pagination
from ebay_sell.metadata.models.product_response_compatibility_details import ProductResponseCompatibilityDetails
from ebay_sell._runtime import ApiModel


class ProductResponse(ApiModel):
    """ProductResponse model."""

    compatibility_details: Optional[List[ProductResponseCompatibilityDetails]] = Field(
        default=None, alias="compatibilityDetails"
    )
    pagination: Optional[Pagination] = None
