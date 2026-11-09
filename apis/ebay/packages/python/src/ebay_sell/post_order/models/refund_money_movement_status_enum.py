# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class RefundMoneyMovementStatusEnum(str, Enum):
    """Allowed values of RefundMoneyMovementStatusEnum."""

    REQUESTED = "REQUESTED"
    SUCCESS = "SUCCESS"
    PENDING = "PENDING"
    FAILED = "FAILED"
    UNKNOWN = "UNKNOWN"
