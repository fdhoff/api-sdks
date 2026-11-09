# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or21_request_order_lines import OR21RequestOrderLines
from mirakl_seller._runtime import ApiModel


class OR21Request(ApiModel):
    """OR21Request model."""

    order_lines: List[OR21RequestOrderLines]
