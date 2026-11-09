# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class CancelStateEnum(str, Enum):
    """Allowed values of CancelStateEnum."""

    INITIAL = "INITIAL"
    REFUND_PENDING = "REFUND_PENDING"
    REFUND_INITIATED = "REFUND_INITIATED"
    APPROVAL_PENDING = "APPROVAL_PENDING"
    CONFIRM_REFUND_PENDING = "CONFIRM_REFUND_PENDING"
    CLOSED = "CLOSED"
    REFUND_FAILED_RETRY = "REFUND_FAILED_RETRY"
    OTHER = "OTHER"
