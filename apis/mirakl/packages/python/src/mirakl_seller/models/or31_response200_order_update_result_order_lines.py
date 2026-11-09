# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or31_response200_order_update_result_order_lines_order_line_additional_fields import (
    OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields,
)
from mirakl_seller._runtime import ApiModel


class OR31Response200OrderUpdateResultOrderLines(ApiModel):
    """OR31Response200OrderUpdateResultOrderLines model."""

    order_line_additional_fields: Optional[
        List[OR31Response200OrderUpdateResultOrderLinesOrderLineAdditionalFields]
    ] = None
    order_line_id: StrictStr
