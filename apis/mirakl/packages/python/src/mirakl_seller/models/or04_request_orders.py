# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or04_request_orders_order_lines import OR04RequestOrdersOrderLines
from mirakl_seller.models.or04_request_orders_references import OR04RequestOrdersReferences
from mirakl_seller._runtime import ApiModel


class OR04RequestOrders(ApiModel):
    """OR04RequestOrders model."""

    order_id: StrictStr
    order_lines: Optional[List[OR04RequestOrdersOrderLines]] = None
    references: Optional[OR04RequestOrdersReferences] = None
