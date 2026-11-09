# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.of21_response200_offers_applicable_pricing_context import (
    OF21Response200OffersApplicablePricingContext,
)
from mirakl_seller.models.of21_response200_offers_applicable_pricing_volume_prices import (
    OF21Response200OffersApplicablePricingVolumePrices,
)
from mirakl_seller._runtime import ApiModel


class OF21Response200OffersApplicablePricing(ApiModel):
    """OF21Response200OffersApplicablePricing model."""

    channel_code: Optional[StrictStr] = None
    context: Optional[OF21Response200OffersApplicablePricingContext] = None
    discount_end_date: Optional[datetime] = None
    discount_start_date: Optional[datetime] = None
    price: float
    unit_discount_price: Optional[float] = None
    unit_origin_price: float
    volume_prices: List[OF21Response200OffersApplicablePricingVolumePrices]
