# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or04_request_orders_order_lines_eco_contributions import (
    OR04RequestOrdersOrderLinesEcoContributions,
)
from mirakl_seller._runtime import ApiModel


class OR04RequestOrdersOrderLines(ApiModel):
    """OR04RequestOrdersOrderLines model."""

    eco_contributions: Optional[List[OR04RequestOrdersOrderLinesEcoContributions]] = None
    order_line_id: StrictStr
