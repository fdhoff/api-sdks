# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or28_response200_refunds_amount_breakdown import OR28Response200RefundsAmountBreakdown
from mirakl_seller.models.or28_response200_refunds_eco_contributions import OR28Response200RefundsEcoContributions
from mirakl_seller.models.or28_response200_refunds_fees import OR28Response200RefundsFees
from mirakl_seller.models.or28_response200_refunds_purchase_information import OR28Response200RefundsPurchaseInformation
from mirakl_seller.models.or28_response200_refunds_shipping_amount_breakdown import (
    OR28Response200RefundsShippingAmountBreakdown,
)
from mirakl_seller.models.or28_response200_refunds_shipping_taxes import OR28Response200RefundsShippingTaxes
from mirakl_seller.models.or28_response200_refunds_taxes import OR28Response200RefundsTaxes
from mirakl_seller._runtime import ApiModel


class OR28Response200Refunds(ApiModel):
    """OR28Response200Refunds model."""

    amount: float
    amount_breakdown: Optional[OR28Response200RefundsAmountBreakdown] = None
    currency_iso_code: Optional[StrictStr] = None
    eco_contributions: Optional[List[OR28Response200RefundsEcoContributions]] = None
    excluded_from_shipment: Optional[StrictBool] = None
    fees: Optional[List[OR28Response200RefundsFees]] = None
    order_line_id: StrictStr
    order_refund_id: StrictStr
    purchase_information: Optional[OR28Response200RefundsPurchaseInformation] = None
    quantity: StrictInt
    reason_code: StrictStr
    refund_id: StrictStr
    shipping_amount: float
    shipping_amount_breakdown: Optional[OR28Response200RefundsShippingAmountBreakdown] = None
    shipping_taxes: Optional[List[OR28Response200RefundsShippingTaxes]] = None
    taxes: Optional[List[OR28Response200RefundsTaxes]] = None
