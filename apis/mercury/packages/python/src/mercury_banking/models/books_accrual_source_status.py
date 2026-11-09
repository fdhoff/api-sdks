# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BooksAccrualSourceStatus(str, Enum):
    """Allowed values of BooksAccrualSourceStatus."""

    OPEN = "open"
    PAID = "paid"
    DRAFT = "draft"
    CANCELLED = "cancelled"
    PROCESSING = "processing"
