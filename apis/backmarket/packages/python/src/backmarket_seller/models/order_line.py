# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from backmarket_seller.models.order_line_state import OrderLineState
from backmarket_seller.models.product_condition import ProductCondition
from backmarket_seller.models.return_reason import ReturnReason
from backmarket_seller._runtime import ApiModel


class OrderLine(ApiModel):
    """OrderLine model."""

    id: Optional[StrictInt] = None
    date_creation: Optional[datetime] = None
    state: Optional[OrderLineState] = None
    price: Optional[StrictStr] = None
    shipping_price: Optional[StrictStr] = None
    shipping_delay: Optional[StrictInt] = None
    currency: Optional[StrictStr] = None
    return_reason: Optional[ReturnReason] = None
    return_message: Optional[StrictStr] = None
    listing: Optional[StrictStr] = None
    listing_id: Optional[StrictInt] = None
    orderline_fee: Optional[StrictStr] = None
    product: Optional[StrictStr] = None
    quantity: Optional[StrictInt] = None
    brand: Optional[StrictStr] = None
    product_id: Optional[StrictInt] = None
    backcare: Optional[StrictBool] = None
    backcare_price: Optional[StrictInt] = None
    sales_taxes: Optional[StrictStr] = None
    imei: Optional[StrictStr] = None
    serial_number: Optional[StrictStr] = None
    condition: Optional[ProductCondition] = None
