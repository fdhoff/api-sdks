# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BooksJournalEntryCreationSource(str, Enum):
    """Allowed values of BooksJournalEntryCreationSource."""

    MANUAL = "manual"
    TRANSACTION = "transaction"
    ACCRUAL = "accrual"
    PAYMENTAPPLICATION = "paymentApplication"
    LEGACY = "legacy"
