# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or32_response200_order_lines_adjusted_refunds_eco_contributions import (
    OR32Response200OrderLinesAdjustedRefundsEcoContributions,
)
from mirakl_seller.models.or32_response200_order_lines_adjusted_refunds_shipping_taxes import (
    OR32Response200OrderLinesAdjustedRefundsShippingTaxes,
)
from mirakl_seller.models.or32_response200_order_lines_adjusted_refunds_taxes import (
    OR32Response200OrderLinesAdjustedRefundsTaxes,
)
from mirakl_seller._runtime import ApiModel


class OR32Response200OrderLinesAdjustedRefunds(ApiModel):
    """OR32Response200OrderLinesAdjustedRefunds model."""

    amount: Optional[float] = None
    currency_iso_code: Optional[StrictStr] = None
    eco_contributions: Optional[List[OR32Response200OrderLinesAdjustedRefundsEcoContributions]] = None
    quantity: Optional[StrictInt] = None
    reason_code: Optional[StrictStr] = None
    shipping_amount: Optional[float] = None
    shipping_taxes: Optional[List[OR32Response200OrderLinesAdjustedRefundsShippingTaxes]] = None
    taxes: Optional[List[OR32Response200OrderLinesAdjustedRefundsTaxes]] = None
