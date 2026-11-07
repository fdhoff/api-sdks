# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ReturnReason(int, Enum):
    """Allowed values of ReturnReason."""

    STOCK_MISTAKE = 0
    WITHDRAWAL = 1
    NOT_AT_ADDRESS = 11
    NOT_DELIVERED = 12
    LOST_PARCEL = 13
    FAULTY_ON_ARRIVAL = 21
    FAILED_ON_FIRST_USE = 22
    FAILED_UNDER_WARRANTY = 23
    NON_COMPLIANT = 24
    OTHER = 25
