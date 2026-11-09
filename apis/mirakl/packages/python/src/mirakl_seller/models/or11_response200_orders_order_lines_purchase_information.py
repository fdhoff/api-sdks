# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or11_response200_orders_order_lines_purchase_information_purchase_commission_on_fees import (
    OR11Response200OrdersOrderLinesPurchaseInformationPurchaseCommissionOnFees,
)
from mirakl_seller.models.or11_response200_orders_order_lines_purchase_information_purchase_fee_amount import (
    OR11Response200OrdersOrderLinesPurchaseInformationPurchaseFeeAmount,
)
from mirakl_seller._runtime import ApiModel


class OR11Response200OrdersOrderLinesPurchaseInformation(ApiModel):
    """OR11Response200OrdersOrderLinesPurchaseInformation model."""

    purchase_commission_on_fees: Optional[
        OR11Response200OrdersOrderLinesPurchaseInformationPurchaseCommissionOnFees
    ] = None
    purchase_commission_on_price: float
    purchase_commission_on_shipping: float
    purchase_fee_amount: Optional[OR11Response200OrdersOrderLinesPurchaseInformationPurchaseFeeAmount] = None
    purchase_price: float
    purchase_shipping_price: float
    purchase_unit_price: float
