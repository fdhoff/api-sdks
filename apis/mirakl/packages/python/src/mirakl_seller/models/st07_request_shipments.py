# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.st07_request_shipments_shipping_from import ST07RequestShipmentsShippingFrom
from mirakl_seller._runtime import ApiModel


class ST07RequestShipments(ApiModel):
    """ST07RequestShipments model."""

    id: StrictStr
    shipping_from: ST07RequestShipmentsShippingFrom
