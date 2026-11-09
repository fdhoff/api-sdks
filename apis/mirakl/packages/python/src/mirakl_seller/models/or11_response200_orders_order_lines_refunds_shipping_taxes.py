# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or11_response200_orders_order_lines_refunds_shipping_taxes_amount_breakdown import (
    OR11Response200OrdersOrderLinesRefundsShippingTaxesAmountBreakdown,
)
from mirakl_seller.models.or11_response200_orders_order_lines_refunds_shipping_taxes_purchase_tax import (
    OR11Response200OrdersOrderLinesRefundsShippingTaxesPurchaseTax,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersOrderLinesRefundsShippingTaxes(ApiModel):
    """OR11Response200OrdersOrderLinesRefundsShippingTaxes model."""

    amount: float
    amount_breakdown: Optional[OR11Response200OrdersOrderLinesRefundsShippingTaxesAmountBreakdown] = None
    code: StrictStr
    purchase_tax: Optional[OR11Response200OrdersOrderLinesRefundsShippingTaxesPurchaseTax] = None
    rate: Optional[float] = None
