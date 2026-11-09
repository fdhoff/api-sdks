# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or04_response200_updated_orders_updated_order_lines import (
    OR04Response200UpdatedOrdersUpdatedOrderLines,
)
from mirakl_seller.models.or04_response200_updated_orders_updated_references import (
    OR04Response200UpdatedOrdersUpdatedReferences,
)
from mirakl_seller._runtime import ApiModel


class OR04Response200UpdatedOrdersUpdated(ApiModel):
    """OR04Response200UpdatedOrdersUpdated model."""

    order_lines: Optional[List[OR04Response200UpdatedOrdersUpdatedOrderLines]] = None
    references: Optional[OR04Response200UpdatedOrdersUpdatedReferences] = None
