# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.api_v1_budget_member import ApiV1BudgetMember
from mercury_banking.models.api_v1_budget_members_response_page import ApiV1BudgetMembersResponsePage
from mercury_banking._runtime import ApiModel


class ApiV1BudgetMembersResponse(ApiModel):
    """ApiV1BudgetMembersResponse model."""

    members: List[ApiV1BudgetMember]
    page: ApiV1BudgetMembersResponsePage
