# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st42_response200_data_errors import ST42Response200DataErrors
from mirakl_seller.models.st42_response200_data_rates import ST42Response200DataRates
from mirakl_seller._runtime import ApiModel


class ST42Response200Data(ApiModel):
    """ST42Response200Data model."""

    date_created: datetime
    errors: Optional[List[ST42Response200DataErrors]] = None
    label_rate_state: StrictStr
    last_updated: datetime
    rates: Optional[List[ST42Response200DataRates]] = None
    shipment_id: StrictStr
