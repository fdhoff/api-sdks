# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.money import Money
from etsy_seller._runtime import ApiModel


class ShopShippingProfileDestination(ApiModel):
    """ShopShippingProfileDestination model."""

    shipping_profile_destination_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    shipping_profile_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    origin_country_iso: Optional[StrictStr] = None
    destination_country_iso: Optional[StrictStr] = None
    destination_region: Optional[StrictStr] = None
    primary_cost: Optional[Money] = None
    secondary_cost: Optional[Money] = None
    shipping_carrier_id: Optional[StrictInt] = None
    mail_class: Optional[StrictStr] = None
    min_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None
    max_delivery_days: Optional[Annotated[int, Field(le=45, strict=True, ge=1)]] = None
