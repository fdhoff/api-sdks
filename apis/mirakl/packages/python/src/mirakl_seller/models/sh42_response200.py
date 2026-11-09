# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.sh42_response200_delivery_times import SH42Response200DeliveryTimes
from mirakl_seller.models.sh42_response200_lead_time_to_ship import SH42Response200LeadTimeToShip
from mirakl_seller.models.sh42_response200_order_cut_off_times import SH42Response200OrderCutOffTimes
from mirakl_seller._runtime import ApiModel


class SH42Response200(ApiModel):
    """SH42Response200 model."""

    delivery_times: List[SH42Response200DeliveryTimes]
    last_updated_date: Optional[datetime] = None
    lead_time_to_ship: SH42Response200LeadTimeToShip
    order_cut_off_times: List[SH42Response200OrderCutOffTimes]
    order_free_shipping: StrictBool
    shipping_paid_by_operator: StrictBool
    shop_id: StrictStr
