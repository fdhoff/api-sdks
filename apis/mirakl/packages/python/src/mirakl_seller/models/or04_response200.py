# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or04_response200_updated_orders import OR04Response200UpdatedOrders
from mirakl_seller._runtime import ApiModel


class OR04Response200(ApiModel):
    """OR04Response200 model."""

    updated_orders: Optional[List[OR04Response200UpdatedOrders]] = None
