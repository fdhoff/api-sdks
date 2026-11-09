# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.rt52_response200_data_errors import RT52Response200DataErrors
from mirakl_seller.models.rt52_response200_data_estimated_cost import RT52Response200DataEstimatedCost
from mirakl_seller.models.rt52_response200_data_files import RT52Response200DataFiles
from mirakl_seller.models.rt52_response200_data_tracking import RT52Response200DataTracking
from mirakl_seller._runtime import ApiModel


class RT52Response200Data(ApiModel):
    """RT52Response200Data model."""

    date_created: datetime
    errors: Optional[List[RT52Response200DataErrors]] = None
    estimated_cost: Optional[RT52Response200DataEstimatedCost] = None
    files: Optional[RT52Response200DataFiles] = None
    label_state: StrictStr
    last_updated: datetime
    return_id: StrictStr
    tracking: Optional[RT52Response200DataTracking] = None
