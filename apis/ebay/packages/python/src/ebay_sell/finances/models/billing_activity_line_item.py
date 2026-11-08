# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.finances.models.amount import Amount
from ebay_sell.finances.models.discount_detail import DiscountDetail
from ebay_sell._runtime import ApiModel


class BillingActivityLineItem(ApiModel):
    """BillingActivityLineItem model."""

    amount: Optional[Amount] = None
    billing_transaction_date: Optional[StrictStr] = Field(default=None, alias="billingTransactionDate")
    billing_transaction_id: Optional[StrictStr] = Field(default=None, alias="billingTransactionId")
    booking_entry: Optional[StrictStr] = Field(default=None, alias="bookingEntry")
    fee_type: Optional[StrictStr] = Field(default=None, alias="feeType")
    fee_type_description: Optional[StrictStr] = Field(default=None, alias="feeTypeDescription")
    listing_id: Optional[StrictStr] = Field(default=None, alias="listingId")
    order_id: Optional[StrictStr] = Field(default=None, alias="orderId")
    promotional_offers: Optional[List[DiscountDetail]] = Field(default=None, alias="promotionalOffers")
