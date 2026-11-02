# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.buyback_listing_grade import BuybackListingGrade
from backmarket_seller._runtime import ApiModel


class BuybackOrderListing(ApiModel):
    """BuybackOrderListing model."""

    sku: Optional[StrictStr] = None
    product_id: float = Field(alias="productId")
    title: StrictStr
    grade: BuybackListingGrade
