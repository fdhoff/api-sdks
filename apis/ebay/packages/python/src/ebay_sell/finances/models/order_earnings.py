# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.order_earning import OrderEarning
from ebay_sell._runtime import ApiModel


class OrderEarnings(ApiModel):
    """OrderEarnings model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    orders: Optional[List[OrderEarning]] = None
    prev: Optional[StrictStr] = None
    total: Optional[StrictInt] = None
