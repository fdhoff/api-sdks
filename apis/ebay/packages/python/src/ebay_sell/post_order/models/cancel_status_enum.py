# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class CancelStatusEnum(str, Enum):
    """Allowed values of CancelStatusEnum."""

    INVALID = "INVALID"
    CANCEL_REQUESTED = "CANCEL_REQUESTED"
    CANCEL_PENDING = "CANCEL_PENDING"
    CANCEL_REJECTED = "CANCEL_REJECTED"
    CANCEL_CLOSED_NO_REFUND = "CANCEL_CLOSED_NO_REFUND"
    CANCEL_CLOSED_WITH_REFUND = "CANCEL_CLOSED_WITH_REFUND"
    CANCEL_CLOSED_UNKNOWN_REFUND = "CANCEL_CLOSED_UNKNOWN_REFUND"
    CANCEL_CLOSED_FOR_COMMITMENT = "CANCEL_CLOSED_FOR_COMMITMENT"
