# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_shipping_price_amount_breakdown_parts import (
    OR15Response200ExtFileStructureOrdersOrderLinesShippingPriceAmountBreakdownParts,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersOrderLinesShippingPriceAmountBreakdown(ApiModel):
    """OR15Response200ExtFileStructureOrdersOrderLinesShippingPriceAmountBreakdown model."""

    parts: Annotated[
        List[OR15Response200ExtFileStructureOrdersOrderLinesShippingPriceAmountBreakdownParts],
        Field(min_length=1, max_length=2147483647),
    ]
