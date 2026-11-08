# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell.finances.models.buyer import Buyer
from ebay_sell.finances.models.fee_jurisdiction import FeeJurisdiction
from ebay_sell.finances.models.order_line_item import OrderLineItem
from ebay_sell.finances.models.payout_details import PayoutDetails
from ebay_sell.finances.models.reference import Reference
from ebay_sell.finances.models.tax import Tax
from ebay_sell._runtime import ApiModel


class Transaction(ApiModel):
    """Transaction model."""

    amount: Optional[Amount] = None
    booking_entry: Optional[StrictStr] = Field(default=None, alias="bookingEntry")
    buyer: Optional[Buyer] = None
    e_bay_collected_tax_amount: Optional[Amount] = Field(default=None, alias="eBayCollectedTaxAmount")
    fee_jurisdiction: Optional[FeeJurisdiction] = Field(default=None, alias="feeJurisdiction")
    fee_type: Optional[StrictStr] = Field(default=None, alias="feeType")
    order_id: Optional[StrictStr] = Field(default=None, alias="orderId")
    order_line_items: Optional[List[OrderLineItem]] = Field(default=None, alias="orderLineItems")
    payments_entity: Optional[StrictStr] = Field(default=None, alias="paymentsEntity")
    payout_details: Optional[PayoutDetails] = Field(default=None, alias="payoutDetails")
    payout_id: Optional[StrictStr] = Field(default=None, alias="payoutId")
    references: Optional[List[Reference]] = None
    sales_record_reference: Optional[StrictStr] = Field(default=None, alias="salesRecordReference")
    taxes: Optional[List[Tax]] = None
    total_fee_amount: Optional[Amount] = Field(default=None, alias="totalFeeAmount")
    total_fee_basis_amount: Optional[Amount] = Field(default=None, alias="totalFeeBasisAmount")
    transaction_date: Optional[StrictStr] = Field(default=None, alias="transactionDate")
    transaction_id: Optional[StrictStr] = Field(default=None, alias="transactionId")
    transaction_memo: Optional[StrictStr] = Field(default=None, alias="transactionMemo")
    transaction_status: Optional[StrictStr] = Field(default=None, alias="transactionStatus")
    transaction_type: Optional[StrictStr] = Field(default=None, alias="transactionType")
