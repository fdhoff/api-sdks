# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.shop_shipping_profile_destination import ShopShippingProfileDestination
from etsy_seller.models.shop_shipping_profile_upgrade import ShopShippingProfileUpgrade
from etsy_seller._runtime import ApiModel


class ShopShippingProfile(ApiModel):
    """ShopShippingProfile model."""

    shipping_profile_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    title: Optional[StrictStr] = None
    user_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    origin_country_iso: Optional[StrictStr] = None
    is_deleted: Optional[StrictBool] = None
    shipping_profile_destinations: Optional[List[ShopShippingProfileDestination]] = None
    shipping_profile_upgrades: Optional[List[ShopShippingProfileUpgrade]] = None
    origin_postal_code: Optional[StrictStr] = None
    profile_type: Optional[StrictStr] = "manual"
    domestic_handling_fee: Optional[Annotated[float, Field(ge=0)]] = 0
    international_handling_fee: Optional[Annotated[float, Field(ge=0)]] = 0
