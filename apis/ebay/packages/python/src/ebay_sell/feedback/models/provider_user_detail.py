# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feedback.models.provider_user_detail_user_attributes import ProviderUserDetailUserAttributes
from ebay_sell._runtime import ApiModel


class ProviderUserDetail(ApiModel):
    """ProviderUserDetail model."""

    feedback_score: Optional[StrictInt] = Field(default=None, alias="feedbackScore")
    feedback_star: Optional[StrictStr] = Field(default=None, alias="feedbackStar")
    role: Optional[StrictStr] = None
    user_attributes: Optional[List[ProviderUserDetailUserAttributes]] = Field(default=None, alias="userAttributes")
    user_id: Optional[StrictStr] = Field(default=None, alias="userId")
