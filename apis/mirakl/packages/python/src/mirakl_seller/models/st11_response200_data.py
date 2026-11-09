# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st11_response200_data_payment_details import ST11Response200DataPaymentDetails
from mirakl_seller.models.st11_response200_data_shipment_additional_information import (
    ST11Response200DataShipmentAdditionalInformation,
)
from mirakl_seller.models.st11_response200_data_shipment_lines import ST11Response200DataShipmentLines
from mirakl_seller.models.st11_response200_data_shipping_from import ST11Response200DataShippingFrom
from mirakl_seller.models.st11_response200_data_tracking import ST11Response200DataTracking
from mirakl_seller._runtime import ApiModel


class ST11Response200Data(ApiModel):
    """ST11Response200Data model."""

    created_date: datetime
    id: StrictStr
    invoice_reference: Optional[StrictStr] = None
    last_updated_date: datetime
    order_id: StrictStr
    payment_details: Optional[ST11Response200DataPaymentDetails] = None
    shipment_additional_information: Optional[List[ST11Response200DataShipmentAdditionalInformation]] = None
    shipment_lines: Optional[List[ST11Response200DataShipmentLines]] = None
    shipped_date: Optional[datetime] = None
    shipping_from: Optional[ST11Response200DataShippingFrom] = None
    status: StrictStr
    status_customer_debit: StrictStr
    tracking: Optional[ST11Response200DataTracking] = None
