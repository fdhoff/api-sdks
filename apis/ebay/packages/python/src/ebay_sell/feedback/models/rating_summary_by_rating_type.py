# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feedback.models.feedback_metrics import FeedbackMetrics
from ebay_sell.feedback.models.feedback_rating_value_distribution import FeedbackRatingValueDistribution
from ebay_sell.feedback.models.period import Period
from ebay_sell._runtime import ApiModel


class RatingSummaryByRatingType(ApiModel):
    """RatingSummaryByRatingType model."""

    feedback_metrics: Optional[List[FeedbackMetrics]] = Field(default=None, alias="feedbackMetrics")
    feedback_rating_value_distribution: Optional[List[FeedbackRatingValueDistribution]] = Field(
        default=None, alias="feedbackRatingValueDistribution"
    )
    period: Optional[Period] = None
    user_role_type: Optional[StrictStr] = Field(default=None, alias="userRoleType")
