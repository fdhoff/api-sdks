# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.rt01_response200_return_success_return_lines_compliance import (
    RT01Response200ReturnSuccessReturnLinesCompliance,
)
from mirakl_seller._runtime import ApiModel


class RT01Response200ReturnSuccessReturnLines(ApiModel):
    """RT01Response200ReturnSuccessReturnLines model."""

    compliance: Optional[List[RT01Response200ReturnSuccessReturnLinesCompliance]] = None
    order_line_id: StrictStr
    quantity: StrictInt
    reason_code: StrictStr
