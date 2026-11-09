# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_shipping_from_address import (
    OR15Response200ExtFileStructureOrdersOrderLinesShippingFromAddress,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_shipping_from_warehouse import (
    OR15Response200ExtFileStructureOrdersOrderLinesShippingFromWarehouse,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersOrderLinesShippingFrom(ApiModel):
    """OR15Response200ExtFileStructureOrdersOrderLinesShippingFrom model."""

    address: Optional[OR15Response200ExtFileStructureOrdersOrderLinesShippingFromAddress] = None
    warehouse: Optional[OR15Response200ExtFileStructureOrdersOrderLinesShippingFromWarehouse] = None
