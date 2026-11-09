# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st01_response201_shipment_success_tracking_milestones_additional_info import (
    ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfo,
)
from mirakl_seller.models.st01_response201_shipment_success_tracking_milestones_occurrence_date import (
    ST01Response201ShipmentSuccessTrackingMilestonesOccurrenceDate,
)
from mirakl_seller._runtime import ApiModel


class ST01Response201ShipmentSuccessTrackingMilestones(ApiModel):
    """ST01Response201ShipmentSuccessTrackingMilestones model."""

    additional_info: Optional[ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfo] = None
    occurrence_date: Optional[ST01Response201ShipmentSuccessTrackingMilestonesOccurrenceDate] = None
    type: Optional[StrictStr] = None
