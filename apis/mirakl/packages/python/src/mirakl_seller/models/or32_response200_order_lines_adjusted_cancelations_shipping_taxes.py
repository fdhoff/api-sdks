# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class OR32Response200OrderLinesAdjustedCancelationsShippingTaxes(ApiModel):
    """OR32Response200OrderLinesAdjustedCancelationsShippingTaxes model."""

    amount: Optional[float] = None
    code: Optional[StrictStr] = None
