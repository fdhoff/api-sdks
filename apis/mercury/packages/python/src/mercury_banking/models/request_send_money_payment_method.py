# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class RequestSendMoneyPaymentMethod(str, Enum):
    """Allowed values of RequestSendMoneyPaymentMethod."""

    ACH = "ach"
    CHECK = "check"
    DOMESTICWIRE = "domesticWire"
    INTERNATIONALWIRE = "internationalWire"
    REALTIMEPAYMENT = "realTimePayment"
