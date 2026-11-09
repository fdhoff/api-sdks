# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from mercury_banking.models.books_api_categorization_rule import BooksAPICategorizationRule
from mercury_banking._runtime import ApiModel


class GetBooksAPICategorizationRulesResponse(ApiModel):
    """GetBooksAPICategorizationRulesResponse model."""

    next_page_token: Optional[StrictStr] = Field(default=None, alias="nextPageToken")
    rules: List[BooksAPICategorizationRule]
