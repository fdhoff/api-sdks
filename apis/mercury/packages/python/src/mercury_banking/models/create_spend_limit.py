# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mercury_banking.models.spend_limit_interval import SpendLimitInterval
from mercury_banking._runtime import ApiModel


class CreateSpendLimit(ApiModel):
    """CreateSpendLimit model."""

    amount_cents: Annotated[int, Field(strict=True, ge=0)] = Field(alias="amountCents")
    interval: SpendLimitInterval
