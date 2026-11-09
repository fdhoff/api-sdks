# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ApiEventResourceType(str, Enum):
    """Allowed values of ApiEventResourceType."""

    TRANSACTION = "transaction"
    CHECKINGACCOUNT = "checkingAccount"
    SAVINGSACCOUNT = "savingsAccount"
    TREASURYACCOUNT = "treasuryAccount"
    INVESTMENTACCOUNT = "investmentAccount"
    CREDITACCOUNT = "creditAccount"
