# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or07_response200_order_lines_errors import OR07Response200OrderLinesErrors
from mirakl_seller.models.or07_response200_order_lines_updated import OR07Response200OrderLinesUpdated
from mirakl_seller._runtime import ApiModel


class OR07Response200OrderLines(ApiModel):
    """OR07Response200OrderLines model."""

    errors: Optional[List[OR07Response200OrderLinesErrors]] = None
    id: StrictStr
    updated: Optional[OR07Response200OrderLinesUpdated] = None
