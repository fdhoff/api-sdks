# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking._runtime import ApiModel


class CardBudget(ApiModel):
    """CardBudget model."""

    amount_cents: Annotated[int, Field(strict=True, ge=0)] = Field(alias="amountCents")
    id: UUID
    name: StrictStr
    remaining_amount_cents: Annotated[int, Field(strict=True, ge=0)] = Field(alias="remainingAmountCents")
