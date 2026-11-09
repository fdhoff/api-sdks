# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.books_api_categorization_rule_condition import BooksAPICategorizationRuleCondition
from mercury_banking.models.books_api_categorization_rule_output import BooksAPICategorizationRuleOutput
from mercury_banking.models.books_api_categorization_rule_status import BooksAPICategorizationRuleStatus
from mercury_banking._runtime import ApiModel


class BooksAPICategorizationRule(ApiModel):
    """BooksAPICategorizationRule model."""

    conditions: Annotated[List[BooksAPICategorizationRuleCondition], Field(min_length=1)]
    gl_code_name: Optional[StrictStr] = Field(default=None, alias="glCodeName")
    id: UUID
    last_applied: Optional[StrictStr] = Field(default=None, alias="lastApplied")
    outputs: Annotated[List[BooksAPICategorizationRuleOutput], Field(min_length=1)]
    status: BooksAPICategorizationRuleStatus
