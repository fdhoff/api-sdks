# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller._runtime import ApiModel


class P11Response200ProductsOffersShippingTypesDeliveryTime(ApiModel):
    """P11Response200ProductsOffersShippingTypesDeliveryTime model."""

    earliest_days: StrictInt
    earliest_delivery_date: datetime
    latest_days: StrictInt
    latest_delivery_date: datetime
