# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from backmarket_seller._runtime import ApiModel


class ListingPublicShippingsInner(ApiModel):
    """ListingPublicShippingsInner model."""

    country_code: StrictStr
    shipper: StrictStr
    shipper_display: StrictStr
    shipping_delay: StrictInt
    shipping_price: StrictStr
