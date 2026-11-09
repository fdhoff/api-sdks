# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking._runtime import ApiModel


class AutoTransferRuleReservoirPercentage(ApiModel):
    """AutoTransferRuleReservoirPercentage model."""

    account_id: UUID = Field(alias="accountId")
    percentage: Annotated[float, Field(multiple_of=0.01)]
