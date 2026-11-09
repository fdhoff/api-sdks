# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st07_response200_shipment_success_shipping_from_address import (
    ST07Response200ShipmentSuccessShippingFromAddress,
)
from mirakl_seller.models.st07_response200_shipment_success_shipping_from_warehouse import (
    ST07Response200ShipmentSuccessShippingFromWarehouse,
)
from mirakl_seller._runtime import ApiModel


class ST07Response200ShipmentSuccessShippingFrom(ApiModel):
    """ST07Response200ShipmentSuccessShippingFrom model."""

    address: Optional[ST07Response200ShipmentSuccessShippingFromAddress] = None
    warehouse: Optional[ST07Response200ShipmentSuccessShippingFromWarehouse] = None
