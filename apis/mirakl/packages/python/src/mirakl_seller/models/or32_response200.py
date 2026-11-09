# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or32_response200_order_lines_adjusted import OR32Response200OrderLinesAdjusted
from mirakl_seller._runtime import ApiModel


class OR32Response200(ApiModel):
    """OR32Response200 model."""

    order_lines_adjusted: Optional[List[OR32Response200OrderLinesAdjusted]] = None
