# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class ST01Response201ShipmentSuccessTrackingLastKnownLocationOccurrenceDate(ApiModel):
    """ST01Response201ShipmentSuccessTrackingLastKnownLocationOccurrenceDate model."""

    var_date: Optional[date] = Field(default=None, alias="date")
    offset: Optional[StrictStr] = None
    time: Optional[StrictStr] = None
