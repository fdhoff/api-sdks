# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class BooksAPILedgerWriteErrorCode(str, Enum):
    """Allowed values of BooksAPILedgerWriteErrorCode."""

    INVALIDLEDGER = "invalidLedger"
    MISSINGPARAMETERS = "missingParameters"
    DUPLICATENAME = "duplicateName"
    DUPLICATESORTCODE = "duplicateSortCode"
    INVALIDLEDGERTYPE = "invalidLedgerType"
    INVALIDLEDGERPARENT = "invalidLedgerParent"
    INVALIDLEDGERREPORTCASHFLOW = "invalidLedgerReportCashFlow"
    DELETINGREQUIREDLEDGER = "deletingRequiredLedger"
    DELETINGLEDGERWITHACTIVITY = "deletingLedgerWithActivity"
    DELETINGLINKEDLEDGER = "deletingLinkedLedger"
    DELETINGPARENTLEDGER = "deletingParentLedger"
    MODIFYINGREQUIREDLEDGER = "modifyingRequiredLedger"
    INTEGRATIONMAPPED = "integrationMapped"
    MERCURYACCOUNTLEDGER = "mercuryAccountLedger"
    UNKNOWNERROR = "unknownError"
