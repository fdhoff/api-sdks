# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class CanMoneyMovementStatusEnum(str, Enum):
    """Allowed values of CanMoneyMovementStatusEnum."""

    UNKNOWN = "UNKNOWN"
    REQUESTED = "REQUESTED"
    PENDING = "PENDING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"
