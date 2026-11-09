# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or31_request_order_lines_order_line_additional_fields import (
    OR31RequestOrderLinesOrderLineAdditionalFields,
)
from mirakl_seller._runtime import ApiModel


class OR31RequestOrderLines(ApiModel):
    """OR31RequestOrderLines model."""

    order_line_additional_fields: Optional[List[OR31RequestOrderLinesOrderLineAdditionalFields]] = None
    order_line_id: StrictStr
