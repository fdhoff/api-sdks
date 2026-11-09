# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import datetime
from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or11_response200_orders_order_lines_cancelations_amount_breakdown import (
    OR11Response200OrdersOrderLinesCancelationsAmountBreakdown,
)
from mirakl_seller.models.or11_response200_orders_order_lines_cancelations_commission_taxes import (
    OR11Response200OrdersOrderLinesCancelationsCommissionTaxes,
)
from mirakl_seller.models.or11_response200_orders_order_lines_cancelations_eco_contributions import (
    OR11Response200OrdersOrderLinesCancelationsEcoContributions,
)
from mirakl_seller.models.or11_response200_orders_order_lines_cancelations_fees import (
    OR11Response200OrdersOrderLinesCancelationsFees,
)
from mirakl_seller.models.or11_response200_orders_order_lines_cancelations_purchase_information import (
    OR11Response200OrdersOrderLinesCancelationsPurchaseInformation,
)
from mirakl_seller.models.or11_response200_orders_order_lines_cancelations_shipping_amount_breakdown import (
    OR11Response200OrdersOrderLinesCancelationsShippingAmountBreakdown,
)
from mirakl_seller.models.or11_response200_orders_order_lines_cancelations_shipping_taxes import (
    OR11Response200OrdersOrderLinesCancelationsShippingTaxes,
)
from mirakl_seller.models.or11_response200_orders_order_lines_cancelations_taxes import (
    OR11Response200OrdersOrderLinesCancelationsTaxes,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersOrderLinesCancelations(ApiModel):
    """OR11Response200OrdersOrderLinesCancelations model."""

    amount: Optional[float] = None
    amount_breakdown: Optional[OR11Response200OrdersOrderLinesCancelationsAmountBreakdown] = None
    commission_amount: float
    commission_taxes: List[OR11Response200OrdersOrderLinesCancelationsCommissionTaxes]
    commission_total_amount: float
    created_date: datetime
    eco_contributions: Optional[List[OR11Response200OrdersOrderLinesCancelationsEcoContributions]] = None
    fees: Optional[List[OR11Response200OrdersOrderLinesCancelationsFees]] = None
    id: StrictStr
    purchase_information: Optional[OR11Response200OrdersOrderLinesCancelationsPurchaseInformation] = None
    quantity: Optional[StrictInt] = None
    reason_code: Optional[StrictStr] = None
    shipping_amount: Optional[float] = None
    shipping_amount_breakdown: Optional[OR11Response200OrdersOrderLinesCancelationsShippingAmountBreakdown] = None
    shipping_taxes: Optional[List[OR11Response200OrdersOrderLinesCancelationsShippingTaxes]] = None
    taxes: Optional[List[OR11Response200OrdersOrderLinesCancelationsTaxes]] = None
