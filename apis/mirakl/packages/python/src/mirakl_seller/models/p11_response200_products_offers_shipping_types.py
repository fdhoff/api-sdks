# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.p11_response200_products_offers_shipping_types_delivery_time import (
    P11Response200ProductsOffersShippingTypesDeliveryTime,
)
from mirakl_seller._runtime import ApiModel


class P11Response200ProductsOffersShippingTypes(ApiModel):
    """P11Response200ProductsOffersShippingTypes model."""

    code: StrictStr
    cut_off_next_date: Optional[datetime] = None
    cut_off_time: Optional[StrictStr] = None
    delivery_time: Optional[P11Response200ProductsOffersShippingTypesDeliveryTime] = None
    label: StrictStr
    shipping_deadline: Optional[datetime] = None
    shipping_price_type: StrictStr
    shipping_price_unit: float
    shipping_zone_code: StrictStr
    shipping_zone_label: StrictStr
    standard_code: Optional[StrictStr] = None
