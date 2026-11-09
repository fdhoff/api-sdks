# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or07_response200_order_lines import OR07Response200OrderLines
from mirakl_seller._runtime import ApiModel


class OR07Response200(ApiModel):
    """OR07Response200 model."""

    order_lines: Optional[List[OR07Response200OrderLines]] = None
