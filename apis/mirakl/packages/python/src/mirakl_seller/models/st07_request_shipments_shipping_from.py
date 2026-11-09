# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.st07_request_shipments_shipping_from_warehouse import (
    ST07RequestShipmentsShippingFromWarehouse,
)
from mirakl_seller._runtime import ApiModel


class ST07RequestShipmentsShippingFrom(ApiModel):
    """ST07RequestShipmentsShippingFrom model."""

    warehouse: ST07RequestShipmentsShippingFromWarehouse
