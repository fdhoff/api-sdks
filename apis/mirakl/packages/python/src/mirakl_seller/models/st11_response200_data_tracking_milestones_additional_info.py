# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st11_response200_data_tracking_milestones_additional_info_occurrence_date import (
    ST11Response200DataTrackingMilestonesAdditionalInfoOccurrenceDate,
)
from mirakl_seller._runtime import ApiModel


class ST11Response200DataTrackingMilestonesAdditionalInfo(ApiModel):
    """ST11Response200DataTrackingMilestonesAdditionalInfo model."""

    occurrence_date: Optional[ST11Response200DataTrackingMilestonesAdditionalInfoOccurrenceDate] = None
    type: Optional[StrictStr] = None
