# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from mercury_banking.models.books_api_categorization_rule_credit_card_condition import (
    BooksAPICategorizationRuleCreditCardCondition,
)
from mercury_banking._runtime import ApiModel


class BooksAPICategorizationRuleConditionCreditCard(ApiModel):
    """BooksAPICategorizationRuleConditionCreditCard model."""

    contents: BooksAPICategorizationRuleCreditCardCondition
    tag: StrictStr
