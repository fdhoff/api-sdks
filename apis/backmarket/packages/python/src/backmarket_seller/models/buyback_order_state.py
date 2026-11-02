# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BuybackOrderState(str, Enum):
    """Allowed values of BuybackOrderState."""

    NEW = "NEW"
    PENDING = "PENDING"
    TO_SEND = "TO_SEND"
    SENT = "SENT"
    RECEIVED = "RECEIVED"
    COUNTER_PROPOSAL = "COUNTER_PROPOSAL"
    VALIDATED = "VALIDATED"
    PAID = "PAID"
    MONEY_TRANSFERED = "MONEY_TRANSFERED"
    SUSPENDED = "SUSPENDED"
