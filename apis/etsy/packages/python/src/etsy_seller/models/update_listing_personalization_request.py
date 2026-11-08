# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List
from etsy_seller.models.update_listing_personalization_request_personalization_questions_inner import (
    UpdateListingPersonalizationRequestPersonalizationQuestionsInner,
)
from etsy_seller._runtime import ApiModel


class UpdateListingPersonalizationRequest(ApiModel):
    """UpdateListingPersonalizationRequest model."""

    personalization_questions: List[UpdateListingPersonalizationRequestPersonalizationQuestionsInner]
