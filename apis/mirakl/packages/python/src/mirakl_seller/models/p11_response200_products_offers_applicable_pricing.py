# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.p11_response200_products_offers_applicable_pricing_context import (
    P11Response200ProductsOffersApplicablePricingContext,
)
from mirakl_seller.models.p11_response200_products_offers_applicable_pricing_volume_prices import (
    P11Response200ProductsOffersApplicablePricingVolumePrices,
)
from mirakl_seller._runtime import ApiModel


class P11Response200ProductsOffersApplicablePricing(ApiModel):
    """P11Response200ProductsOffersApplicablePricing model."""

    channel_code: Optional[StrictStr] = None
    context: Optional[P11Response200ProductsOffersApplicablePricingContext] = None
    discount_end_date: Optional[datetime] = None
    discount_start_date: Optional[datetime] = None
    price: float
    unit_discount_price: Optional[float] = None
    unit_origin_price: float
    volume_prices: List[P11Response200ProductsOffersApplicablePricingVolumePrices]
