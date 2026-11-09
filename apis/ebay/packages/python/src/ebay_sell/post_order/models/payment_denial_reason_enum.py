# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from enum import Enum


class PaymentDenialReasonEnum(str, Enum):
    """Allowed values of PaymentDenialReasonEnum."""

    PP_PAYPAL_GUEST = "PP_PAYPAL_GUEST"
    PP_DISALLOWED_DISPUTE = "PP_DISALLOWED_DISPUTE"
    PP_ADMINISTRATIVE_FRAUD_REVIEW = "PP_ADMINISTRATIVE_FRAUD_REVIEW"
    PP_CREDITCARD_CHARGEBACK = "PP_CREDITCARD_CHARGEBACK"
    PP_ELV_REVERSAL = "PP_ELV_REVERSAL"
    PP_ACH_RETURN = "PP_ACH_RETURN"
    PP_UNAUTHORIZED_TRANSACTION = "PP_UNAUTHORIZED_TRANSACTION"
    OTHER = "OTHER"
