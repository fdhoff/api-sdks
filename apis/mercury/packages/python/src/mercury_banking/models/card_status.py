# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class CardStatus(str, Enum):
    """Allowed values of CardStatus."""

    ACTIVE = "active"
    FROZEN = "frozen"
    CANCELLED = "cancelled"
    INACTIVE = "inactive"
    EXPIRED = "expired"
    SUSPENDED = "suspended"
    SINGLEUSECONSUMED = "singleUseConsumed"
