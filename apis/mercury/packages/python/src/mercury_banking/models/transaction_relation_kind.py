# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class TransactionRelationKind(str, Enum):
    """Allowed values of TransactionRelationKind."""

    PROVISIONALCREDITREVERSALTOMERCHANTREFUND = "ProvisionalCreditReversalToMerchantRefund"
    MERCHANTREFUNDTOPROVISIONALCREDITREVERSAL = "MerchantRefundToProvisionalCreditReversal"
    MERCHANTREFUNDTOFRAUDULENTCHARGE = "MerchantRefundToFraudulentCharge"
    FRAUDULENTCHARGETOMERCHANTREFUND = "FraudulentChargeToMerchantRefund"
    PAYMENTREFUNDTOFAILEDPAYMENT = "PaymentRefundToFailedPayment"
    FAILEDPAYMENTTOPAYMENTREFUND = "FailedPaymentToPaymentRefund"
    GIFTCOMPENSATIONTOORIGINALTRANSACTION = "GiftCompensationToOriginalTransaction"
    FEEPAYMENTTOORIGINALTRANSACTION = "FeePaymentToOriginalTransaction"
    ORIGINALTRANSACTIONTOFEEPAYMENT = "OriginalTransactionToFeePayment"
    FEEPAYMENTTOFEEREBATE = "FeePaymentToFeeRebate"
    FEEREBATETOFEEPAYMENT = "FeeRebateToFeePayment"
    FEEPAYMENTTOFEEREVERSAL = "FeePaymentToFeeReversal"
    FEEREVERSALTOFEEPAYMENT = "FeeReversalToFeePayment"
    FEEREBATETOFEEREBATEREVERSAL = "FeeRebateToFeeRebateReversal"
    FEEREBATEREVERSALTOFEEREBATE = "FeeRebateReversalToFeeRebate"
    TREASURYSPLITLIQUIDATION = "TreasurySplitLiquidation"
    PROVISIONALCREDITTOORIGINALCHARGE = "ProvisionalCreditToOriginalCharge"
    ORIGINALCHARGETOPROVISIONALCREDIT = "OriginalChargeToProvisionalCredit"
    FEEATMREIMBURSEMENTTOATMTRANSACTION = "FeeAtmReimbursementToAtmTransaction"
    ATMTRANSACTIONTOFEEATMREIMBURSEMENT = "AtmTransactionToFeeAtmReimbursement"
    ATMTRANSACTIONTOATMREIMBURSEMENTREVERSAL = "AtmTransactionToAtmReimbursementReversal"
    ATMREIMBURSEMENTREVERSALTOATMTRANSACTION = "AtmReimbursementReversalToAtmTransaction"
    RETURNTOORIGINALTRANSACTION = "ReturnToOriginalTransaction"
    ORIGINALTRANSACTIONTORETURN = "OriginalTransactionToReturn"
    PROVISIONALCREDITTOREVERSAL = "ProvisionalCreditToReversal"
    REVERSALTOPROVISIONALCREDIT = "ReversalToProvisionalCredit"
    MERCHANTREFUNDTOORIGINALCHARGE = "MerchantRefundToOriginalCharge"
    ORIGINALCHARGETOMERCHANTREFUND = "OriginalChargeToMerchantRefund"
