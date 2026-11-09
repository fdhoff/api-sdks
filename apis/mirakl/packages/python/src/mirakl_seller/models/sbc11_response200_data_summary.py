# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from mirakl_seller._runtime import ApiModel


class SBC11Response200DataSummary(ApiModel):
    """SBC11Response200DataSummary model."""

    total_commissions_excl_tax: Optional[float] = None
    total_commissions_incl_tax: Optional[float] = None
    total_fee_excl_tax: Optional[float] = None
    total_fee_incl_tax: Optional[float] = None
    total_fee_operator_remitted_excl_tax: Optional[float] = None
    total_fee_operator_remitted_incl_tax: Optional[float] = None
    total_mirakl_ads_credit_excl_tax: Optional[float] = None
    total_mirakl_ads_credit_incl_tax: Optional[float] = None
    total_mirakl_ads_debit_excl_tax: Optional[float] = None
    total_mirakl_ads_debit_incl_tax: Optional[float] = None
    total_non_payable_orders_excl_tax: Optional[float] = None
    total_non_payable_orders_incl_tax: Optional[float] = None
    total_operator_paid_shipping_charges_excl_tax: Optional[float] = None
    total_operator_paid_shipping_charges_incl_tax: Optional[float] = None
    total_operator_remitted_taxes: Optional[float] = None
    total_other_credits_excl_tax: Optional[float] = None
    total_other_credits_incl_tax: Optional[float] = None
    total_other_invoices_excl_tax: Optional[float] = None
    total_other_invoices_incl_tax: Optional[float] = None
    total_payable_orders_excl_tax: Optional[float] = None
    total_payable_orders_incl_tax: Optional[float] = None
    total_purchase_taxes: Optional[float] = None
    total_refund_commissions_excl_tax: Optional[float] = None
    total_refund_commissions_incl_tax: Optional[float] = None
    total_refund_fee_excl_tax: Optional[float] = None
    total_refund_fee_incl_tax: Optional[float] = None
    total_refund_fee_operator_remitted_excl_tax: Optional[float] = None
    total_refund_fee_operator_remitted_incl_tax: Optional[float] = None
    total_refund_non_payable_orders_excl_tax: Optional[float] = None
    total_refund_non_payable_orders_incl_tax: Optional[float] = None
    total_refund_operator_paid_shipping_charges_excl_tax: Optional[float] = None
    total_refund_operator_paid_shipping_charges_incl_tax: Optional[float] = None
    total_refund_operator_remitted_taxes: Optional[float] = None
    total_refund_orders_excl_tax: Optional[float] = None
    total_refund_orders_incl_tax: Optional[float] = None
    total_refund_payable_orders_excl_tax: Optional[float] = None
    total_refund_payable_orders_incl_tax: Optional[float] = None
    total_refund_purchase_taxes: Optional[float] = None
    total_seller_fees_on_orders_excl_tax: Optional[float] = None
    total_seller_fees_on_orders_incl_tax: Optional[float] = None
    total_seller_penalty_fees_excl_tax: Optional[float] = None
    total_seller_penalty_fees_incl_tax: Optional[float] = None
    total_subscription_excl_tax: Optional[float] = None
    total_subscription_incl_tax: Optional[float] = None
