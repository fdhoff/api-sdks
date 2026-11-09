# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class DR12Response200DataDeliveryBillInformation(ApiModel):
    """DR12Response200DataDeliveryBillInformation model."""

    delivery_bill_date: Optional[date] = None
    delivery_bill_id: Optional[StrictStr] = None
