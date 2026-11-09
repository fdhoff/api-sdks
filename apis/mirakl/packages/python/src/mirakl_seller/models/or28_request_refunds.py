# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or28_request_refunds_fees import OR28RequestRefundsFees
from mirakl_seller.models.or28_request_refunds_shipping_taxes import OR28RequestRefundsShippingTaxes
from mirakl_seller.models.or28_request_refunds_taxes import OR28RequestRefundsTaxes
from mirakl_seller._runtime import ApiModel


class OR28RequestRefunds(ApiModel):
    """OR28RequestRefunds model."""

    amount: float
    currency_iso_code: Optional[StrictStr] = None
    excluded_from_shipment: Optional[StrictBool] = None
    fees: Optional[List[OR28RequestRefundsFees]] = None
    order_line_id: StrictStr
    quantity: Optional[StrictInt] = 0
    reason_code: StrictStr
    shipping_amount: float
    shipping_taxes: Optional[List[OR28RequestRefundsShippingTaxes]] = None
    taxes: Optional[List[OR28RequestRefundsTaxes]] = None
