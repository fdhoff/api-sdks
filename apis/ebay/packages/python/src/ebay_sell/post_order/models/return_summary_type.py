# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ebay_sell.post_order.models.available_option_type import AvailableOptionType
from ebay_sell.post_order.models.escalation_info_type import EscalationInfoType
from ebay_sell.post_order.models.return_creation_info_type import ReturnCreationInfoType
from ebay_sell.post_order.models.return_policy_type import ReturnPolicyType
from ebay_sell.post_order.models.return_response_due_type import ReturnResponseDueType
from ebay_sell.post_order.models.return_state_enum import ReturnStateEnum
from ebay_sell.post_order.models.return_status_enum import ReturnStatusEnum
from ebay_sell.post_order.models.return_type_enum import ReturnTypeEnum
from ebay_sell.post_order.models.timestamp import Timestamp
from ebay_sell.post_order.models.total_refund_amount_type import TotalRefundAmountType
from ebay_sell._runtime import ApiModel


class ReturnSummaryType(ApiModel):
    """ReturnSummaryType model."""

    buyer_available_options: Optional[List[AvailableOptionType]] = Field(default=None, alias="buyerAvailableOptions")
    buyer_login_name: Optional[StrictStr] = Field(default=None, alias="buyerLoginName")
    buyer_response_due: Optional[ReturnResponseDueType] = Field(default=None, alias="buyerResponseDue")
    buyer_total_refund: Optional[TotalRefundAmountType] = Field(default=None, alias="buyerTotalRefund")
    creation_info: Optional[ReturnCreationInfoType] = Field(default=None, alias="creationInfo")
    current_type: Optional[ReturnTypeEnum] = Field(default=None, alias="currentType")
    escalation_info: Optional[EscalationInfoType] = Field(default=None, alias="escalationInfo")
    order_id: Optional[StrictStr] = Field(default=None, alias="orderId")
    return_id: Optional[StrictStr] = Field(default=None, alias="returnId")
    return_policy: Optional[ReturnPolicyType] = Field(default=None, alias="returnPolicy")
    seller_available_options: Optional[List[AvailableOptionType]] = Field(default=None, alias="sellerAvailableOptions")
    seller_login_name: Optional[StrictStr] = Field(default=None, alias="sellerLoginName")
    seller_response_due: Optional[ReturnResponseDueType] = Field(default=None, alias="sellerResponseDue")
    seller_total_refund: Optional[TotalRefundAmountType] = Field(default=None, alias="sellerTotalRefund")
    state: Optional[ReturnStateEnum] = None
    status: Optional[ReturnStatusEnum] = None
    timeout_date: Optional[Timestamp] = Field(default=None, alias="timeoutDate")
