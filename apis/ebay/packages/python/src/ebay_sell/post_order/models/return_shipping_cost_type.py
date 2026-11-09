# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ReturnShippingCostType(str, Enum):
    """Allowed values of ReturnShippingCostType."""

    LABEL_COST = "LABEL_COST"
    SIGNATURE_CONFIRMATION_COST = "SIGNATURE_CONFIRMATION_COST"
    INSURANCE = "INSURANCE"
    OTHER = "OTHER"
