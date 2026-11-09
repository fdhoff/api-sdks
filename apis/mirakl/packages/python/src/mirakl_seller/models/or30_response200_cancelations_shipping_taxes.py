# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or30_response200_cancelations_shipping_taxes_amount_breakdown import (
    OR30Response200CancelationsShippingTaxesAmountBreakdown,
)
from mirakl_seller.models.or30_response200_cancelations_shipping_taxes_purchase_tax import (
    OR30Response200CancelationsShippingTaxesPurchaseTax,
)
from mirakl_seller._runtime import ApiModel


class OR30Response200CancelationsShippingTaxes(ApiModel):
    """OR30Response200CancelationsShippingTaxes model."""

    amount: float
    amount_breakdown: Optional[OR30Response200CancelationsShippingTaxesAmountBreakdown] = None
    code: StrictStr
    purchase_tax: Optional[OR30Response200CancelationsShippingTaxesPurchaseTax] = None
    rate: Optional[float] = None
