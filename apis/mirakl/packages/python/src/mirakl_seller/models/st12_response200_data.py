# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st12_response200_data_fulfillment import ST12Response200DataFulfillment
from mirakl_seller.models.st12_response200_data_references import ST12Response200DataReferences
from mirakl_seller.models.st12_response200_data_shipment_lines import ST12Response200DataShipmentLines
from mirakl_seller.models.st12_response200_data_shipping_address import ST12Response200DataShippingAddress
from mirakl_seller._runtime import ApiModel


class ST12Response200Data(ApiModel):
    """ST12Response200Data model."""

    fulfillment: Optional[ST12Response200DataFulfillment] = None
    order_id: StrictStr
    references: Optional[ST12Response200DataReferences] = None
    shipment_lines: Optional[List[ST12Response200DataShipmentLines]] = None
    shipping_address: ST12Response200DataShippingAddress
    shipping_date: datetime
    shipping_deadline: Optional[datetime] = None
    shipping_type_code: StrictStr
    shipping_type_standard_code: Optional[StrictStr] = None
