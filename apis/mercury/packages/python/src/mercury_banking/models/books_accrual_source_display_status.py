# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BooksAccrualSourceDisplayStatus(str, Enum):
    """Allowed values of BooksAccrualSourceDisplayStatus."""

    OPEN = "open"
    PAID = "paid"
    DRAFT = "draft"
    CANCELLED = "cancelled"
    OVERDUE = "overdue"
    PARTIALLYPAID = "partiallyPaid"
    PROCESSING = "processing"
