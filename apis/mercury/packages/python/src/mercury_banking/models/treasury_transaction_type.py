# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class TreasuryTransactionType(str, Enum):
    """Allowed values of TreasuryTransactionType."""

    DEPOSITCANCELED = "depositCanceled"
    DEPOSITCOMPLETE = "depositComplete"
    DEPOSITFAILED = "depositFailed"
    DEPOSITRETURNED = "depositReturned"
    MERCURYFEEPOSTED = "mercuryFeePosted"
    MERCURYFEEFAILED = "mercuryFeeFailed"
    MERCURYFEEREFUNDED = "mercuryFeeRefunded"
    MERCURYFEECANCELED = "mercuryFeeCanceled"
    WITHDRAWALPOSTED = "withdrawalPosted"
    WITHDRAWALFAILED = "withdrawalFailed"
    WITHDRAWALCANCELED = "withdrawalCanceled"
    WITHDRAWALRETURNED = "withdrawalReturned"
    REVERTTXN = "revertTxn"
    INTERESTPOSTED = "interestPosted"
    INTERESTCANCELED = "interestCanceled"
    MANUALAMENDMENTPOSTED = "manualAmendmentPosted"
    MERCURYCREDITPOSTED = "mercuryCreditPosted"
    MERCURYCREDITFAILED = "mercuryCreditFailed"
    DIVIDENDPOSTED = "dividendPosted"
    DIVIDENDCANCELED = "dividendCanceled"
    DIVIDENDREINVESTMENTPOSTED = "dividendReinvestmentPosted"
    MUTUALFUNDTRADEFAILED = "mutualFundTradeFailed"
    MUTUALFUNDTRADEPOSTED = "mutualFundTradePosted"
    SWEEPINPOSTED = "sweepInPosted"
    SWEEPOUTPOSTED = "sweepOutPosted"
    SWEEPRECONCILEPOSTED = "sweepReconcilePosted"
    VALUATIONCHANGEPOSTED = "valuationChangePosted"
    OEMSMUTUALFUNDORDERSETTLED = "oemsMutualFundOrderSettled"
    OEMSMUTUALFUNDORDERCANCELED = "oemsMutualFundOrderCanceled"
    OEMSMUTUALFUNDORDERREJECTED = "oemsMutualFundOrderRejected"
    OEMSFIXEDINCOMEORDERSETTLED = "oemsFixedIncomeOrderSettled"
    OEMSFIXEDINCOMEORDERCANCELED = "oemsFixedIncomeOrderCanceled"
    OEMSFIXEDINCOMEORDERREJECTED = "oemsFixedIncomeOrderRejected"
    COUPONPOSTED = "couponPosted"
    COUPONCANCELED = "couponCanceled"
    MATURITYPOSTED = "maturityPosted"
    MATURITYCANCELED = "maturityCanceled"
