# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or11_response200_orders_order_lines_refunds_purchase_information_purchase_commission_on_fees import (
    OR11Response200OrdersOrderLinesRefundsPurchaseInformationPurchaseCommissionOnFees,
)
from mirakl_seller.models.or11_response200_orders_order_lines_refunds_purchase_information_purchase_fee_amount import (
    OR11Response200OrdersOrderLinesRefundsPurchaseInformationPurchaseFeeAmount,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersOrderLinesRefundsPurchaseInformation(ApiModel):
    """OR11Response200OrdersOrderLinesRefundsPurchaseInformation model."""

    purchase_commission_on_fees: Optional[
        OR11Response200OrdersOrderLinesRefundsPurchaseInformationPurchaseCommissionOnFees
    ] = None
    purchase_commission_on_price: float
    purchase_commission_on_shipping: float
    purchase_fee_amount: Optional[OR11Response200OrdersOrderLinesRefundsPurchaseInformationPurchaseFeeAmount] = None
    purchase_price: float
    purchase_shipping_price: float
