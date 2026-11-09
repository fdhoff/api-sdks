# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class PostTransactionPaymentMethod(str, Enum):
    """Allowed values of PostTransactionPaymentMethod."""

    ACH = "ach"
    CHECK = "check"
    DOMESTICWIRE = "domesticWire"
    REALTIMEPAYMENT = "realTimePayment"
