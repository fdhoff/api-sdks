# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.fulfillment.models.dispute_evidence import DisputeEvidence
from ebay_sell.fulfillment.models.evidence_request import EvidenceRequest
from ebay_sell.fulfillment.models.info_from_buyer import InfoFromBuyer
from ebay_sell.fulfillment.models.monetary_transaction import MonetaryTransaction
from ebay_sell.fulfillment.models.order_line_items import OrderLineItems
from ebay_sell.fulfillment.models.payment_dispute_outcome_detail import PaymentDisputeOutcomeDetail
from ebay_sell.fulfillment.models.return_address import ReturnAddress
from ebay_sell.fulfillment.models.simple_amount import SimpleAmount
from ebay_sell._runtime import ApiModel


class PaymentDispute(ApiModel):
    """PaymentDispute model."""

    amount: Optional[SimpleAmount] = None
    available_choices: Optional[List[StrictStr]] = Field(default=None, alias="availableChoices")
    buyer_provided: Optional[InfoFromBuyer] = Field(default=None, alias="buyerProvided")
    buyer_username: Optional[StrictStr] = Field(default=None, alias="buyerUsername")
    closed_date: Optional[StrictStr] = Field(default=None, alias="closedDate")
    evidence: Optional[List[DisputeEvidence]] = None
    evidence_requests: Optional[List[EvidenceRequest]] = Field(default=None, alias="evidenceRequests")
    line_items: Optional[List[OrderLineItems]] = Field(default=None, alias="lineItems")
    monetary_transactions: Optional[List[MonetaryTransaction]] = Field(default=None, alias="monetaryTransactions")
    note: Optional[StrictStr] = None
    open_date: Optional[StrictStr] = Field(default=None, alias="openDate")
    order_id: Optional[StrictStr] = Field(default=None, alias="orderId")
    payment_dispute_id: Optional[StrictStr] = Field(default=None, alias="paymentDisputeId")
    payment_dispute_status: Optional[StrictStr] = Field(default=None, alias="paymentDisputeStatus")
    reason: Optional[StrictStr] = None
    resolution: Optional[PaymentDisputeOutcomeDetail] = None
    respond_by_date: Optional[StrictStr] = Field(default=None, alias="respondByDate")
    return_address: Optional[ReturnAddress] = Field(default=None, alias="returnAddress")
    revision: Optional[StrictInt] = None
    seller_response: Optional[StrictStr] = Field(default=None, alias="sellerResponse")
