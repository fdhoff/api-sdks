# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell._runtime import ApiModel


class RespondToFeedbackRequest(ApiModel):
    """RespondToFeedbackRequest model."""

    feedback_id: Optional[StrictStr] = Field(default=None, alias="feedbackId")
    recipient_user_id: Optional[StrictStr] = Field(default=None, alias="recipientUserId")
    response_text: Optional[StrictStr] = Field(default=None, alias="responseText")
    response_type: Optional[StrictStr] = Field(default=None, alias="responseType")
