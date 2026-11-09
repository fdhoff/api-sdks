# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class CanMoneyMovementTypeEnum(str, Enum):
    """Allowed values of CanMoneyMovementTypeEnum."""

    UNKNOWN = "UNKNOWN"
    SELLER_VOLUNTARY_REFUND = "SELLER_VOLUNTARY_REFUND"
    PAYPAL_REFUND = "PAYPAL_REFUND"
    BUYER_PAYOUT = "BUYER_PAYOUT"
    RECOUP_FROM_SELLER = "RECOUP_FROM_SELLER"
