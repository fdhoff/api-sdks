# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List
from mirakl_seller.models.or07_request_order_lines_shipping_from import OR07RequestOrderLinesShippingFrom
from mirakl_seller._runtime import ApiModel


class OR07RequestOrderLines(ApiModel):
    """OR07RequestOrderLines model."""

    id: StrictStr
    shipping_from: OR07RequestOrderLinesShippingFrom
