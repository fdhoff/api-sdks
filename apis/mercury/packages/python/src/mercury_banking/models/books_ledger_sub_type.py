# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BooksLedgerSubType(str, Enum):
    """Allowed values of BooksLedgerSubType."""

    CURRENTASSETS = "currentAssets"
    NONCURRENTASSETS = "nonCurrentAssets"
    TRANSFERSBETWEENACCOUNTS = "transfersBetweenAccounts"
    UNCATEGORIZEDASSETS = "uncategorizedAssets"
    CURRENTLIABILITIES = "currentLiabilities"
    NONCURRENTLIABILITIES = "nonCurrentLiabilities"
    EQUITY = "equity"
    OPERATINGREVENUES = "operatingRevenues"
    OTHERINCOME = "otherIncome"
    COSTOFGOODSSOLD = "costOfGoodsSold"
    OPERATINGEXPENSES = "operatingExpenses"
    OTHEREXPENSES = "otherExpenses"
    RETAINEDEARNINGS = "retainedEarnings"
