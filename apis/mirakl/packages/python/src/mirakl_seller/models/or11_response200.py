# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or11_response200_orders import OR11Response200Orders
from mirakl_seller._runtime import ApiModel


class OR11Response200(ApiModel):
    """OR11Response200 model."""

    orders: List[OR11Response200Orders]
    total_count: StrictInt
