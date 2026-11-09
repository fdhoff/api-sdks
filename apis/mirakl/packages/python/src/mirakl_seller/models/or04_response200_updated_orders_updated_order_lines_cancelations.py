# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or04_response200_updated_orders_updated_order_lines_cancelations_eco_contributions import (
    OR04Response200UpdatedOrdersUpdatedOrderLinesCancelationsEcoContributions,
)
from mirakl_seller._runtime import ApiModel


class OR04Response200UpdatedOrdersUpdatedOrderLinesCancelations(ApiModel):
    """OR04Response200UpdatedOrdersUpdatedOrderLinesCancelations model."""

    cancelation_id: Optional[StrictStr] = None
    eco_contributions: Optional[List[OR04Response200UpdatedOrdersUpdatedOrderLinesCancelationsEcoContributions]] = None
