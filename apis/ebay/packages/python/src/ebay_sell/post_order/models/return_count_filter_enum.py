# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ReturnCountFilterEnum(str, Enum):
    """Allowed values of ReturnCountFilterEnum."""

    RETURN_STARTED = "RETURN_STARTED"
    ITEM_SHIPPED = "ITEM_SHIPPED"
    ITEM_DELIVERED = "ITEM_DELIVERED"
    CLOSED = "CLOSED"
    ALL_OPEN_REPLACEMENT = "ALL_OPEN_REPLACEMENT"
    ALL_OPEN = "ALL_OPEN"
    ALL_OPEN_RETURN = "ALL_OPEN_RETURN"
    SELLER_ACTION_DUE = "SELLER_ACTION_DUE"
    SELLER_ACTION_OVERDUE = "SELLER_ACTION_OVERDUE"
    SELLER_NO_ACTION = "SELLER_NO_ACTION"
    EBAY_PLUS = "EBAY_PLUS"
    UNKNOWN = "UNKNOWN"
