# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or30_request_cancelations_fees import OR30RequestCancelationsFees
from mirakl_seller.models.or30_request_cancelations_shipping_taxes import OR30RequestCancelationsShippingTaxes
from mirakl_seller.models.or30_request_cancelations_taxes import OR30RequestCancelationsTaxes
from mirakl_seller._runtime import ApiModel


class OR30RequestCancelations(ApiModel):
    """OR30RequestCancelations model."""

    amount: float
    currency_iso_code: Optional[StrictStr] = None
    fees: Optional[List[OR30RequestCancelationsFees]] = None
    order_line_id: StrictStr
    quantity: StrictInt
    reason_code: StrictStr
    shipping_amount: float
    shipping_taxes: Optional[List[OR30RequestCancelationsShippingTaxes]] = None
    taxes: Optional[List[OR30RequestCancelationsTaxes]] = None
