# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.amount import Amount
from ebay_sell.fulfillment.models.buyer import Buyer
from ebay_sell.fulfillment.models.cancel_status import CancelStatus
from ebay_sell.fulfillment.models.fulfillment_start_instruction import FulfillmentStartInstruction
from ebay_sell.fulfillment.models.line_item import LineItem
from ebay_sell.fulfillment.models.payment_summary import PaymentSummary
from ebay_sell.fulfillment.models.pricing_summary import PricingSummary
from ebay_sell.fulfillment.models.program import Program
from ebay_sell._runtime import ApiModel


class Order(ApiModel):
    """Order model."""

    buyer: Optional[Buyer] = None
    buyer_checkout_notes: Optional[StrictStr] = Field(default=None, alias="buyerCheckoutNotes")
    cancel_status: Optional[CancelStatus] = Field(default=None, alias="cancelStatus")
    creation_date: Optional[StrictStr] = Field(default=None, alias="creationDate")
    ebay_collect_and_remit_tax: Optional[StrictBool] = Field(default=None, alias="ebayCollectAndRemitTax")
    fulfillment_hrefs: Optional[List[StrictStr]] = Field(default=None, alias="fulfillmentHrefs")
    fulfillment_start_instructions: Optional[List[FulfillmentStartInstruction]] = Field(
        default=None, alias="fulfillmentStartInstructions"
    )
    last_modified_date: Optional[StrictStr] = Field(default=None, alias="lastModifiedDate")
    line_items: Optional[List[LineItem]] = Field(default=None, alias="lineItems")
    order_fulfillment_status: Optional[StrictStr] = Field(default=None, alias="orderFulfillmentStatus")
    order_id: Optional[StrictStr] = Field(default=None, alias="orderId")
    order_payment_status: Optional[StrictStr] = Field(default=None, alias="orderPaymentStatus")
    payment_summary: Optional[PaymentSummary] = Field(default=None, alias="paymentSummary")
    pricing_summary: Optional[PricingSummary] = Field(default=None, alias="pricingSummary")
    program: Optional[Program] = None
    sales_record_reference: Optional[StrictStr] = Field(default=None, alias="salesRecordReference")
    seller_id: Optional[StrictStr] = Field(default=None, alias="sellerId")
    total_fee_basis_amount: Optional[Amount] = Field(default=None, alias="totalFeeBasisAmount")
    total_marketplace_fee: Optional[Amount] = Field(default=None, alias="totalMarketplaceFee")
