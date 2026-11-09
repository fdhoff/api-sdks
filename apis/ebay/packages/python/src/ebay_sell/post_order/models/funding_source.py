# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.funding_method_brand_enum import FundingMethodBrandEnum
from ebay_sell.post_order.models.funding_method_type_enum import FundingMethodTypeEnum
from ebay_sell._runtime import ApiModel


class FundingSource(ApiModel):
    """FundingSource model."""

    brand: Optional[FundingMethodBrandEnum] = None
    memo: Optional[StrictStr] = None
    type: Optional[FundingMethodTypeEnum] = None
