# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or30_response200_cancelations_purchase_information_purchase_commission_on_fees import (
    OR30Response200CancelationsPurchaseInformationPurchaseCommissionOnFees,
)
from mirakl_seller.models.or30_response200_cancelations_purchase_information_purchase_fee_amount import (
    OR30Response200CancelationsPurchaseInformationPurchaseFeeAmount,
)
from mirakl_seller._runtime import ApiModel


class OR30Response200CancelationsPurchaseInformation(ApiModel):
    """OR30Response200CancelationsPurchaseInformation model."""

    purchase_commission_on_fees: Optional[OR30Response200CancelationsPurchaseInformationPurchaseCommissionOnFees] = None
    purchase_commission_on_price: float
    purchase_commission_on_shipping: float
    purchase_fee_amount: Optional[OR30Response200CancelationsPurchaseInformationPurchaseFeeAmount] = None
    purchase_price: float
    purchase_shipping_price: float
