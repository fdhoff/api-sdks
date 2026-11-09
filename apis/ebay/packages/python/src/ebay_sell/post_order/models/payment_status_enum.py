# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class PaymentStatusEnum(str, Enum):
    """Allowed values of PaymentStatusEnum."""

    UNKNOWN = "UNKNOWN"
    PAYPAL_PAID = "PAYPAL_PAID"
    ONLINE_PAID = "ONLINE_PAID"
    MARK_AS_PAID = "MARK_AS_PAID"
    NOT_PAID = "NOT_PAID"
