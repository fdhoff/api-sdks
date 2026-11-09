# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class WebhookEventType(str, Enum):
    """Allowed values of WebhookEventType."""

    TRANSACTION_DOT_CREATED = "transaction.created"
    TRANSACTION_DOT_UPDATED = "transaction.updated"
    CHECKING_ACCOUNT_DOT_BALANCE_DOT_UPDATED = "checkingAccount.balance.updated"
    SAVINGS_ACCOUNT_DOT_BALANCE_DOT_UPDATED = "savingsAccount.balance.updated"
    TREASURY_ACCOUNT_DOT_BALANCE_DOT_UPDATED = "treasuryAccount.balance.updated"
    INVESTMENT_ACCOUNT_DOT_BALANCE_DOT_UPDATED = "investmentAccount.balance.updated"
    CREDIT_ACCOUNT_DOT_BALANCE_DOT_UPDATED = "creditAccount.balance.updated"
