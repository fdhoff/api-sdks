# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.sh11_response200_shipping_zones import SH11Response200ShippingZones
from mirakl_seller._runtime import ApiModel


class SH11Response200(ApiModel):
    """SH11Response200 model."""

    shipping_zones: List[SH11Response200ShippingZones]
