# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st42_response200_data_rates_estimated_cost import ST42Response200DataRatesEstimatedCost
from mirakl_seller._runtime import ApiModel


class ST42Response200DataRates(ApiModel):
    """ST42Response200DataRates model."""

    carrier_code: StrictStr
    carrier_name: StrictStr
    carrier_service_code: Optional[StrictStr] = None
    carrier_standard_code: StrictStr
    estimated_cost: Optional[ST42Response200DataRatesEstimatedCost] = None
    estimated_delivery_days: Optional[StrictInt] = None
    estimated_delivery_promise_status: Optional[StrictStr] = None
    label_selection_tags: List[StrictStr]
