# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st01_response201_shipment_success_shipping_from_address import (
    ST01Response201ShipmentSuccessShippingFromAddress,
)
from mirakl_seller.models.st01_response201_shipment_success_shipping_from_warehouse import (
    ST01Response201ShipmentSuccessShippingFromWarehouse,
)
from mirakl_seller._runtime import ApiModel


class ST01Response201ShipmentSuccessShippingFrom(ApiModel):
    """ST01Response201ShipmentSuccessShippingFrom model."""

    address: Optional[ST01Response201ShipmentSuccessShippingFromAddress] = None
    warehouse: Optional[ST01Response201ShipmentSuccessShippingFromWarehouse] = None
