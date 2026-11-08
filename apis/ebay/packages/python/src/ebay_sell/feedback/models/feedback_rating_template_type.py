# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.feedback.models.feedback_rating_acceptable_value import FeedbackRatingAcceptableValue
from ebay_sell._runtime import ApiModel


class FeedbackRatingTemplateType(ApiModel):
    """FeedbackRatingTemplateType model."""

    acceptable_values: Optional[List[FeedbackRatingAcceptableValue]] = Field(default=None, alias="acceptableValues")
    default_value: Optional[StrictStr] = Field(default=None, alias="defaultValue")
    early_feedback_message: Optional[StrictStr] = Field(default=None, alias="earlyFeedbackMessage")
    enabled: Optional[StrictBool] = None
    maximum_characters_allowed: Optional[StrictInt] = Field(default=None, alias="maximumCharactersAllowed")
    multi_value_rating: Optional[StrictBool] = Field(default=None, alias="multiValueRating")
    rating_key: Optional[StrictStr] = Field(default=None, alias="ratingKey")
    rating_label: Optional[StrictStr] = Field(default=None, alias="ratingLabel")
    rating_value_type: Optional[StrictStr] = Field(default=None, alias="ratingValueType")
    required: Optional[StrictBool] = None
