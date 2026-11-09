# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.amount import Amount
from ebay_sell.post_order.models.claim_history_response import ClaimHistoryResponse
from ebay_sell.post_order.models.inquiry_details import InquiryDetails
from ebay_sell.post_order.models.item_details import ItemDetails
from ebay_sell.post_order.models.resolution_estimate import ResolutionEstimate
from ebay_sell.post_order.models.return_address import ReturnAddress
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell.post_order.models.user_party_enum import UserPartyEnum
from ebay_sell._runtime import ApiModel


class InquiryDetailsResponse(ApiModel):
    """InquiryDetailsResponse model."""

    claim_amount: Optional[Amount] = Field(default=None, alias="claimAmount")
    creation_reason: Optional[StrictStr] = Field(default=None, alias="creationReason")
    ext_transaction_id: Optional[StrictStr] = Field(default=None, alias="extTransactionId")
    initiator: Optional[UserPartyEnum] = None
    inquiry_closure_date: Optional[Timestamp] = Field(default=None, alias="inquiryClosureDate")
    inquiry_content_on_hold: Optional[StrictBool] = Field(default=None, alias="inquiryContentOnHold")
    inquiry_details: Optional[InquiryDetails] = Field(default=None, alias="inquiryDetails")
    inquiry_history_details: Optional[ClaimHistoryResponse] = Field(default=None, alias="inquiryHistoryDetails")
    inquiry_id: Optional[StrictStr] = Field(default=None, alias="inquiryId")
    inquiry_quantity: Optional[StrictInt] = Field(default=None, alias="inquiryQuantity")
    item_details: Optional[ItemDetails] = Field(default=None, alias="itemDetails")
    item_id: Optional[StrictStr] = Field(default=None, alias="itemId")
    return_details: Optional[ReturnAddress] = Field(default=None, alias="returnDetails")
    seller_make_it_right_by_date: Optional[Timestamp] = Field(default=None, alias="sellerMakeItRightByDate")
    resolution_estimate: Optional[ResolutionEstimate] = Field(default=None, alias="resolutionEstimate")
    shipping_cost: Optional[Amount] = Field(default=None, alias="shippingCost")
    state: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    transaction_id: Optional[StrictStr] = Field(default=None, alias="transactionId")
    view_pp_trasanction_url: Optional[StrictStr] = Field(default=None, alias="viewPPTrasanctionUrl")
