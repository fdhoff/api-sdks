# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.sh42_response200_delivery_times_delivery_time import SH42Response200DeliveryTimesDeliveryTime
from mirakl_seller._runtime import ApiModel


class SH42Response200DeliveryTimes(ApiModel):
    """SH42Response200DeliveryTimes model."""

    delivery_time: Optional[SH42Response200DeliveryTimesDeliveryTime] = None
    set_by: StrictStr
    shipping_type_code: StrictStr
    shipping_zone_code: StrictStr
