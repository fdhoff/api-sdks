# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or11_response200_orders_order_lines_shipping_from_address import (
    OR11Response200OrdersOrderLinesShippingFromAddress,
)
from mirakl_seller.models.or11_response200_orders_order_lines_shipping_from_warehouse import (
    OR11Response200OrdersOrderLinesShippingFromWarehouse,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersOrderLinesShippingFrom(ApiModel):
    """OR11Response200OrdersOrderLinesShippingFrom model."""

    address: Optional[OR11Response200OrdersOrderLinesShippingFromAddress] = None
    warehouse: Optional[OR11Response200OrdersOrderLinesShippingFromWarehouse] = None
