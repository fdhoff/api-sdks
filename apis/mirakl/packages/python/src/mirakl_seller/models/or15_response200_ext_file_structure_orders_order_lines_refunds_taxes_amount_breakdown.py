# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_refunds_taxes_amount_breakdown_parts import (
    OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxesAmountBreakdownParts,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxesAmountBreakdown(ApiModel):
    """OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxesAmountBreakdown model."""

    parts: Annotated[
        List[OR15Response200ExtFileStructureOrdersOrderLinesRefundsTaxesAmountBreakdownParts],
        Field(min_length=1, max_length=2147483647),
    ]
