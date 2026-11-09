# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BooksAPICategorizationRuleAmountOperator(str, Enum):
    """Allowed values of BooksAPICategorizationRuleAmountOperator."""

    LESSTHAN = "lessThan"
    LESSTHANOREQUALTO = "lessThanOrEqualTo"
    GREATERTHAN = "greaterThan"
    GREATERTHANOREQUALTO = "greaterThanOrEqualTo"
    EQUALTO = "equalTo"
