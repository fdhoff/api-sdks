# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or11_response200_orders_order_lines_taxes_amount_breakdown import (
    OR11Response200OrdersOrderLinesTaxesAmountBreakdown,
)
from mirakl_seller.models.or11_response200_orders_order_lines_taxes_purchase_tax import (
    OR11Response200OrdersOrderLinesTaxesPurchaseTax,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersOrderLinesTaxes(ApiModel):
    """OR11Response200OrdersOrderLinesTaxes model."""

    amount: float
    amount_breakdown: Optional[OR11Response200OrdersOrderLinesTaxesAmountBreakdown] = None
    code: StrictStr
    origin_unit_amount: Optional[float] = None
    purchase_tax: Optional[OR11Response200OrdersOrderLinesTaxesPurchaseTax] = None
    rate: Optional[float] = None
    tax_calculation_rule: StrictStr
