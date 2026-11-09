# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_order_line_additional_fields import (
    OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFieldsRegex(
    OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFields
):
    """OR15Response200ExtFileStructureOrdersOrderLinesOrderLineAdditionalFieldsRegex model."""

    value: StrictStr
