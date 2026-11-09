# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BooksFinancialAccountType(str, Enum):
    """Allowed values of BooksFinancialAccountType."""

    BANKACCOUNT = "bankAccount"
    CREDITCARD = "creditCard"
    PAYMENTS = "payments"
    PAYROLL = "payroll"
    LOAN = "loan"
    PREPAIDCARD = "prepaidCard"
    ACCOUNTSRECEIVABLE = "accountsReceivable"
    ACCOUNTSPAYABLE = "accountsPayable"
    INVESTMENT = "investment"
    TREASURY = "treasury"
