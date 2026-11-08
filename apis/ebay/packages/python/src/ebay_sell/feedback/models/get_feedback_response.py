# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feedback.models.feedback_detail import FeedbackDetail
from ebay_sell.feedback.models.pagination import Pagination
from ebay_sell._runtime import ApiModel


class GetFeedbackResponse(ApiModel):
    """GetFeedbackResponse model."""

    feedback_entries: Optional[List[FeedbackDetail]] = Field(default=None, alias="feedbackEntries")
    pagination: Optional[Pagination] = None
