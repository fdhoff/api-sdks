# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st01_response201_shipment_success_payment_details import (
    ST01Response201ShipmentSuccessPaymentDetails,
)
from mirakl_seller.models.st01_response201_shipment_success_shipment_additional_information import (
    ST01Response201ShipmentSuccessShipmentAdditionalInformation,
)
from mirakl_seller.models.st01_response201_shipment_success_shipment_lines import (
    ST01Response201ShipmentSuccessShipmentLines,
)
from mirakl_seller.models.st01_response201_shipment_success_shipping_from import (
    ST01Response201ShipmentSuccessShippingFrom,
)
from mirakl_seller.models.st01_response201_shipment_success_tracking import ST01Response201ShipmentSuccessTracking
from mirakl_seller._runtime import ApiModel


class ST01Response201ShipmentSuccess(ApiModel):
    """ST01Response201ShipmentSuccess model."""

    created_date: datetime
    id: StrictStr
    invoice_reference: Optional[StrictStr] = None
    last_updated_date: datetime
    order_id: StrictStr
    payment_details: Optional[ST01Response201ShipmentSuccessPaymentDetails] = None
    shipment_additional_information: Optional[List[ST01Response201ShipmentSuccessShipmentAdditionalInformation]] = None
    shipment_lines: Optional[List[ST01Response201ShipmentSuccessShipmentLines]] = None
    shipped_date: Optional[datetime] = None
    shipping_from: Optional[ST01Response201ShipmentSuccessShippingFrom] = None
    status: StrictStr
    status_customer_debit: StrictStr
    tracking: Optional[ST01Response201ShipmentSuccessTracking] = None
