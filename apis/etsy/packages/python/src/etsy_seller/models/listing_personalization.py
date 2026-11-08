# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from etsy_seller.models.personalization_question import PersonalizationQuestion
from etsy_seller._runtime import ApiModel


class ListingPersonalization(ApiModel):
    """ListingPersonalization model."""

    personalization_questions: Optional[List[PersonalizationQuestion]] = None
