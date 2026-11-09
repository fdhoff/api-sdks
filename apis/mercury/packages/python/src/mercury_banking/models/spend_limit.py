# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.spend_limit_interval import SpendLimitInterval
from mercury_banking._runtime import ApiModel


class SpendLimit(ApiModel):
    """SpendLimit model."""

    amount_cents: Annotated[int, Field(strict=True, ge=0)] = Field(alias="amountCents")
    atm_amount_cents: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=None, alias="atmAmountCents")
    interval: SpendLimitInterval
