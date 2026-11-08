# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell._runtime import ApiModel


class TransactionSummaryResponse(ApiModel):
    """TransactionSummaryResponse model."""

    adjustment_amount: Optional[Amount] = Field(default=None, alias="adjustmentAmount")
    adjustment_booking_entry: Optional[StrictStr] = Field(default=None, alias="adjustmentBookingEntry")
    adjustment_count: Optional[StrictInt] = Field(default=None, alias="adjustmentCount")
    balance_transfer_amount: Optional[Amount] = Field(default=None, alias="balanceTransferAmount")
    balance_transfer_booking_entry: Optional[StrictStr] = Field(default=None, alias="balanceTransferBookingEntry")
    balance_transfer_count: Optional[StrictInt] = Field(default=None, alias="balanceTransferCount")
    credit_amount: Optional[Amount] = Field(default=None, alias="creditAmount")
    credit_booking_entry: Optional[StrictStr] = Field(default=None, alias="creditBookingEntry")
    credit_count: Optional[StrictInt] = Field(default=None, alias="creditCount")
    dispute_amount: Optional[Amount] = Field(default=None, alias="disputeAmount")
    dispute_booking_entry: Optional[StrictStr] = Field(default=None, alias="disputeBookingEntry")
    dispute_count: Optional[StrictInt] = Field(default=None, alias="disputeCount")
    loan_repayment_amount: Optional[Amount] = Field(default=None, alias="loanRepaymentAmount")
    loan_repayment_booking_entry: Optional[StrictStr] = Field(default=None, alias="loanRepaymentBookingEntry")
    loan_repayment_count: Optional[StrictInt] = Field(default=None, alias="loanRepaymentCount")
    non_sale_charge_amount: Optional[Amount] = Field(default=None, alias="nonSaleChargeAmount")
    non_sale_charge_booking_entry: Optional[StrictStr] = Field(default=None, alias="nonSaleChargeBookingEntry")
    non_sale_charge_count: Optional[StrictInt] = Field(default=None, alias="nonSaleChargeCount")
    on_hold_amount: Optional[Amount] = Field(default=None, alias="onHoldAmount")
    on_hold_booking_entry: Optional[StrictStr] = Field(default=None, alias="onHoldBookingEntry")
    on_hold_count: Optional[StrictInt] = Field(default=None, alias="onHoldCount")
    purchase_amount: Optional[Amount] = Field(default=None, alias="purchaseAmount")
    purchase_booking_entry: Optional[StrictStr] = Field(default=None, alias="purchaseBookingEntry")
    purchase_count: Optional[StrictInt] = Field(default=None, alias="purchaseCount")
    refund_amount: Optional[Amount] = Field(default=None, alias="refundAmount")
    refund_booking_entry: Optional[StrictStr] = Field(default=None, alias="refundBookingEntry")
    refund_count: Optional[StrictInt] = Field(default=None, alias="refundCount")
    shipping_label_amount: Optional[Amount] = Field(default=None, alias="shippingLabelAmount")
    shipping_label_booking_entry: Optional[StrictStr] = Field(default=None, alias="shippingLabelBookingEntry")
    shipping_label_count: Optional[StrictInt] = Field(default=None, alias="shippingLabelCount")
    transfer_amount: Optional[Amount] = Field(default=None, alias="transferAmount")
    transfer_booking_entry: Optional[StrictStr] = Field(default=None, alias="transferBookingEntry")
    transfer_count: Optional[StrictInt] = Field(default=None, alias="transferCount")
    withdrawal_amount: Optional[Amount] = Field(default=None, alias="withdrawalAmount")
    withdrawal_booking_entry: Optional[StrictStr] = Field(default=None, alias="withdrawalBookingEntry")
    withdrawal_count: Optional[StrictInt] = Field(default=None, alias="withdrawalCount")
