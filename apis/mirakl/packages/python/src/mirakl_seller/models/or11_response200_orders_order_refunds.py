# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or11_response200_orders_order_refunds_taxes import OR11Response200OrdersOrderRefundsTaxes
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersOrderRefunds(ApiModel):
    """OR11Response200OrdersOrderRefunds model."""

    order_refund_id: StrictStr
    taxes: Optional[List[OR11Response200OrdersOrderRefundsTaxes]] = None
