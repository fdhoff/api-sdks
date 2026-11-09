# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date, datetime
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class DR12Response200DataShipments(ApiModel):
    """DR12Response200DataShipments model."""

    carrier_name: Optional[StrictStr] = None
    carrier_scac_code: Optional[StrictStr] = None
    delivery_bill_date: Optional[date] = None
    delivery_bill_id: Optional[StrictStr] = None
    id: Optional[StrictStr] = None
    shipped_date: Optional[datetime] = None
    tracking_number: Optional[StrictStr] = None
