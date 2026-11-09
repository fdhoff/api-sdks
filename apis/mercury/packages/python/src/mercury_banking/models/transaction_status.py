# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class TransactionStatus(str, Enum):
    """Allowed values of TransactionStatus."""

    PENDING = "pending"
    SENT = "sent"
    CANCELLED = "cancelled"
    FAILED = "failed"
    REVERSED = "reversed"
    BLOCKED = "blocked"
