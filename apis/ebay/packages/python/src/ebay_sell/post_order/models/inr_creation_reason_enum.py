# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class INRCreationReasonEnum(str, Enum):
    """Allowed values of INRCreationReasonEnum."""

    TRACKING_INFO_UNAVAILABLE = "TRACKING_INFO_UNAVAILABLE"
    INCOMPLETE_ORDER = "INCOMPLETE_ORDER"
    ITEM_NOT_RECEIVED_TRACKING_SHOWS_DELIVERED = "ITEM_NOT_RECEIVED_TRACKING_SHOWS_DELIVERED"
    ITEM_NOT_RECEIVED_ASK_FOR_REFUND = "ITEM_NOT_RECEIVED_ASK_FOR_REFUND"
    LATE_ORDER = "LATE_ORDER"
    EMPTY_BOX = "EMPTY_BOX"
    UNKNOWN = "UNKNOWN"
