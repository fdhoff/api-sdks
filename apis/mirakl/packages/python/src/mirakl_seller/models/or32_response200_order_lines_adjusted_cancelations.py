# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller.models.or32_response200_order_lines_adjusted_cancelations_eco_contributions import (
    OR32Response200OrderLinesAdjustedCancelationsEcoContributions,
)
from mirakl_seller.models.or32_response200_order_lines_adjusted_cancelations_shipping_taxes import (
    OR32Response200OrderLinesAdjustedCancelationsShippingTaxes,
)
from mirakl_seller.models.or32_response200_order_lines_adjusted_cancelations_taxes import (
    OR32Response200OrderLinesAdjustedCancelationsTaxes,
)
from mirakl_seller._runtime import ApiModel


class OR32Response200OrderLinesAdjustedCancelations(ApiModel):
    """OR32Response200OrderLinesAdjustedCancelations model."""

    amount: Optional[float] = None
    currency_iso_code: Optional[StrictStr] = None
    eco_contributions: Optional[List[OR32Response200OrderLinesAdjustedCancelationsEcoContributions]] = None
    quantity: Optional[StrictInt] = None
    reason_code: Optional[StrictStr] = None
    shipping_amount: Optional[float] = None
    shipping_taxes: Optional[List[OR32Response200OrderLinesAdjustedCancelationsShippingTaxes]] = None
    taxes: Optional[List[OR32Response200OrderLinesAdjustedCancelationsTaxes]] = None
