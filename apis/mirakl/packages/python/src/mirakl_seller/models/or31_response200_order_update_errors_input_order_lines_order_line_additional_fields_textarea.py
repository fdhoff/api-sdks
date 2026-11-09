# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or31_response200_order_update_errors_input_order_lines_order_line_additional_fields import (
    OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFields,
)
from mirakl_seller._runtime import ApiModel


class OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFieldsTextarea(
    OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFields
):
    """OR31Response200OrderUpdateErrorsInputOrderLinesOrderLineAdditionalFieldsTextarea model."""

    value: StrictStr
