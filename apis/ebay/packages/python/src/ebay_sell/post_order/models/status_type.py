# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class StatusType(str, Enum):
    """Allowed values of StatusType."""

    SUCCESS = "SUCCESS"
    SELLER_APPROVAL = "SELLER_APPROVAL"
    FAILED = "FAILED"
    WARNING = "WARNING"
    UNKNOWN = "UNKNOWN"
