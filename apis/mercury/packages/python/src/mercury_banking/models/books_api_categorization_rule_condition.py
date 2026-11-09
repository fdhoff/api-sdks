# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from mercury_banking.models.books_api_categorization_rule_condition_amount import (
    BooksAPICategorizationRuleConditionAmount,
)
from mercury_banking.models.books_api_categorization_rule_condition_counterparty import (
    BooksAPICategorizationRuleConditionCounterparty,
)
from mercury_banking.models.books_api_categorization_rule_condition_credit_card import (
    BooksAPICategorizationRuleConditionCreditCard,
)
from mercury_banking.models.books_api_categorization_rule_condition_custom_category import (
    BooksAPICategorizationRuleConditionCustomCategory,
)
from mercury_banking.models.books_api_categorization_rule_condition_debit_card import (
    BooksAPICategorizationRuleConditionDebitCard,
)
from mercury_banking.models.books_api_categorization_rule_condition_description import (
    BooksAPICategorizationRuleConditionDescription,
)
from mercury_banking.models.books_api_categorization_rule_condition_user import BooksAPICategorizationRuleConditionUser
from typing import Union

BooksAPICategorizationRuleCondition = Union[
    BooksAPICategorizationRuleConditionAmount,
    BooksAPICategorizationRuleConditionDescription,
    BooksAPICategorizationRuleConditionCounterparty,
    BooksAPICategorizationRuleConditionDebitCard,
    BooksAPICategorizationRuleConditionCreditCard,
    BooksAPICategorizationRuleConditionUser,
    BooksAPICategorizationRuleConditionCustomCategory,
]
