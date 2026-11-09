# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_refunds_purchase_information_purchase_commission_on_fees import (
    OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformationPurchaseCommissionOnFees,
)
from mirakl_seller.models.or15_response200_ext_file_structure_orders_order_lines_refunds_purchase_information_purchase_fee_amount import (
    OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformationPurchaseFeeAmount,
)
from mirakl_seller._runtime import ApiModel


class OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformation(ApiModel):
    """OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformation model."""

    purchase_commission_on_fees: Optional[
        OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformationPurchaseCommissionOnFees
    ] = None
    purchase_commission_on_price: float
    purchase_commission_on_shipping: float
    purchase_fee_amount: Optional[
        OR15Response200ExtFileStructureOrdersOrderLinesRefundsPurchaseInformationPurchaseFeeAmount
    ] = None
    purchase_price: float
    purchase_shipping_price: float
