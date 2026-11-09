# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_refunds_taxes import (
    OR15Response200ExtFileStructureOrdersOrderRefundsTaxes,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersOrderRefunds(ApiModel):
    """OR15Response200ExtFileStructureOrdersOrderRefunds model."""

    order_refund_id: StrictStr
    taxes: Optional[List[OR15Response200ExtFileStructureOrdersOrderRefundsTaxes]] = None
