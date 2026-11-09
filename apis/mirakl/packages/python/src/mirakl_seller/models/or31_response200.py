# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or31_response200_order_update_errors import OR31Response200OrderUpdateErrors
from mirakl_seller.models.or31_response200_order_update_result import OR31Response200OrderUpdateResult
from mirakl_seller._runtime import ApiModel


class OR31Response200(ApiModel):
    """OR31Response200 model."""

    order_update_errors: Optional[OR31Response200OrderUpdateErrors] = None
    order_update_result: Optional[OR31Response200OrderUpdateResult] = None
