# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feedback.models.rating_summary_by_rating_type import RatingSummaryByRatingType
from ebay_sell._runtime import ApiModel


class FeedbackRatingSummary(ApiModel):
    """FeedbackRatingSummary model."""

    rating_summary_by_rating_type: Optional[List[RatingSummaryByRatingType]] = Field(
        default=None, alias="ratingSummaryByRatingType"
    )
    rating_type: Optional[StrictStr] = Field(default=None, alias="ratingType")
