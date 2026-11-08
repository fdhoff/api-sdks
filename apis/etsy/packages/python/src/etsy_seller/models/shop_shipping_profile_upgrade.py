# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.money import Money
from etsy_seller._runtime import ApiModel


class ShopShippingProfileUpgrade(ApiModel):
    """ShopShippingProfileUpgrade model."""

    shipping_profile_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    upgrade_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    upgrade_name: Optional[StrictStr] = None
    type: Optional[StrictInt] = None
    rank: Optional[Annotated[int, Field(strict=True, ge=0)]] = None
    language: Optional[StrictStr] = None
    price: Optional[Money] = None
    secondary_price: Optional[Money] = None
    shipping_carrier_id: Optional[StrictInt] = None
    mail_class: Optional[StrictStr] = None
    min_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None
    max_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None
