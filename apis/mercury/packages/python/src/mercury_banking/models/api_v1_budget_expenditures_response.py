# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.api_v1_budget_expenditure import ApiV1BudgetExpenditure
from mercury_banking.models.api_v1_budget_expenditures_response_page import ApiV1BudgetExpendituresResponsePage
from mercury_banking._runtime import ApiModel


class ApiV1BudgetExpendituresResponse(ApiModel):
    """ApiV1BudgetExpendituresResponse model."""

    expenditures: List[ApiV1BudgetExpenditure]
    page: ApiV1BudgetExpendituresResponsePage
