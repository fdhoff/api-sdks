# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BuybackMessageAuthor(str, Enum):
    """Allowed values of BuybackMessageAuthor."""

    MERCHANT = "Merchant"
    CLIENT = "Client"
    BACKMARKET = "BackMarket"
    UNKNOWN = "Unknown"
