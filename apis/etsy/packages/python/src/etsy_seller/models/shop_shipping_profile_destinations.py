# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.shop_shipping_profile_destination import ShopShippingProfileDestination
from etsy_seller._runtime import ApiModel


class ShopShippingProfileDestinations(ApiModel):
    """ShopShippingProfileDestinations model."""

    count: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    results: Optional[List[ShopShippingProfileDestination]] = None
