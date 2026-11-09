# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BooksCategorizerType(str, Enum):
    """Allowed values of BooksCategorizerType."""

    AI = "aI"
    RULES = "rules"
    SIMILARITY = "similarity"
    TRANSFERBETWEENACCOUNTS = "transferBetweenAccounts"
    UNCATEGORIZED = "uncategorized"
    USER = "user"
