# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.action_deadlines import ActionDeadlines
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.appeal_details import AppealDetails
from ebay_sell.post_order.models.case_details import CaseDetails
from ebay_sell.post_order.models.case_type_enum import CaseTypeEnum
from ebay_sell.post_order.models.claim_history_response import ClaimHistoryResponse
from ebay_sell.post_order.models.return_address import ReturnAddress
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell.post_order.models.user_party_enum import UserPartyEnum
from ebay_sell._runtime import ApiModel


class CaseDetailsResponse(ApiModel):
    """CaseDetailsResponse model."""

    action_deadlines: Optional[ActionDeadlines] = Field(default=None, alias="actionDeadlines")
    appeal_details: Optional[AppealDetails] = Field(default=None, alias="appealDetails")
    buyer_closure_reason: Optional[StrictStr] = Field(default=None, alias="buyerClosureReason")
    buyer_protected_program_link: Optional[StrictStr] = Field(default=None, alias="buyerProtectedProgramLink")
    case_details: Optional[CaseDetails] = Field(default=None, alias="caseDetails")
    case_history_details: Optional[ClaimHistoryResponse] = Field(default=None, alias="caseHistoryDetails")
    case_id: Optional[StrictStr] = Field(default=None, alias="caseId")
    case_quantity: Optional[StrictInt] = Field(default=None, alias="caseQuantity")
    case_type: Optional[CaseTypeEnum] = Field(default=None, alias="caseType")
    claim_amount: Optional[Amount] = Field(default=None, alias="claimAmount")
    creation_date: Optional[Timestamp] = Field(default=None, alias="creationDate")
    escalated_by: Optional[UserPartyEnum] = Field(default=None, alias="escalatedBy")
    escalate_reason: Optional[StrictStr] = Field(default=None, alias="escalateReason")
    event_tickets_link: Optional[StrictStr] = Field(default=None, alias="eventTicketsLink")
    ext_transaction_id: Optional[StrictStr] = Field(default=None, alias="extTransactionId")
    fsnad_days_to_add_tracking_after_shipping_item: Optional[StrictInt] = Field(
        default=None, alias="fsnadDaysToAddTrackingAfterShippingItem"
    )
    fsnad_ship_to_seller_by_date: Optional[Timestamp] = Field(default=None, alias="fsnadShipToSellerByDate")
    initiator: Optional[UserPartyEnum] = None
    case_content_on_hold: Optional[StrictBool] = Field(default=None, alias="caseContentOnHold")
    item_id: Optional[StrictStr] = Field(default=None, alias="itemId")
    item_on_hold: Optional[StrictBool] = Field(default=None, alias="itemOnHold")
    last_modified_date: Optional[Timestamp] = Field(default=None, alias="lastModifiedDate")
    pay_for_item_link: Optional[StrictStr] = Field(default=None, alias="payForItemLink")
    price_signature_confirmation_amount: Optional[StrictStr] = Field(
        default=None, alias="priceSignatureConfirmationAmount"
    )
    recalled_item_link: Optional[StrictStr] = Field(default=None, alias="recalledItemLink")
    return_details: Optional[ReturnAddress] = Field(default=None, alias="returnDetails")
    return_id: Optional[StrictStr] = Field(default=None, alias="returnId")
    seller_closure_reason: Optional[StrictStr] = Field(default=None, alias="sellerClosureReason")
    shipping_fee: Optional[Amount] = Field(default=None, alias="shippingFee")
    status: Optional[StrictStr] = None
    transaction_id: Optional[StrictStr] = Field(default=None, alias="transactionId")
