# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ReimbursementPaymentStatus(str, Enum):
    """Allowed values of ReimbursementPaymentStatus."""

    PENDING = "pending"
    INITIATED = "initiated"
    PAID = "paid"
    FAILED = "failed"
