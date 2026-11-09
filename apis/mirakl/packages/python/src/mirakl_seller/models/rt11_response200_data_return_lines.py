# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.rt11_response200_data_return_lines_compliance import RT11Response200DataReturnLinesCompliance
from mirakl_seller._runtime import ApiModel


class RT11Response200DataReturnLines(ApiModel):
    """RT11Response200DataReturnLines model."""

    compliance: Optional[List[RT11Response200DataReturnLinesCompliance]] = None
    order_line_id: StrictStr
    quantity: StrictInt
    reason_code: StrictStr
