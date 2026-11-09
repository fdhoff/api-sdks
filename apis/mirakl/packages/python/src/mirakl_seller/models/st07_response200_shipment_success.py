# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st07_response200_shipment_success_shipping_from import (
    ST07Response200ShipmentSuccessShippingFrom,
)
from mirakl_seller._runtime import ApiModel


class ST07Response200ShipmentSuccess(ApiModel):
    """ST07Response200ShipmentSuccess model."""

    id: Optional[StrictStr] = None
    shipping_from: Optional[ST07Response200ShipmentSuccessShippingFrom] = None
