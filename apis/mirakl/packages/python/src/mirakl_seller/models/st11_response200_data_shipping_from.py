# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.st11_response200_data_shipping_from_address import ST11Response200DataShippingFromAddress
from mirakl_seller.models.st11_response200_data_shipping_from_warehouse import ST11Response200DataShippingFromWarehouse
from mirakl_seller._runtime import ApiModel


class ST11Response200DataShippingFrom(ApiModel):
    """ST11Response200DataShippingFrom model."""

    address: Optional[ST11Response200DataShippingFromAddress] = None
    warehouse: Optional[ST11Response200DataShippingFromWarehouse] = None
