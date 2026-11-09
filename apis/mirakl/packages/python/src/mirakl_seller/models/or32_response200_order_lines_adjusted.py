# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or32_response200_order_lines_adjusted_cancelations import (
    OR32Response200OrderLinesAdjustedCancelations,
)
from mirakl_seller.models.or32_response200_order_lines_adjusted_errors import OR32Response200OrderLinesAdjustedErrors
from mirakl_seller.models.or32_response200_order_lines_adjusted_measurement import (
    OR32Response200OrderLinesAdjustedMeasurement,
)
from mirakl_seller.models.or32_response200_order_lines_adjusted_refunds import OR32Response200OrderLinesAdjustedRefunds
from mirakl_seller._runtime import ApiModel


class OR32Response200OrderLinesAdjusted(ApiModel):
    """OR32Response200OrderLinesAdjusted model."""

    cancelations: Optional[List[OR32Response200OrderLinesAdjustedCancelations]] = None
    errors: Optional[List[OR32Response200OrderLinesAdjustedErrors]] = None
    measurement: Optional[OR32Response200OrderLinesAdjustedMeasurement] = None
    order_line_id: Optional[StrictStr] = None
    refunds: Optional[List[OR32Response200OrderLinesAdjustedRefunds]] = None
