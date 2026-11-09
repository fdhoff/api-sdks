# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class TreasuryStatementDocumentType(str, Enum):
    """Allowed values of TreasuryStatementDocumentType."""

    MONTHLYSTATEMENT = "MonthlyStatement"
    TRADECONFIRMATION = "TradeConfirmation"
    ENUM_1099 = "1099"
    ENUM_1099R = "1099R"
    ENUM_1042S = "1042S"
    ENUM_5498 = "5498"
    ENUM_5498ESA = "5498ESA"
    ENUM_1099Q = "1099Q"
    FMV = "FMV"
    SDIRA = "SDIRA"
