# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from uuid import UUID
from mercury_banking._runtime import ApiModel


class AutoTransferRuleMaintainTargetBalance(ApiModel):
    """AutoTransferRuleMaintainTargetBalance model."""

    lower_bound: Optional[float] = Field(default=None, alias="lowerBound")
    reservoir_account_id: UUID = Field(alias="reservoirAccountId")
    target_balance: float = Field(alias="targetBalance")
    upper_bound: Optional[float] = Field(default=None, alias="upperBound")
