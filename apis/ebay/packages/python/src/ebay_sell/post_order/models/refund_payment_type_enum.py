# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class RefundPaymentTypeEnum(str, Enum):
    """Allowed values of RefundPaymentTypeEnum."""

    INSTANT_REFUND = "INSTANT_REFUND"
    ECHECK = "ECHECK"
    PAYOUT = "PAYOUT"
    INTERMEDIATED_REFUND = "INTERMEDIATED_REFUND"
    OTHER = "OTHER"
