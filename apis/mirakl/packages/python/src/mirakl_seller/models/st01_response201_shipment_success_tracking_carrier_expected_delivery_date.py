# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st01_response201_shipment_success_tracking_carrier_expected_delivery_date_earliest import (
    ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDateEarliest,
)
from mirakl_seller.models.st01_response201_shipment_success_tracking_carrier_expected_delivery_date_latest import (
    ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDateLatest,
)
from mirakl_seller._runtime import ApiModel


class ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDate(ApiModel):
    """ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDate model."""

    earliest: Optional[ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDateEarliest] = None
    latest: Optional[ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDateLatest] = None
