# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.of54_response200_ext_file_structure_shipping_types_delivery_time import (
    OF54Response200ExtFileStructureShippingTypesDeliveryTime,
)
from mirakl_seller._runtime import ApiModel


class OF54Response200ExtFileStructureShippingTypes(ApiModel):
    """OF54Response200ExtFileStructureShippingTypes model."""

    code: Optional[StrictStr] = None
    delivery_time: Optional[OF54Response200ExtFileStructureShippingTypesDeliveryTime] = None
    shipping_price_additional_unit: Optional[float] = None
    shipping_price_type: Optional[StrictStr] = None
    shipping_price_unit: Optional[float] = None
    shipping_zone_code: Optional[StrictStr] = None
