# coding: utf-8

# Generated code. Do not edit by hand; change the templates, the overlay or the runtime instead.


from __future__ import annotations

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from uuid import UUID
from mercury_banking.models.payment_approval_review import PaymentApprovalReview
from mercury_banking.models.request_send_money_payment_method import RequestSendMoneyPaymentMethod
from mercury_banking.models.review_request_status import ReviewRequestStatus
from mercury_banking._runtime import ApiModel


class SendMoneyApprovalRequestResponse(ApiModel):
    """SendMoneyApprovalRequestResponse model."""

    account_id: UUID = Field(alias="accountId")
    amount: Annotated[float, Field(ge=0.01)]
    created_at: StrictStr = Field(alias="createdAt")
    memo: Optional[StrictStr] = None
    number_of_approvers_required: Optional[
        Annotated[int, Field(le=9223372036854776000, strict=True, ge=-9223372036854776000)]
    ] = Field(default=None, alias="numberOfApproversRequired")
    payment_method: RequestSendMoneyPaymentMethod = Field(alias="paymentMethod")
    recipient_id: UUID = Field(alias="recipientId")
    request_id: StrictStr = Field(alias="requestId")
    requested_by_user_id: UUID = Field(alias="requestedByUserId")
    requester_may_approve: Optional[StrictBool] = Field(default=None, alias="requesterMayApprove")
    reviews: List[PaymentApprovalReview]
    scheduled_send_date: Optional[date] = Field(default=None, alias="scheduledSendDate")
    status: ReviewRequestStatus
