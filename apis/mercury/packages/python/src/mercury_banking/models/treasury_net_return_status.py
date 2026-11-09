# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class TreasuryNetReturnStatus(str, Enum):
    """Allowed values of TreasuryNetReturnStatus."""

    PROCESSING = "processing"
    PENDING = "pending"
    CHARGED = "charged"
    ERROR = "error"
