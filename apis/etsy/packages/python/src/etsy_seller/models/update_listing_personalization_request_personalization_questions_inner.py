# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.update_listing_personalization_request_personalization_questions_inner_options_inner import (
    UpdateListingPersonalizationRequestPersonalizationQuestionsInnerOptionsInner,
)
from etsy_seller._runtime import ApiModel


class UpdateListingPersonalizationRequestPersonalizationQuestionsInner(ApiModel):
    """UpdateListingPersonalizationRequestPersonalizationQuestionsInner model."""

    question_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    question_text: StrictStr
    instructions: Optional[StrictStr] = None
    question_type: StrictStr
    required: StrictBool
    max_allowed_files: Optional[StrictInt] = None
    max_allowed_characters: Optional[StrictInt] = None
    options: Optional[List[UpdateListingPersonalizationRequestPersonalizationQuestionsInnerOptionsInner]] = None
    add_on_price: Optional[float] = None
