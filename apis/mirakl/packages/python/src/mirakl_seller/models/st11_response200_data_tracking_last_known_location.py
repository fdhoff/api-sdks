# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st11_response200_data_tracking_last_known_location_occurrence_date import (
    ST11Response200DataTrackingLastKnownLocationOccurrenceDate,
)
from mirakl_seller._runtime import ApiModel


class ST11Response200DataTrackingLastKnownLocation(ApiModel):
    """ST11Response200DataTrackingLastKnownLocation model."""

    location: Optional[StrictStr] = None
    occurrence_date: Optional[ST11Response200DataTrackingLastKnownLocationOccurrenceDate] = None
