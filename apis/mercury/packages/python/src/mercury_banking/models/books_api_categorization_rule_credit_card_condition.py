# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from uuid import UUID
from mercury_banking._runtime import ApiModel


class BooksAPICategorizationRuleCreditCardCondition(ApiModel):
    """BooksAPICategorizationRuleCreditCardCondition model."""

    credit_card_id: UUID = Field(alias="creditCardId")
