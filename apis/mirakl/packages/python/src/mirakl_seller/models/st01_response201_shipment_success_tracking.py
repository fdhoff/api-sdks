# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st01_response201_shipment_success_tracking_carrier_expected_delivery_date import (
    ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDate,
)
from mirakl_seller.models.st01_response201_shipment_success_tracking_last_known_location import (
    ST01Response201ShipmentSuccessTrackingLastKnownLocation,
)
from mirakl_seller.models.st01_response201_shipment_success_tracking_milestones import (
    ST01Response201ShipmentSuccessTrackingMilestones,
)
from mirakl_seller._runtime import ApiModel


class ST01Response201ShipmentSuccessTracking(ApiModel):
    """ST01Response201ShipmentSuccessTracking model."""

    carrier_code: Optional[StrictStr] = None
    carrier_expected_delivery_date: Optional[ST01Response201ShipmentSuccessTrackingCarrierExpectedDeliveryDate] = None
    carrier_name: Optional[StrictStr] = None
    carrier_standard_code: Optional[StrictStr] = None
    last_known_location: Optional[ST01Response201ShipmentSuccessTrackingLastKnownLocation] = None
    milestones: Optional[List[ST01Response201ShipmentSuccessTrackingMilestones]] = None
    tracking_number: Optional[StrictStr] = None
    tracking_url: Optional[StrictStr] = None
    validity_status: Optional[StrictStr] = None
