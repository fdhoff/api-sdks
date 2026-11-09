# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class OrderTypeEnum(str, Enum):
    """Allowed values of OrderTypeEnum."""

    IN_STORE_PICKUP = "IN_STORE_PICKUP"
    EBAY_NOW = "EBAY_NOW"
    ONLINE = "ONLINE"
    OTHER = "OTHER"
