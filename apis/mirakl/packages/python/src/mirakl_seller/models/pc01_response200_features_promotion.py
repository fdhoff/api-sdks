# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class PC01Response200FeaturesPromotion(ApiModel):
    """PC01Response200FeaturesPromotion model."""

    cart_promotion_campaign: StrictBool
    discount_campaign: StrictBool
    seller_promotion: StrictBool
