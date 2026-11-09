# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or31_request_order_additional_fields import OR31RequestOrderAdditionalFields
from mirakl_seller.models.or31_request_order_lines import OR31RequestOrderLines
from mirakl_seller._runtime import ApiModel


class OR31Request(ApiModel):
    """OR31Request model."""

    order_additional_fields: Optional[List[OR31RequestOrderAdditionalFields]] = None
    order_lines: Optional[List[OR31RequestOrderLines]] = None
