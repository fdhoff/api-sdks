# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class OrderLineState(int, Enum):
    """Allowed values of OrderLineState."""

    CREATED = 0
    ON_HOLD = 9
    PENDING_PAYMENT = 8
    PAID = 1
    ACCEPTED = 2
    SHIPPED = 3
    CANCELLED = 4
    REFUNDED_BEFORE_SHIPPING = 5
    REFUNDED_AFTER_SHIPPING = 6
    NOT_PAID = 7
