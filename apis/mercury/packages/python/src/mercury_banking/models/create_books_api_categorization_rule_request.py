# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from mercury_banking.models.books_api_categorization_rule_condition import BooksAPICategorizationRuleCondition
from mercury_banking.models.books_api_categorization_rule_output import BooksAPICategorizationRuleOutput
from mercury_banking._runtime import ApiModel


class CreateBooksAPICategorizationRuleRequest(ApiModel):
    """CreateBooksAPICategorizationRuleRequest model."""

    conditions: Annotated[List[BooksAPICategorizationRuleCondition], Field(min_length=1)]
    outputs: Annotated[List[BooksAPICategorizationRuleOutput], Field(min_length=1)]
