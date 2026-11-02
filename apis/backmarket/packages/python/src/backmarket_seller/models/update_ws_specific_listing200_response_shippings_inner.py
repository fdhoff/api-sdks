# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List
from backmarket_seller._runtime import ApiModel


class UpdateWsSpecificListing200ResponseShippingsInner(ApiModel):
    """UpdateWsSpecificListing200ResponseShippingsInner model."""

    shipping_price: StrictStr
    shipping_delay: StrictInt
    shipper: StrictStr
    shipper_display: StrictStr
    country_code: StrictStr
