# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st01_request_shipments_shipping_from_warehouse import (
    ST01RequestShipmentsShippingFromWarehouse,
)
from mirakl_seller._runtime import ApiModel


class ST01RequestShipmentsShippingFrom(ApiModel):
    """ST01RequestShipmentsShippingFrom model."""

    warehouse: Optional[ST01RequestShipmentsShippingFromWarehouse] = None
