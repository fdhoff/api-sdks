# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mirakl_seller.models.st01_request_shipments_shipment_additional_information import (
    ST01RequestShipmentsShipmentAdditionalInformation,
)
from mirakl_seller.models.st01_request_shipments_shipment_lines import ST01RequestShipmentsShipmentLines
from mirakl_seller.models.st01_request_shipments_shipping_from import ST01RequestShipmentsShippingFrom
from mirakl_seller.models.st01_request_shipments_tracking import ST01RequestShipmentsTracking
from mirakl_seller._runtime import ApiModel


class ST01RequestShipments(ApiModel):
    """ST01RequestShipments model."""

    invoice_reference: Optional[Annotated[str, Field(min_length=0, strict=True, max_length=255)]] = None
    order_id: Annotated[str, Field(min_length=1, strict=True, max_length=2147483647)]
    shipment_additional_information: Optional[List[ST01RequestShipmentsShipmentAdditionalInformation]] = None
    shipment_lines: Annotated[List[ST01RequestShipmentsShipmentLines], Field(min_length=1, max_length=2147483647)]
    shipped: Optional[StrictBool] = False
    shipping_from: Optional[ST01RequestShipmentsShippingFrom] = None
    tracking: Optional[ST01RequestShipmentsTracking] = None
