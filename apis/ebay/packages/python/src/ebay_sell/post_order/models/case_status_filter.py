# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class CaseStatusFilter(str, Enum):
    """Allowed values of CaseStatusFilter."""

    WAITING_DELIVERY = "WAITING_DELIVERY"
    WAITING_CS = "WAITING_CS"
    OPEN = "OPEN"
    ON_HOLD = "ON_HOLD"
    REFUND_AGREED_BUT_FAILED = "REFUND_AGREED_BUT_FAILED"
    CLOSED = "CLOSED"
    CS_CLOSED = "CS_CLOSED"
    OTHER = "OTHER"
