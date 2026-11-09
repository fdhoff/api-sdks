# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ReturnSortEnum(str, Enum):
    """Allowed values of ReturnSortEnum."""

    FILING_DATE = "FILING_DATE"
    REASON = "REASON"
    STATUS = "STATUS"
    ESTIMATED_AMOUNT = "ESTIMATED_AMOUNT"
    BUYER_LOGIN_NAME = "BUYER_LOGIN_NAME"
    ACTUAL_AMOUNT = "ACTUAL_AMOUNT"
    REFUND_DUE_DATE = "REFUND_DUE_DATE"
    RETURN_ID = "RETURN_ID"
    UNKNOWN = "UNKNOWN"
