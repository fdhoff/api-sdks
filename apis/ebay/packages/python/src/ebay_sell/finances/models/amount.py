# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class Amount(ApiModel):
    """Amount model."""

    converted_from_currency: Optional[StrictStr] = Field(default=None, alias="convertedFromCurrency")
    converted_from_value: Optional[StrictStr] = Field(default=None, alias="convertedFromValue")
    converted_to_currency: Optional[StrictStr] = Field(default=None, alias="convertedToCurrency")
    converted_to_value: Optional[StrictStr] = Field(default=None, alias="convertedToValue")
    currency: Optional[StrictStr] = None
    exchange_rate: Optional[StrictStr] = Field(default=None, alias="exchangeRate")
    value: Optional[StrictStr] = None
