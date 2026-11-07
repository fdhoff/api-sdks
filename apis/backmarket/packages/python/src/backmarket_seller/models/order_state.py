# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class OrderState(int, Enum):
    """Allowed values of OrderState."""

    CREATED = 0
    PENDING_PAYMENT = 10
    PAYMENT_VALIDATED = 1
    PENDING_SHIPMENT = 3
    NOT_PAID = 8
    SHIPPED = 9
