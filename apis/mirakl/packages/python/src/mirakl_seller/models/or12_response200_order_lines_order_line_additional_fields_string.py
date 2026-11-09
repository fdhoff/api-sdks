# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or12_response200_order_lines_order_line_additional_fields import (
    OR12Response200OrderLinesOrderLineAdditionalFields,
)
from mirakl_seller._runtime import ApiModel


class OR12Response200OrderLinesOrderLineAdditionalFieldsString(OR12Response200OrderLinesOrderLineAdditionalFields):
    """OR12Response200OrderLinesOrderLineAdditionalFieldsString model."""

    value: StrictStr
