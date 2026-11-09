# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or11_response200_orders_order_lines_order_line_additional_fields import (
    OR11Response200OrdersOrderLinesOrderLineAdditionalFields,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersOrderLinesOrderLineAdditionalFieldsTextarea(
    OR11Response200OrdersOrderLinesOrderLineAdditionalFields
):
    """OR11Response200OrdersOrderLinesOrderLineAdditionalFieldsTextarea model."""

    value: StrictStr
