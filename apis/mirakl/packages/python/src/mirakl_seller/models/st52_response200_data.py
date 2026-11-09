# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st52_response200_data_errors import ST52Response200DataErrors
from mirakl_seller.models.st52_response200_data_estimated_cost import ST52Response200DataEstimatedCost
from mirakl_seller.models.st52_response200_data_files import ST52Response200DataFiles
from mirakl_seller.models.st52_response200_data_tracking import ST52Response200DataTracking
from mirakl_seller._runtime import ApiModel


class ST52Response200Data(ApiModel):
    """ST52Response200Data model."""

    date_created: datetime
    errors: Optional[List[ST52Response200DataErrors]] = None
    estimated_cost: Optional[ST52Response200DataEstimatedCost] = None
    files: Optional[ST52Response200DataFiles] = None
    label_state: StrictStr
    last_updated: datetime
    shipment_id: StrictStr
    tracking: Optional[ST52Response200DataTracking] = None
