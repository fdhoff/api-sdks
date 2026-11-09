# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or31_response200_order_update_errors_errors import OR31Response200OrderUpdateErrorsErrors
from mirakl_seller.models.or31_response200_order_update_errors_input import OR31Response200OrderUpdateErrorsInput
from mirakl_seller._runtime import ApiModel


class OR31Response200OrderUpdateErrors(ApiModel):
    """OR31Response200OrderUpdateErrors model."""

    errors: List[OR31Response200OrderUpdateErrorsErrors]
    input: Optional[OR31Response200OrderUpdateErrorsInput] = None
