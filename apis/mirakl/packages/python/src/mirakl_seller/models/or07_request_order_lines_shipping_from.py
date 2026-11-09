# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or07_request_order_lines_shipping_from_address import OR07RequestOrderLinesShippingFromAddress
from mirakl_seller.models.or07_request_order_lines_shipping_from_warehouse import (
    OR07RequestOrderLinesShippingFromWarehouse,
)
from mirakl_seller._runtime import ApiModel


class OR07RequestOrderLinesShippingFrom(ApiModel):
    """OR07RequestOrderLinesShippingFrom model."""

    address: Optional[OR07RequestOrderLinesShippingFromAddress] = None
    warehouse: Optional[OR07RequestOrderLinesShippingFromWarehouse] = None
