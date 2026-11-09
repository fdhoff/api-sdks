# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or31_response200_order_update_errors_input_order_additional_fields import (
    OR31Response200OrderUpdateErrorsInputOrderAdditionalFields,
)
from mirakl_seller.models.or31_response200_order_update_errors_input_order_lines import (
    OR31Response200OrderUpdateErrorsInputOrderLines,
)
from mirakl_seller._runtime import ApiModel


class OR31Response200OrderUpdateErrorsInput(ApiModel):
    """OR31Response200OrderUpdateErrorsInput model."""

    order_additional_fields: Optional[List[OR31Response200OrderUpdateErrorsInputOrderAdditionalFields]] = None
    order_lines: Optional[List[OR31Response200OrderUpdateErrorsInputOrderLines]] = None
