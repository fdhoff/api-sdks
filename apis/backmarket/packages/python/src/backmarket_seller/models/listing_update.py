# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.integer_or_string import IntegerOrString
from backmarket_seller.models.listing_price import ListingPrice
from backmarket_seller.models.listing_shipping_price import ListingShippingPrice
from backmarket_seller.models.shipper import Shipper
from backmarket_seller._runtime import ApiModel


class ListingUpdate(ApiModel):
    """ListingUpdate model."""

    price: Optional[ListingPrice] = None
    currency: Optional[StrictStr] = None
    comment: Optional[StrictStr] = None
    warranty_delay: Optional[IntegerOrString] = None
    quantity: Optional[IntegerOrString] = None
    shipper_1: Optional[Shipper] = None
    shipper_display_1: Optional[StrictStr] = None
    shipping_delay_1: Optional[StrictInt] = None
    shipping_price_1: Optional[ListingShippingPrice] = None
    shipper_2: Optional[Shipper] = None
    shipper_display_2: Optional[StrictStr] = None
    shipping_delay_2: Optional[StrictInt] = None
    shipping_price_2: Optional[ListingShippingPrice] = None
    shipper_3: Optional[Shipper] = None
    shipper_display_3: Optional[StrictStr] = None
    shipping_delay_3: Optional[StrictInt] = None
    shipping_price_3: Optional[ListingShippingPrice] = None
    min_price: Optional[ListingShippingPrice] = None
