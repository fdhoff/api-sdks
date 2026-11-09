# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class RefundType(str, Enum):
    """Allowed values of RefundType."""

    FULL = "FULL"
    PARTIAL = "PARTIAL"
    OTHER = "OTHER"
