# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st01_response201_shipment_success_tracking_milestones_additional_info_occurrence_date import (
    ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfoOccurrenceDate,
)
from mirakl_seller._runtime import ApiModel


class ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfo(ApiModel):
    """ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfo model."""

    occurrence_date: Optional[ST01Response201ShipmentSuccessTrackingMilestonesAdditionalInfoOccurrenceDate] = None
    type: Optional[StrictStr] = None
