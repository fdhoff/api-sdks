# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.api_v1_spend_budget_response import ApiV1SpendBudgetResponse
from mercury_banking.models.api_v1_spend_budgets_response_page import ApiV1SpendBudgetsResponsePage
from mercury_banking._runtime import ApiModel


class ApiV1SpendBudgetsResponse(ApiModel):
    """ApiV1SpendBudgetsResponse model."""

    budgets: List[ApiV1SpendBudgetResponse]
    page: ApiV1SpendBudgetsResponsePage
