# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class OF21Response200OffersApplicablePricingVolumePrices(ApiModel):
    """OF21Response200OffersApplicablePricingVolumePrices model."""

    price: float
    quantity_threshold: StrictInt
    unit_discount_price: float
    unit_origin_price: float
