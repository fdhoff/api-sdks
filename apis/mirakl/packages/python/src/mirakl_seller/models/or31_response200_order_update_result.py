# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or31_response200_order_update_result_order_additional_fields import (
    OR31Response200OrderUpdateResultOrderAdditionalFields,
)
from mirakl_seller.models.or31_response200_order_update_result_order_lines import (
    OR31Response200OrderUpdateResultOrderLines,
)
from mirakl_seller._runtime import ApiModel


class OR31Response200OrderUpdateResult(ApiModel):
    """OR31Response200OrderUpdateResult model."""

    order_additional_fields: Optional[List[OR31Response200OrderUpdateResultOrderAdditionalFields]] = None
    order_lines: Optional[List[OR31Response200OrderUpdateResultOrderLines]] = None
