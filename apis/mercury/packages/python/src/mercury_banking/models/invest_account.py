# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.account_status import AccountStatus
from mercury_banking._runtime import ApiModel


class InvestAccount(ApiModel):
    """InvestAccount model."""

    available_balance: Annotated[float, Field(multiple_of=0.01)] = Field(alias="availableBalance")
    created_at: StrictStr = Field(alias="createdAt")
    current_balance: Annotated[float, Field(multiple_of=0.01)] = Field(alias="currentBalance")
    id: UUID
    status: AccountStatus
