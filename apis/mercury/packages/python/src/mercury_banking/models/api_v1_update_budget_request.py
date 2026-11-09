# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from mercury_banking.models.api_v1_budget_frequency import ApiV1BudgetFrequency
from mercury_banking._runtime import ApiModel


class ApiV1UpdateBudgetRequest(ApiModel):
    """ApiV1UpdateBudgetRequest model."""

    amount_per_user_per_period: Optional[Annotated[float, Field(ge=0)]] = Field(
        default=None, alias="amountPerUserPerPeriod"
    )
    description: Optional[StrictStr] = None
    end_date: Optional[date] = Field(default=None, alias="endDate")
    frequency: Optional[ApiV1BudgetFrequency] = None
    name: Optional[StrictStr] = None
    start_date: Optional[date] = Field(default=None, alias="startDate")
