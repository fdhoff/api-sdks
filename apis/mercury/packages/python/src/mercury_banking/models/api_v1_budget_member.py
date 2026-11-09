# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking._runtime import ApiModel


class ApiV1BudgetMember(ApiModel):
    """ApiV1BudgetMember model."""

    cycle_remaining: Annotated[float, Field(ge=0)] = Field(alias="cycleRemaining")
    cycle_spent: Annotated[float, Field(ge=0)] = Field(alias="cycleSpent")
    email: StrictStr
    first_name: StrictStr = Field(alias="firstName")
    last_name: StrictStr = Field(alias="lastName")
    org_user_id: UUID = Field(alias="orgUserId")
