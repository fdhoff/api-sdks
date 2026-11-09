# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.rt04_response200_return_success_return_lines_compliance import (
    RT04Response200ReturnSuccessReturnLinesCompliance,
)
from mirakl_seller._runtime import ApiModel


class RT04Response200ReturnSuccessReturnLines(ApiModel):
    """RT04Response200ReturnSuccessReturnLines model."""

    compliance: Optional[List[RT04Response200ReturnSuccessReturnLinesCompliance]] = None
    order_line_id: StrictStr
    quantity: StrictInt
    reason_code: StrictStr
