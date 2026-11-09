# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class FundingMethodTypeEnum(str, Enum):
    """Allowed values of FundingMethodTypeEnum."""

    CREDIT_CARD = "CREDIT_CARD"
    DIRECT_DEBIT = "DIRECT_DEBIT"
    PAY_UPON_INVOICE = "PAY_UPON_INVOICE"
    AVAILABLE_FUNDS = "AVAILABLE_FUNDS"
