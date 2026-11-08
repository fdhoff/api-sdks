# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feed.models.order_task import OrderTask
from ebay_sell._runtime import ApiModel


class OrderTaskCollection(ApiModel):
    """OrderTaskCollection model."""

    href: Optional[StrictStr] = None
    limit: Optional[StrictInt] = None
    next: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    prev: Optional[StrictStr] = None
    tasks: Optional[List[OrderTask]] = None
    total: Optional[StrictInt] = None
