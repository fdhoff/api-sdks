# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or30_response200_cancelations_taxes_amount_breakdown import (
    OR30Response200CancelationsTaxesAmountBreakdown,
)
from mirakl_seller.models.or30_response200_cancelations_taxes_purchase_tax import (
    OR30Response200CancelationsTaxesPurchaseTax,
)
from mirakl_seller._runtime import ApiModel


class OR30Response200CancelationsTaxes(ApiModel):
    """OR30Response200CancelationsTaxes model."""

    amount: float
    amount_breakdown: Optional[OR30Response200CancelationsTaxesAmountBreakdown] = None
    code: StrictStr
    purchase_tax: Optional[OR30Response200CancelationsTaxesPurchaseTax] = None
    rate: Optional[float] = None
