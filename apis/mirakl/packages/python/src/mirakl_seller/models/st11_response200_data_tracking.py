# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st11_response200_data_tracking_carrier_expected_delivery_date import (
    ST11Response200DataTrackingCarrierExpectedDeliveryDate,
)
from mirakl_seller.models.st11_response200_data_tracking_last_known_location import (
    ST11Response200DataTrackingLastKnownLocation,
)
from mirakl_seller.models.st11_response200_data_tracking_milestones import ST11Response200DataTrackingMilestones
from mirakl_seller._runtime import ApiModel


class ST11Response200DataTracking(ApiModel):
    """ST11Response200DataTracking model."""

    carrier_code: Optional[StrictStr] = None
    carrier_expected_delivery_date: Optional[ST11Response200DataTrackingCarrierExpectedDeliveryDate] = None
    carrier_name: Optional[StrictStr] = None
    carrier_scac_code: Optional[StrictStr] = None
    carrier_standard_code: Optional[StrictStr] = None
    last_known_location: Optional[ST11Response200DataTrackingLastKnownLocation] = None
    milestones: Optional[List[ST11Response200DataTrackingMilestones]] = None
    tracking_number: Optional[StrictStr] = None
    tracking_url: Optional[StrictStr] = None
    validity_status: Optional[StrictStr] = None
