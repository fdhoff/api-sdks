# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or07_response200_order_lines_updated_address import OR07Response200OrderLinesUpdatedAddress
from mirakl_seller.models.or07_response200_order_lines_updated_warehouse import (
    OR07Response200OrderLinesUpdatedWarehouse,
)
from mirakl_seller._runtime import ApiModel


class OR07Response200OrderLinesUpdated(ApiModel):
    """OR07Response200OrderLinesUpdated model."""

    address: Optional[OR07Response200OrderLinesUpdatedAddress] = None
    warehouse: Optional[OR07Response200OrderLinesUpdatedWarehouse] = None
