# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class TrackingStatusEnum(str, Enum):
    """Allowed values of TrackingStatusEnum."""

    DELIVERED = "DELIVERED"
    IN_TRANSIT = "IN_TRANSIT"
    CREATED = "CREATED"
    CANCELLED = "CANCELLED"
    UNKNOWN = "UNKNOWN"
