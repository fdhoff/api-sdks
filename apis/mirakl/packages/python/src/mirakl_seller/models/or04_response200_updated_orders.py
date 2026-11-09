# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or04_response200_updated_orders_errors import OR04Response200UpdatedOrdersErrors
from mirakl_seller.models.or04_response200_updated_orders_updated import OR04Response200UpdatedOrdersUpdated
from mirakl_seller._runtime import ApiModel


class OR04Response200UpdatedOrders(ApiModel):
    """OR04Response200UpdatedOrders model."""

    errors: Optional[List[OR04Response200UpdatedOrdersErrors]] = None
    order_id: Optional[StrictStr] = None
    updated: Optional[OR04Response200UpdatedOrdersUpdated] = None
