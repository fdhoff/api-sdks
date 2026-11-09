# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class AppealCloseReasonEnum(str, Enum):
    """Allowed values of AppealCloseReasonEnum."""

    APPEAL_BUYER_WINS = "APPEAL_BUYER_WINS"
    APPEAL_SELLER_WINS_FULL_CREDIT = "APPEAL_SELLER_WINS_FULL_CREDIT"
    APPEAL_SELLER_WINS_PARTIAL_CREDIT = "APPEAL_SELLER_WINS_PARTIAL_CREDIT"
    APPEAL_BUYER_DENIED = "APPEAL_BUYER_DENIED"
    APPEAL_SELLER_DENIED = "APPEAL_SELLER_DENIED"
    APPEAL_SELLER_WINS_FULL_CREDIT_CANCEL_RECOUP = "APPEAL_SELLER_WINS_FULL_CREDIT_CANCEL_RECOUP"
    APPEAL_BUYER_WINS_PARTIAL_CREDIT = "APPEAL_BUYER_WINS_PARTIAL_CREDIT"
    OTHER = "OTHER"
