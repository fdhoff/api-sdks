# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feedback.models.comment_comment_period import CommentCommentPeriod
from ebay_sell._runtime import ApiModel


class Comment(ApiModel):
    """Comment model."""

    comment_period: Optional[CommentCommentPeriod] = Field(default=None, alias="commentPeriod")
    comment_text: Optional[StrictStr] = Field(default=None, alias="commentText")
    comment_text_removed_per_policy: Optional[StrictBool] = Field(default=None, alias="commentTextRemovedPerPolicy")
    state: Optional[StrictStr] = None
