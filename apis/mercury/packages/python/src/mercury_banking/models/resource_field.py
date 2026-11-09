# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ResourceField(str, Enum):
    """Allowed values of ResourceField."""

    TRANSACTION_DOT_AMOUNT = "transaction.amount"
    TRANSACTION_DOT_BANK_DESCRIPTION = "transaction.bankDescription"
    TRANSACTION_DOT_CATEGORY_DATA = "transaction.categoryData"
    TRANSACTION_DOT_CUSTOM_CATEGORY = "transaction.customCategory"
    TRANSACTION_DOT_CUSTOM_CATEGORY_DOT_ID = "transaction.customCategory.id"
    TRANSACTION_DOT_CUSTOM_CATEGORY_DOT_NAME = "transaction.customCategory.name"
    TRANSACTION_DOT_MERCURY_CATEGORY = "transaction.mercuryCategory"
    TRANSACTION_DOT_ESTIMATED_DELIVERY_DATE = "transaction.estimatedDeliveryDate"
    TRANSACTION_DOT_EXTERNAL_MEMO = "transaction.externalMemo"
    TRANSACTION_DOT_FAILED_AT = "transaction.failedAt"
    TRANSACTION_DOT_NOTE = "transaction.note"
    TRANSACTION_DOT_POSTED_AT = "transaction.postedAt"
    TRANSACTION_DOT_REASON_FOR_FAILURE = "transaction.reasonForFailure"
    TRANSACTION_DOT_STATUS = "transaction.status"
    CHECKING_ACCOUNT_DOT_AVAILABLE_BALANCE = "checkingAccount.availableBalance"
    CHECKING_ACCOUNT_DOT_CURRENT_BALANCE = "checkingAccount.currentBalance"
    CHECKING_ACCOUNT_DOT_IN_FLIGHT_BALANCE = "checkingAccount.inFlightBalance"
    SAVINGS_ACCOUNT_DOT_AVAILABLE_BALANCE = "savingsAccount.availableBalance"
    SAVINGS_ACCOUNT_DOT_CURRENT_BALANCE = "savingsAccount.currentBalance"
    SAVINGS_ACCOUNT_DOT_IN_FLIGHT_BALANCE = "savingsAccount.inFlightBalance"
    TREASURY_ACCOUNT_DOT_AVAILABLE_BALANCE = "treasuryAccount.availableBalance"
    TREASURY_ACCOUNT_DOT_CURRENT_BALANCE = "treasuryAccount.currentBalance"
    TREASURY_ACCOUNT_DOT_IN_FLIGHT_BALANCE = "treasuryAccount.inFlightBalance"
    INVESTMENT_ACCOUNT_DOT_AVAILABLE_BALANCE = "investmentAccount.availableBalance"
    INVESTMENT_ACCOUNT_DOT_CURRENT_BALANCE = "investmentAccount.currentBalance"
    INVESTMENT_ACCOUNT_DOT_IN_FLIGHT_BALANCE = "investmentAccount.inFlightBalance"
    CREDIT_ACCOUNT_DOT_AVAILABLE_BALANCE = "creditAccount.availableBalance"
    CREDIT_ACCOUNT_DOT_CURRENT_BALANCE = "creditAccount.currentBalance"
    CREDIT_ACCOUNT_DOT_IN_FLIGHT_BALANCE = "creditAccount.inFlightBalance"
