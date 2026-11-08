# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feedback.models.comment import Comment
from ebay_sell.feedback.models.feedback_entered_period import FeedbackEnteredPeriod
from ebay_sell.feedback.models.feedback_rating import FeedbackRating
from ebay_sell.feedback.models.image import Image
from ebay_sell.feedback.models.order_line_item_summary import OrderLineItemSummary
from ebay_sell.feedback.models.provider_user_detail import ProviderUserDetail
from ebay_sell.feedback.models.topic import Topic
from ebay_sell._runtime import ApiModel


class FeedbackDetail(ApiModel):
    """FeedbackDetail model."""

    automated_feedback: Optional[StrictBool] = Field(default=None, alias="automatedFeedback")
    comment_type: Optional[StrictStr] = Field(default=None, alias="commentType")
    eligible_for_revision: Optional[StrictBool] = Field(default=None, alias="eligibleForRevision")
    feedback_comment: Optional[Comment] = Field(default=None, alias="feedbackComment")
    feedback_entered_date: Optional[StrictStr] = Field(default=None, alias="feedbackEnteredDate")
    feedback_entered_period: Optional[FeedbackEnteredPeriod] = Field(default=None, alias="feedbackEnteredPeriod")
    feedback_id: Optional[StrictStr] = Field(default=None, alias="feedbackId")
    feedback_ratings: Optional[List[FeedbackRating]] = Field(default=None, alias="feedbackRatings")
    feedback_score: Optional[StrictInt] = Field(default=None, alias="feedbackScore")
    feedback_state: Optional[StrictStr] = Field(default=None, alias="feedbackState")
    followup_comment: Optional[Comment] = Field(default=None, alias="followupComment")
    has_images: Optional[StrictBool] = Field(default=None, alias="hasImages")
    images: Optional[List[Image]] = None
    order_line_item_summary: Optional[OrderLineItemSummary] = Field(default=None, alias="orderLineItemSummary")
    provider_user_detail: Optional[ProviderUserDetail] = Field(default=None, alias="providerUserDetail")
    replied_before_followup: Optional[StrictBool] = Field(default=None, alias="repliedBeforeFollowup")
    reply_comment: Optional[Comment] = Field(default=None, alias="replyComment")
    topics: Optional[List[Topic]] = None
