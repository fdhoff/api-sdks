# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from etsy_seller.models.money import Money
from etsy_seller.models.personalization_question_options_inner import PersonalizationQuestionOptionsInner
from etsy_seller._runtime import ApiModel


class PersonalizationQuestion(ApiModel):
    """PersonalizationQuestion model."""

    question_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = None
    question_text: Optional[StrictStr] = None
    instructions: Optional[StrictStr] = None
    question_type: Optional[StrictStr] = None
    required: Optional[StrictBool] = None
    max_allowed_characters: Optional[StrictInt] = None
    max_allowed_files: Optional[StrictInt] = None
    add_on_price: Optional[Money] = None
    options: Optional[List[PersonalizationQuestionOptionsInner]] = None
