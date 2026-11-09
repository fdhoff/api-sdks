# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class InquiryStatusEnum(str, Enum):
    """Allowed values of InquiryStatusEnum."""

    PENDING = "PENDING"
    OPEN = "OPEN"
    WAITING_BUYER_RESPONSE = "WAITING_BUYER_RESPONSE"
    WAITING_SELLER_RESPONSE = "WAITING_SELLER_RESPONSE"
    CLOSED = "CLOSED"
    CS_CLOSED = "CS_CLOSED"
    CLOSED_WITH_ESCALATION = "CLOSED_WITH_ESCALATION"
    OTHER = "OTHER"
