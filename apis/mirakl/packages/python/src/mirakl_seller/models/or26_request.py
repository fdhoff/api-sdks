# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or26_request_order_lines import OR26RequestOrderLines
from mirakl_seller._runtime import ApiModel


class OR26Request(ApiModel):
    """OR26Request model."""

    order_lines: List[OR26RequestOrderLines]
