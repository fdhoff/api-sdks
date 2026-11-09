# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or28_response200_refunds_purchase_information_purchase_commission_on_fees import (
    OR28Response200RefundsPurchaseInformationPurchaseCommissionOnFees,
)
from mirakl_seller.models.or28_response200_refunds_purchase_information_purchase_fee_amount import (
    OR28Response200RefundsPurchaseInformationPurchaseFeeAmount,
)
from mirakl_seller._runtime import ApiModel


class OR28Response200RefundsPurchaseInformation(ApiModel):
    """OR28Response200RefundsPurchaseInformation model."""

    purchase_commission_on_fees: Optional[OR28Response200RefundsPurchaseInformationPurchaseCommissionOnFees] = None
    purchase_commission_on_price: float
    purchase_commission_on_shipping: float
    purchase_fee_amount: Optional[OR28Response200RefundsPurchaseInformationPurchaseFeeAmount] = None
    purchase_price: float
    purchase_shipping_price: float
