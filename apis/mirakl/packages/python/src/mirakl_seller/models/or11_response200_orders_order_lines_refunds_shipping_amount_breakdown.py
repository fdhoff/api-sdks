# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.or11_response200_orders_order_lines_refunds_shipping_amount_breakdown_parts import (
    OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdownParts,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdown(ApiModel):
    """OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdown model."""

    parts: Annotated[
        List[OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdownParts],
        Field(min_length=1, max_length=2147483647),
    ]
