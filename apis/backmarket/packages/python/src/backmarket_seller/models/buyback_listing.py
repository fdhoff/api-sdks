# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from backmarket_seller.models.buyback_aesthetic_grade_code import BuybackAestheticGradeCode
from backmarket_seller.models.monetary_amount import MonetaryAmount
from backmarket_seller._runtime import ApiModel


class BuybackListing(ApiModel):
    """BuybackListing model."""

    id: UUID
    product_id: UUID = Field(alias="productId")
    prices: Dict[str, MonetaryAmount]
    aesthetic_grade_code: BuybackAestheticGradeCode = Field(alias="aestheticGradeCode")
    sku: Optional[StrictStr]
    markets: List[Annotated[str, Field(strict=True)]]
