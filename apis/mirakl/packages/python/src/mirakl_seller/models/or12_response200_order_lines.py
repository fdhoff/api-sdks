# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or12_response200_order_lines_order_line_additional_fields import (
    OR12Response200OrderLinesOrderLineAdditionalFields,
)
from mirakl_seller._runtime import ApiModel


class OR12Response200OrderLines(ApiModel):
    """OR12Response200OrderLines model."""

    can_refund: StrictBool
    category_code: StrictStr
    category_label: StrictStr
    commission_fee: float
    commission_rate_vat: float
    commission_vat: float
    created_date: datetime
    debited_date: datetime
    description: StrictStr
    last_updated_date: datetime
    offer_id: StrictInt
    offer_sku: StrictStr
    offer_state_code: StrictStr
    order_line_additional_fields: List[OR12Response200OrderLinesOrderLineAdditionalFields]
    order_line_id: StrictStr
    order_line_index: StrictInt
    order_line_state: StrictStr
    order_line_state_reason_code: StrictStr
    order_line_state_reason_label: StrictStr
    price: float
    price_additional_info: Optional[StrictStr] = None
    price_unit: float
    product_sku: StrictStr
    product_title: StrictStr
    quantity: StrictInt
    received_date: datetime
    shipped_date: datetime
    shipping_price: float
    shipping_price_additional_unit: float
    shipping_price_unit: float
    total_commission: float
    total_price: float
