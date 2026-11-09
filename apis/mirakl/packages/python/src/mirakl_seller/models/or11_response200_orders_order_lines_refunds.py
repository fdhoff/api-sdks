# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or11_response200_orders_order_lines_refunds_amount_breakdown import (
    OR11Response200OrdersOrderLinesRefundsAmountBreakdown,
)
from mirakl_seller.models.or11_response200_orders_order_lines_refunds_commission_taxes import (
    OR11Response200OrdersOrderLinesRefundsCommissionTaxes,
)
from mirakl_seller.models.or11_response200_orders_order_lines_refunds_eco_contributions import (
    OR11Response200OrdersOrderLinesRefundsEcoContributions,
)
from mirakl_seller.models.or11_response200_orders_order_lines_refunds_fees import (
    OR11Response200OrdersOrderLinesRefundsFees,
)
from mirakl_seller.models.or11_response200_orders_order_lines_refunds_purchase_information import (
    OR11Response200OrdersOrderLinesRefundsPurchaseInformation,
)
from mirakl_seller.models.or11_response200_orders_order_lines_refunds_shipping_amount_breakdown import (
    OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdown,
)
from mirakl_seller.models.or11_response200_orders_order_lines_refunds_shipping_taxes import (
    OR11Response200OrdersOrderLinesRefundsShippingTaxes,
)
from mirakl_seller.models.or11_response200_orders_order_lines_refunds_taxes import (
    OR11Response200OrdersOrderLinesRefundsTaxes,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersOrderLinesRefunds(ApiModel):
    """OR11Response200OrdersOrderLinesRefunds model."""

    amount: Optional[float] = None
    amount_breakdown: Optional[OR11Response200OrdersOrderLinesRefundsAmountBreakdown] = None
    commission_amount: float
    commission_tax_amount: float
    commission_taxes: List[OR11Response200OrdersOrderLinesRefundsCommissionTaxes]
    commission_total_amount: float
    created_date: datetime
    eco_contributions: Optional[List[OR11Response200OrdersOrderLinesRefundsEcoContributions]] = None
    fees: Optional[List[OR11Response200OrdersOrderLinesRefundsFees]] = None
    id: StrictStr
    order_refund_id: StrictStr
    purchase_information: Optional[OR11Response200OrdersOrderLinesRefundsPurchaseInformation] = None
    quantity: StrictInt
    reason_code: StrictStr
    refund_state: StrictStr
    shipping_amount: Optional[float] = None
    shipping_amount_breakdown: Optional[OR11Response200OrdersOrderLinesRefundsShippingAmountBreakdown] = None
    shipping_taxes: Optional[List[OR11Response200OrdersOrderLinesRefundsShippingTaxes]] = None
    state: StrictStr
    tax_legal_notice: Optional[StrictStr] = None
    taxes: Optional[List[OR11Response200OrdersOrderLinesRefundsTaxes]] = None
    transaction_date: Optional[datetime] = None
    transaction_number: Optional[StrictStr] = None
