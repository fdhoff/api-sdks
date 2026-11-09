# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class SH12Response200ShippingTypes(ApiModel):
    """SH12Response200ShippingTypes model."""

    click_and_collect: StrictBool
    code: StrictStr
    delivery_by_operator: StrictBool
    description: StrictStr
    ignore_lead_time_to_ship: Optional[StrictBool] = None
    label: StrictStr
    mandatory_tracking: StrictBool
    standard_code: Optional[StrictStr] = None
