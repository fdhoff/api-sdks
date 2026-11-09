# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BooksNeedsActionReason(str, Enum):
    """Allowed values of BooksNeedsActionReason."""

    TRANSACTIONNOTINTEAL = "transactionNotInTeal"
    TRANSACTIONAMOUNTEXCEEDSINVOICEBALANCE = "transactionAmountExceedsInvoiceBalance"
    TRANSACTIONAMOUNTDOESNOTCOVERINVOICES = "transactionAmountDoesNotCoverInvoices"
    SOURCEACCOUNTNOTMAPPED = "sourceAccountNotMapped"
    TRANSACTIONPREDATESBOOKSSTARTDATE = "transactionPredatesBooksStartDate"
    TRANSACTIONAPPLIEDTOOTHERINVOICES = "transactionAppliedToOtherInvoices"
    CARDCHARGESTRIPENOTCONNECTED = "cardChargeStripeNotConnected"
    CARDCHARGESTRIPESETUPPENDING = "cardChargeStripeSetupPending"
