# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or31_request_order_lines_order_line_additional_fields import (
    OR31RequestOrderLinesOrderLineAdditionalFields,
)
from mirakl_seller._runtime import ApiModel


class OR31RequestOrderLinesOrderLineAdditionalFieldsRegex(OR31RequestOrderLinesOrderLineAdditionalFields):
    """OR31RequestOrderLinesOrderLineAdditionalFieldsRegex model."""

    value: StrictStr
