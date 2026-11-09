# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class ElectronicAccountType(str, Enum):
    """Allowed values of ElectronicAccountType."""

    BUSINESSCHECKING = "businessChecking"
    BUSINESSSAVINGS = "businessSavings"
    PERSONALCHECKING = "personalChecking"
    PERSONALSAVINGS = "personalSavings"
    BUSINESSGENERALLEDGER = "businessGeneralLedger"
    PERSONALGENERALLEDGER = "personalGeneralLedger"
    BUSINESSLOAN = "businessLoan"
    PERSONALLOAN = "personalLoan"
