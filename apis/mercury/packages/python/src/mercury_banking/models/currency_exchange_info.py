# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking._runtime import ApiModel


class CurrencyExchangeInfo(ApiModel):
    """CurrencyExchangeInfo model."""

    converted_from_amount: Annotated[float, Field(multiple_of=0.01)] = Field(alias="convertedFromAmount")
    converted_from_currency: StrictStr = Field(alias="convertedFromCurrency")
    converted_to_amount: Annotated[float, Field(multiple_of=0.01)] = Field(alias="convertedToAmount")
    converted_to_currency: StrictStr = Field(alias="convertedToCurrency")
    exchange_rate: Annotated[float, Field(multiple_of=0.00010)] = Field(alias="exchangeRate")
    fee_amount: Annotated[float, Field(multiple_of=0.01)] = Field(alias="feeAmount")
    fee_percentage: Annotated[float, Field(multiple_of=0.00010)] = Field(alias="feePercentage")
    fee_transaction_id: Optional[UUID] = Field(default=None, alias="feeTransactionId")
