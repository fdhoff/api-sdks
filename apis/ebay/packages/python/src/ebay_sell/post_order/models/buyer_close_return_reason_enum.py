# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BuyerCloseReturnReasonEnum(str, Enum):
    """Allowed values of BuyerCloseReturnReasonEnum."""

    UNKNOWN = "UNKNOWN"
    BUYER_RECEIVED_REFUND = "BUYER_RECEIVED_REFUND"
    BUYER_RECEIVED_REPLACEMENT = "BUYER_RECEIVED_REPLACEMENT"
    BUYER_STARTED_RETURN_ACCIDENTALLY = "BUYER_STARTED_RETURN_ACCIDENTALLY"
    CHARGE_BACK_OPENED = "CHARGE_BACK_OPENED"
    BUYER_NO_LONGER_WANTS_RETURN = "BUYER_NO_LONGER_WANTS_RETURN"
    OTHER = "OTHER"
