# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.marketing.models.budget_recommendation_response import BudgetRecommendationResponse
from ebay_sell._runtime import ApiModel


class SuggestBudgetResponse(ApiModel):
    """SuggestBudgetResponse model."""

    suggested_budget: Optional[List[BudgetRecommendationResponse]] = Field(default=None, alias="suggestedBudget")
