# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BuyerCloseReasonEnum(str, Enum):
    """Allowed values of BuyerCloseReasonEnum."""

    ITEM_ARRIVED = "ITEM_ARRIVED"
    WORKED_OUT_WITH_SELLER = "WORKED_OUT_WITH_SELLER"
    WOULD_RATHER_KEEP_THE_ITEM = "WOULD_RATHER_KEEP_THE_ITEM"
    OTHER = "OTHER"
