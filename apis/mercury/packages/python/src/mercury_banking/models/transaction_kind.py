# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class TransactionKind(str, Enum):
    """Allowed values of TransactionKind."""

    EXTERNALTRANSFER = "externalTransfer"
    INTERNALTRANSFER = "internalTransfer"
    OUTGOINGPAYMENT = "outgoingPayment"
    CREDITCARDCREDIT = "creditCardCredit"
    CREDITCARDTRANSACTION = "creditCardTransaction"
    DEBITCARDCREDIT = "debitCardCredit"
    DEBITCARDTRANSACTION = "debitCardTransaction"
    CARDINTERNATIONALTRANSACTIONFEE = "cardInternationalTransactionFee"
    CARDINTERNATIONALTRANSACTIONFEEREBATE = "cardInternationalTransactionFeeRebate"
    CARDINTERNATIONALTRANSACTIONFEEREVERSAL = "cardInternationalTransactionFeeReversal"
    CARDINTERNATIONALTRANSACTIONFEEREBATEREVERSAL = "cardInternationalTransactionFeeRebateReversal"
    INCOMINGDOMESTICWIRE = "incomingDomesticWire"
    CHECKDEPOSIT = "checkDeposit"
    INCOMINGINTERNATIONALWIRE = "incomingInternationalWire"
    TREASURYTRANSFER = "treasuryTransfer"
    CURRENCYCLOUDRETURN = "currencyCloudReturn"
    WIREFEE = "wireFee"
    PERSONALBANKINGSUBSCRIPTIONFEE = "personalBankingSubscriptionFee"
    BILLINGENGINESUBSCRIPTIONFEE = "billingEngineSubscriptionFee"
    EXPENSEREIMBURSEMENT = "expenseReimbursement"
    EXOGENOUSWIREDRAWDOWN = "exogenousWireDrawdown"
    INTERESTPAYMENT = "interestPayment"
    OTHER = "other"
