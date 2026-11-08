# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feedback.models.awaiting_feedback import AwaitingFeedback
from ebay_sell.feedback.models.items_awaiting_feedback_count import ItemsAwaitingFeedbackCount
from ebay_sell.feedback.models.pagination import Pagination
from ebay_sell._runtime import ApiModel


class AwaitingFeedbackResponse(ApiModel):
    """AwaitingFeedbackResponse model."""

    items_awaiting_feedback_count: Optional[ItemsAwaitingFeedbackCount] = Field(
        default=None, alias="itemsAwaitingFeedbackCount"
    )
    line_items: Optional[List[AwaitingFeedback]] = Field(default=None, alias="lineItems")
    pagination: Optional[Pagination] = None
