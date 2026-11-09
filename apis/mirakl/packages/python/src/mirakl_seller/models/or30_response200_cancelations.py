# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or30_response200_cancelations_amount_breakdown import (
    OR30Response200CancelationsAmountBreakdown,
)
from mirakl_seller.models.or30_response200_cancelations_eco_contributions import (
    OR30Response200CancelationsEcoContributions,
)
from mirakl_seller.models.or30_response200_cancelations_fees import OR30Response200CancelationsFees
from mirakl_seller.models.or30_response200_cancelations_purchase_information import (
    OR30Response200CancelationsPurchaseInformation,
)
from mirakl_seller.models.or30_response200_cancelations_shipping_amount_breakdown import (
    OR30Response200CancelationsShippingAmountBreakdown,
)
from mirakl_seller.models.or30_response200_cancelations_shipping_taxes import OR30Response200CancelationsShippingTaxes
from mirakl_seller.models.or30_response200_cancelations_taxes import OR30Response200CancelationsTaxes
from mirakl_seller._runtime import ApiModel


class OR30Response200Cancelations(ApiModel):
    """OR30Response200Cancelations model."""

    amount: float
    amount_breakdown: Optional[OR30Response200CancelationsAmountBreakdown] = None
    cancelation_id: StrictStr
    currency_iso_code: Optional[StrictStr] = None
    eco_contributions: Optional[List[OR30Response200CancelationsEcoContributions]] = None
    fees: Optional[List[OR30Response200CancelationsFees]] = None
    order_line_id: StrictStr
    purchase_information: Optional[OR30Response200CancelationsPurchaseInformation] = None
    quantity: Optional[StrictInt] = None
    reason_code: StrictStr
    shipping_amount: float
    shipping_amount_breakdown: Optional[OR30Response200CancelationsShippingAmountBreakdown] = None
    shipping_taxes: Optional[List[OR30Response200CancelationsShippingTaxes]] = None
    taxes: Optional[List[OR30Response200CancelationsTaxes]] = None
