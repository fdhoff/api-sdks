# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class InquiryEscalationReasonEnum(str, Enum):
    """Allowed values of InquiryEscalationReasonEnum."""

    SELLER_NORESPONSE = "SELLER_NORESPONSE"
    TROUBLE_COMMUNICATION = "TROUBLE_COMMUNICATION"
    NOT_RECEIVED = "NOT_RECEIVED"
    NO_REFUND = "NO_REFUND"
    BUYER_UNHAPPY = "BUYER_UNHAPPY"
    BUYER_TROUBLE = "BUYER_TROUBLE"
    SHIPPED_ITEM = "SHIPPED_ITEM"
    OTHERS = "OTHERS"
