# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class RetEligibilityCheckTypeEnum(str, Enum):
    """Allowed values of RetEligibilityCheckTypeEnum."""

    ITEM_SELECTION = "ITEM_SELECTION"
    RETURN_CREATION = "RETURN_CREATION"
    PRE_TRANSACTION = "PRE_TRANSACTION"
    UNPAID_TRANSACTION = "UNPAID_TRANSACTION"
    RETURN_REASON_SELECTION = "RETURN_REASON_SELECTION"
    REPLACEMENT_CREATION = "REPLACEMENT_CREATION"
    REPLACEMENT_ITEM_SELECTION = "REPLACEMENT_ITEM_SELECTION"
