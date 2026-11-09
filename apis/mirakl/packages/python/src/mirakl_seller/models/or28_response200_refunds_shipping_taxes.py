# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or28_response200_refunds_shipping_taxes_amount_breakdown import (
    OR28Response200RefundsShippingTaxesAmountBreakdown,
)
from mirakl_seller.models.or28_response200_refunds_shipping_taxes_purchase_tax import (
    OR28Response200RefundsShippingTaxesPurchaseTax,
)
from mirakl_seller._runtime import ApiModel


class OR28Response200RefundsShippingTaxes(ApiModel):
    """OR28Response200RefundsShippingTaxes model."""

    amount: float
    amount_breakdown: Optional[OR28Response200RefundsShippingTaxesAmountBreakdown] = None
    code: StrictStr
    purchase_tax: Optional[OR28Response200RefundsShippingTaxesPurchaseTax] = None
    rate: Optional[float] = None
