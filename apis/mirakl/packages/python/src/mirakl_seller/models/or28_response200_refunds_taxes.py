# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or28_response200_refunds_taxes_amount_breakdown import (
    OR28Response200RefundsTaxesAmountBreakdown,
)
from mirakl_seller.models.or28_response200_refunds_taxes_purchase_tax import OR28Response200RefundsTaxesPurchaseTax
from mirakl_seller._runtime import ApiModel


class OR28Response200RefundsTaxes(ApiModel):
    """OR28Response200RefundsTaxes model."""

    amount: float
    amount_breakdown: Optional[OR28Response200RefundsTaxesAmountBreakdown] = None
    code: StrictStr
    purchase_tax: Optional[OR28Response200RefundsTaxesPurchaseTax] = None
    rate: Optional[float] = None
