# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st11_response200_data_tracking_milestones_additional_info import (
    ST11Response200DataTrackingMilestonesAdditionalInfo,
)
from mirakl_seller.models.st11_response200_data_tracking_milestones_occurrence_date import (
    ST11Response200DataTrackingMilestonesOccurrenceDate,
)
from mirakl_seller._runtime import ApiModel


class ST11Response200DataTrackingMilestones(ApiModel):
    """ST11Response200DataTrackingMilestones model."""

    additional_info: Optional[ST11Response200DataTrackingMilestonesAdditionalInfo] = None
    occurrence_date: Optional[ST11Response200DataTrackingMilestonesOccurrenceDate] = None
    type: Optional[StrictStr] = None
